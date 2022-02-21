from Helper import Helper

class Cipher:
    # Zadání (01 - 14.2.2022):
    # Naimplementujte zobecněnou Caesarovu šifru, tedy šifrovací algoritmus označovaný jako Shift cipher.
    # Pracujte s přípustnou abecedou obsahující jen znaky anglické abecedy bez mezery, a to velká písmena.
    # Implementujte jak šifrování, tak dešifrování. Ošetřete situaci, kdy v otevřeném textu budou nepřípustné
    # znaky a malá písmena. Vytvořte jednoduché GUI (stačí na příštím cvičení) pro vstup otevřeného textu, výstup šifrového,
    # čtení / zápis ze soboru atd.
    @staticmethod
    def shift(text, key):
        # only upper aphabetic letters
        text = ''.join([i for i in text.upper() if i.isalpha()])

        result = ""
        for i in range(len(text)):
            letter = text[i]
            # mapping letters to int, 65==A
            result += chr((ord(letter) + key-65) % 26 + 65)
        return {"shift": key, "shiftback": 26-key, "input": text, "result": result}

    # Zadání (01 - 14.2.2022):
    # Naimplementujte Obecnou substituční šifru.
    # Klíčem bude libovolná permutace anglické abecedy bez mezery
    # (ten bude vygenerován, nikoliv zadán).
    @staticmethod
    def substitute(coded_text, alphabet, key_alphabet):
        result = ""
        for i, char in enumerate(coded_text):
            result += key_alphabet[alphabet.index(char)]
        return result

    @staticmethod
    def vigener(coded_text, key, decrypt=True):
        r = ""
        for i, char in enumerate(coded_text):
            key_index = i % len(key)
            key_char = key[key_index]
            key_number = Helper.ALPHABET.index(key_char)
            #print(key[key_index])

            result = Cipher.shift(char,key_number)
            print("keychar:"+key_char)
            print("keynum:"+str(key_number))
            print("shiftback:"+str(result["shiftback"]))
            print("input:"+result["input"])
            print("result:"+result["result"])
            print()
            r += result["result"]
        return r
