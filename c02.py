class Cipher:
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
            # using chr and ord mapping letters to int, 65==A
            result += chr((ord(letter) + key-65) % 26 + 65)
        return {"shift": key, "result": result}

    # Naimplementujte Obecnou substituční šifru.
    # Klíčem bude libovolná permutace anglické abecedy bez mezery
    # (ten bude vygenerován, nikoliv zadán).
    @staticmethod
    def substitute(coded_text, alphabet, key_alphabet):
        coded_text = ''.join([i for i in coded_text.upper() if i.isalpha()])
        alphabet = ''.join([i for i in alphabet.upper() if i.isalpha()])
        key_alphabet = ''.join([i for i in key_alphabet.upper() if i.isalpha()])
        result = ""
        for i, char in enumerate(coded_text):
            result += alphabet[key_alphabet.index(char)]
        return result

