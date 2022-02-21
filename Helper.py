import random


class Helper:

    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALPHABET_LENGHT = len(ALPHABET)

    @staticmethod
    def get_random_permutation(string):
        str_var = list(string)
        random.shuffle(str_var)
        return ''.join(str_var)

    @staticmethod
    def get_clean_text(text):
        return ''.join([i for i in text.upper() if i.isalpha()])

    @staticmethod
    def get_empty_matrix(x, y):
        matrix = []
        for i in range(x):
            matrix.append([])
            for j in range(y):
                matrix[i].append('')
        return matrix

    @staticmethod
    def fill_with_padding(padding_char, key_length, coded_text):
        coded_text = Helper.get_clean_text(coded_text)
        while len(coded_text) % key_length != 0:
            coded_text += padding_char
        return coded_text

    @staticmethod
    def get_trans_key_from_word(word):

