import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

from Helper import Helper
from SymmetricCipher import Cipher

DEFAULT_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = 5  # padding value


class Window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('KPB | ZUR0037')

        vcmd = ('%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')  # for validating integer

        #
        ttk.Label(self.root, text='Ceasarova šifra a obecná substituce\n').grid(row=0, column=1, ipadx=p, ipady=10)
        ##
        ttk.Label(self.root, text='Text k dekódování/zakódování').grid(row=1, column=0, ipadx=p, ipady=10)

        self.ciphertext = tk.StringVar(self.root)
        ciphertext_input = ttk.Entry(self.root, textvariable=self.ciphertext)
        ciphertext_input.grid(row=1, column=1, ipadx=p, ipady=p)
        ciphertext_input.focus()

        ttk.Button(self.root, text='Všechny posuny',
                   command=lambda: self.button_clicked('BRUTEFORCE')) \
            .grid(row=1, column=2, ipadx=p, ipady=p)

        ###
        ttk.Label(self.root, text='Posun o kolik znaků').grid(row=2, column=0, ipadx=p, ipady=10)

        self.keynumber = tk.IntVar(self.root)
        keynumber_input = ttk.Entry(self.root, textvariable=self.keynumber, validate='key', validatecommand=vcmd)
        keynumber_input.grid(row=2, column=1, ipadx=p, ipady=p)

        ttk.Button(self.root, text='Posun',
                   command=lambda: self.button_clicked('NUMBER_KEY')) \
            .grid(row=2, column=2, ipadx=p, ipady=p)

        ####
        ttk.Label(self.root, text='Abeceda pro substituci').grid(row=3, column=0, ipadx=p, ipady=10)

        self.alphabet = tk.StringVar(self.root)
        self.alphabet.set(DEFAULT_ALPHABET)
        alphabet_input = ttk.Entry(self.root, textvariable=self.alphabet)
        alphabet_input.grid(row=3, column=1, ipadx=p, ipady=p)

        ttk.Button(self.root, text='Substituce',
                   command=lambda: self.button_clicked('SUBSTITUTE')).grid(row=3, column=2, ipadx=p, ipady=p)
        #####
        ttk.Button(self.root, text='Výchozí abeceda',
                   command=lambda: self.button_clicked('DEFAULT_APLHABET')).grid(row=4, column=0, ipadx=p, ipady=p)
        ttk.Button(self.root, text='Vygenerovat náhodnou abecedu',
                   command=lambda: self.button_clicked('RANDOM_APLHABET')).grid(row=4, column=1, ipadx=p, ipady=p)
        ######
        ttk.Button(self.root, text='Konec',
                   command=lambda: self.root.quit()).grid(row=10, column=2, ipadx=p, ipady=p)

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def run02(self):
        self.root.mainloop()

    def button_clicked(self, option):

        if option == 'RANDOM_APLHABET':
            self.alphabet.set(Helper.getRandomPermutation(DEFAULT_ALPHABET))
        if option == 'DEFAULT_APLHABET':
            self.alphabet.set(DEFAULT_ALPHABET)
        else:
            # Letters to upper
            ciphertext = ''.join([i for i in self.ciphertext.get().upper() if i.isalpha()])
            alphabet = ''.join([i for i in self.alphabet.get().upper() if i.isalpha()])
            alphabet = "".join(dict.fromkeys(alphabet))  # unique for Ceasar

            # Only 26 letters
            is_alphabet_good = all(c in DEFAULT_ALPHABET for c in alphabet.upper())
            is_ciphertext_good = all(c in DEFAULT_ALPHABET for c in ciphertext.upper())

            try:
                keynumber = self.keynumber.get()
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
            message += alphabet + "\n\n"

            if option == 'BRUTEFORCE':  # Show all 26 shifts
                message += "Posun:\tvýsledek:\n"
                for i in range(len(alphabet)):
                    result = Cipher.shift(ciphertext, i)
                    message += ">" + str(result["shift"]) + "\t" + result["result"] + "\n"
                showinfo(title="Result", message=message)

            elif option == 'NUMBER_KEY':  # show one shift
                message += "Posun:\tvýsledek:\n"
                try:
                    keynumber = int(self.keynumber.get()) % len(alphabet)
                    result = Cipher.shift(ciphertext, keynumber)
                    message += ">" + str(result["shift"]) + "\t" + result["result"] + "\n"
                    showinfo(title="Result", message=message)
                except:
                    showwarning(title="Problém", message="Číslo posunu není validní číslo")


            elif option == 'SUBSTITUTE':
                message += "výsledek:\n"

                message += Cipher.substitute(ciphertext, DEFAULT_ALPHABET, alphabet)

                showinfo(title="Result", message=message)
