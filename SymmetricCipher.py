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

    @staticmethod
    def vigener(coded_text, key, decrypt=True):  # Todo decrypt
        r = ""
        for i, char in enumerate(coded_text):
            key_index = i % len(key)
            key_char = key[key_index]
            key_number = Helper.ALPHABET.index(key_char)
            result = Cipher.shift(char, key_number)
            r += result["result"]
        return r

    @staticmethod
    def transposition(coded_text, key, encrypt=True):  # TODO decrypt
        while len(coded_text) % len(key) != 0:
            coded_text += "X"

        result_row_trans = ['' for i in range(len(coded_text))]
        result_col_trans = ['' for i in range(len(coded_text))]
        max_rows = int(len(coded_text) / len(key))
        matrix=[]
        for i in range(max_rows):
            matrix.append([])
            for j in range(len(key)):
                matrix[i].append('')

        for i, char in enumerate(coded_text):
            row_number = int(i / len(key))
            column_number = i % len(key)
            new_column_index = int(key[column_number])
            new_index_for_row_trans = (row_number * (len(key))) + new_column_index
            new_index_for_col_trans = (new_column_index * (len(key))) + row_number
            matrix[row_number][new_column_index-1] = char
            # print(str(row_number)+"*"+str(len(key))+"+"+str(new_column_index)+"=\t"+str(new_index))
            if char != "X":
                result_row_trans[new_index_for_row_trans - 1] = char
                result_col_trans[new_index_for_col_trans - 1] = char

            # result[i] = coded_text[new_index]



            # print(str(i)+":\t"+char+"("+str(column_number+1)+"->"+str(new_column_index)+")\t("+str(row_number)+")")

        return {
            'rowTransposition': "".join(result_row_trans),
            'colTransposition': "".join(result_col_trans),
            'matrix': matrix,
                }
