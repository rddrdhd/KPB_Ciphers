from Helper import Helper


class Cipher:
    # Zadání (01 - 14.2.2022):
    # Naimplementujte zobecněnou Caesarovu šifru, tedy šifrovací algoritmus označovaný jako Shift cipher.
    # Pracujte s přípustnou abecedou obsahující jen znaky anglické abecedy bez mezery, a to velká písmena.
    # Implementujte jak šifrování, tak dešifrování. Ošetřete situaci, kdy v otevřeném textu budou nepřípustné
    # znaky a malá písmena. Vytvořte jednoduché GUI (stačí na příštím cvičení) pro vstup otevřeného textu, výstup šifrového,
    # čtení / zápis ze soboru atd.
    @staticmethod
    def alphabet_shift(text, key):
        # only upper aphabetic letters
        text = Helper.get_clean_text(text)

        result = ""
        for i in range(len(text)):
            letter = text[i]
            # mapping letters to int, 65==A
            result += chr((ord(letter) + key - 65) % 26 + 65)
        return {"shift": key, "shiftback": 26 - key, "input": text, "result": result}

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

    # Zadání (02 - 21.2.2022): http://www.cs.vsb.cz/ochodkova/courses/kpb/Cviceni%202_2022.pdf
    # Pracujte s přípustnou abecedou obsahující jen znaky anglické
    # abecedy bez mezery. Implementujte jak šifrování, tak dešifrování.
    @staticmethod
    def vigener(coded_text, key, decrypt=True):  # Todo decrypt
        r = ""
        for i, char in enumerate(coded_text):
            key_char = key[i % len(key)]
            key_number = Helper.ALPHABET.index(key_char)
            result_char = Cipher.alphabet_shift(char, key_number)
            r += result_char["result"]
        return r

    # Zadání (02 - 21.2.2022):
    # Naimplementujte transpoziční šifru: columnar + row transposition
    # Pracujte s přípustnou abecedou obsahující jen znaky anglické abecedy bez mezery.
    # Implementujte jak šifrování, tak dešifrování.
    @staticmethod
    def transposition(coded_text, key, encrypt=True):  # TODO decrypt
        # Fill the original message with padding
        coded_text = Helper.fill_with_padding("X", len(key), coded_text)

        result_by_rows = ""
        result_by_cols = ""
        max_rows = int(len(coded_text) / len(key))

        # build the transposition matrix
        matrix = Helper.get_empty_matrix(max_rows, len(key))
        for i, char in enumerate(coded_text):
            row_number = int(i / len(key))
            column_number = i % len(key)

            new_column_number = key.index(str(column_number + 1))
            matrix[row_number][new_column_number] = char

        # read by rows
        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                result_by_rows += cell

        # read by columns
        for x in range(len(key)):
            result_by_cols += ''.join([row[x] for row in matrix])

        return {
            'rowTransposition': result_by_rows,
            'colTransposition': result_by_cols,
            'matrix': matrix,
        }
