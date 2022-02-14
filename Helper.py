import random
class Helper:
    @staticmethod
    def getRandomPermutation(string):
        str_var = list(string)
        random.shuffle(str_var)
        return ''.join(str_var)