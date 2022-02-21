import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

from Helper import Helper
from SymmetricCipher import Cipher

DEFAULT_ALPHABET = Helper.ALPHABET
p = 5  # padding value


class Window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('KPB | ZUR0037')
        self.row_count = 0
        self.alphabet = DEFAULT_ALPHABET
        self.key_string = "key string"

        self.cipher_text = tk.StringVar(self.root)
        self.shift_number = tk.IntVar(self.root)

    def cv02(self):
        vcmd = ('%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')  # for validating integer
        ttk.Label(self.root, text='\nCV1\n\nCeasarova šifra a obecná substituce\n').grid(row=self.row_count, column=1, ipadx=p, ipady=10)
        self.row_count += 1
        ttk.Label(self.root, text='Text k dekódování/zakódování').grid(row=self.row_count, column=0, ipadx=p, ipady=10)
        ciphertext_input = ttk.Entry(self.root, textvariable=self.cipher_text)
        ciphertext_input.grid(row=1, column=1, ipadx=p, ipady=p)
        ciphertext_input.focus()
        ttk.Button(self.root, text='Všechny posuny', command=lambda: self.button_clicked('BRUTEFORCE')).grid(row=1, column=2, ipadx=p, ipady=p)
        self.row_count += 1
        ttk.Label(self.root, text='Posun o kolik znaků').grid(row=self.row_count, column=0, ipadx=p, ipady=10)
        keynumber_input = ttk.Entry(self.root, textvariable=self.shift_number, validate='key', validatecommand=vcmd)
        keynumber_input.grid(row=2, column=1, ipadx=p, ipady=p)
        ttk.Button(self.root, text='Posun', command=lambda: self.button_clicked('NUMBER_KEY')).grid(row=2, column=2, ipadx=p, ipady=p)
        self.row_count += 1
        ttk.Label(self.root, text='Abeceda pro substituci').grid(row=self.row_count, column=0, ipadx=p, ipady=10)
        self.alphabet = tk.StringVar(self.root)
        self.alphabet.set(DEFAULT_ALPHABET)
        alphabet_input = ttk.Entry(self.root, textvariable=self.alphabet)
        alphabet_input.grid(row=3, column=1, ipadx=p, ipady=p)
        ttk.Button(self.root, text='Substituce', command=lambda: self.button_clicked('SUBSTITUTE')).grid(row=3, column=2, ipadx=p, ipady=p)
        self.row_count += 1
        ttk.Button(self.root, text='Výchozí abeceda', command=lambda: self.button_alphabet('DEFAULT_APLHABET')).grid(row=self.row_count, column=0, ipadx=p, ipady=p)
        ttk.Button(self.root, text='Vygenerovat náhodnou abecedu', command=lambda: self.button_alphabet('RANDOM_APLHABET')).grid(row=4, column=1, ipadx=p, ipady=p)
        self.row_count += 1


    def run(self):
        ttk.Label(self.root, text='\n\n\n').grid(row=self.row_count, column=1,
                                                                                     ipadx=p, ipady=10)

        ttk.Button(self.root, text='Konec',
                   command=lambda: self.root.quit()).grid(row=self.row_count, column=1, ipadx=p, ipady=p)
        self.root.mainloop()

    def button_alphabet(self, option):
        if option == 'RANDOM_APLHABET':
            self.alphabet.set(Helper.get_random_permutation(DEFAULT_ALPHABET))
        if option == 'DEFAULT_APLHABET':
            self.alphabet.set(DEFAULT_ALPHABET)

    def button_clicked(self, option):
        # Letters to upper
        ciphertext = ''.join([i for i in self.cipher_text.get().upper() if i.isalpha()])
        alphabet = ''.join(dict.fromkeys([i for i in self.alphabet.get().upper() if i.isalpha()])) # unique

        # Only 26 letters
        is_alphabet_good = all(c in DEFAULT_ALPHABET for c in alphabet.upper())
        is_ciphertext_good = all(c in DEFAULT_ALPHABET for c in ciphertext.upper())

        try:
            keynumber = self.shift_number.get()
            keynumber = int(keynumber) % len(alphabet) if keynumber.isnumeric() else 0
        except:
            keynumber = 0

        if len(ciphertext) == 0:
            showerror(title="Problém", message="Není vyplněný text k vyluštění.")

        elif len(alphabet) != 26 or not (is_alphabet_good, is_ciphertext_good):
            showerror(title="Délka abecedy",
                      message="Abeceda musí mít 26 unikátních znaků. Teď jich má " + str(len(alphabet)) + ".")
        else:  # valid input
            message = "Původní text:\n"
            message += ciphertext + "\n\n"
            message += "Klíč:\n"

            if option == 'BRUTEFORCE':  # Show all 26 shifts
                message += DEFAULT_ALPHABET + "\n\n"
                message += "Posun:\tvýsledek:\n"
                for i in range(len(alphabet)):
                    result = Cipher.alphabet_shift(ciphertext, i)
                    message += ">" + str(result["shift"]) + "\t" + result["result"] + "\n"
                showinfo(title="Result", message=message)

            elif option == 'NUMBER_KEY':  # show one shift
                message += DEFAULT_ALPHABET + "\n\n"
                message += "Posun:\tvýsledek:\n"
                try:
                    keynumber = int(self.shift_number.get()) % len(alphabet)
                    result = Cipher.alphabet_shift(ciphertext, keynumber)
                    message += ">" + str(result["shift"]) + "\t" + result["result"] + "\n"
                    showinfo(title="Result", message=message)
                except:
                    showwarning(title="Problém", message="Číslo posunu není validní číslo")


            elif option == 'SUBSTITUTE':
                message += str(self.alphabet) + "\n\n"
                message += "výsledek:\n"
                message += Cipher.substitute(ciphertext, DEFAULT_ALPHABET, alphabet)
                showinfo(title="Result", message=message)
            else:
                print("idk")

    def cv03(self):
        ttk.Label(self.root, text='\nCV2\n\nVigenerova a transpoziční šifra\n').grid(row=self.row_count, column=1, ipadx=p, ipady=10)
        self.row_count += 1
        ttk.Label(self.root, text='Text k dekódování/zakódování').grid(row=self.row_count, column=0, ipadx=p, ipady=10)
        ciphertext_input = ttk.Entry(self.root, textvariable=self.cipher_text)
        ciphertext_input.grid(row=self.row_count, column=1, ipadx=p, ipady=p)
        ciphertext_input.focus()

        self.row_count += 1
        key_input = ttk.Entry(self.root, textvariable=self.key_string)
        key_input.grid(row=self.row_count, column=1, ipadx=p, ipady=p)
        ttk.Button(self.root,
                   text='Vigenerova šifra',
                   command=lambda: self.button_clicked('VIGENER')
                   ).grid(row=self.row_count, column=2, ipadx=p, ipady=p)
        self.row_count += 1
        #TODO zbytek


