import random
class Helper:
    ALPHABET_LENGHT = 26
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    @staticmethod
    def getRandomPermutation(string):
        str_var = list(string)
        random.shuffle(str_var)
        return ''.join(str_var)

    @staticmethod
    def getCleanText(text):
        return ''.join([i for i in text.upper() if i.isalpha()])