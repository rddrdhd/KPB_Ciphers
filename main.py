from Helper import Helper
from SymmetricCipher import Cipher
from view import Window

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cv2():
    zasifrovany_text = "LTTLQJHMHJSDSNUTRTHNZENAFYJQZRXPTSYWTQTZEIFOJOJONHMMJXQTOJXYJXYFQJGJEUJHSJKNWRFUWTYTUWNUWFANQFXUJHNFQSNITUQSJPITUWTMQNEJHJHMWTRJYJSUTPFEIJPIDEEFIFYJSJPIJSFNSYJWSJYZMJXQTEPTSYWTQZOJEIFSJSNAIFYFGFENPTRUWTRNYTAFSDHMMJXJQ"

    # CEASAR
    for i in range(len(ALPHABET)):
        print(Cipher.shift(zasifrovany_text, i))

    RANDOM_ALPHABET = Helper.getRandomAlphabet(ALPHABET)

    # OBECNY ALGORITMUS SUBSTITUCE
    C = "WIRFR WAJUH YFTSD VFSFU UFYA"
    SA = "DKVQFIBJWPESCXHTMYAUOLRGZN"
    M = Cipher.substitute(C, ALPHABET, SA)
    print(M)


if __name__ == '__main__':
    # cv2()
    cv02 = Window()
    cv02.run()
