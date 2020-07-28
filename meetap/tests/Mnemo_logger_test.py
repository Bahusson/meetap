"""Test generatora identyfikatorów mnemotechnicznych"""

import random


class Mnemo_logger(object):
    # Program generuje login z losowych sylab i 3 cyfr, który
    # jest w ten sposób stosunkowo łatwy do zapamiętania.

    def gen_login(self):
        vowels = ['a', 'e']
        # , 'i', 'o', 'u', 'y']
        consonants = [
         'b', 'c', 'd', 'f', 'g', 'h', 'j',
         'k', 'l', 'm', 'n', 'p', 'r', 's',
         't', 'w', 'z']

    #    L1 = random.choice(consonants).capitalize()
        L2 = random.choice(vowels)
    #    L3 = random.choice(consonants)
    #    L4 = random.choice(vowels)
    #    L5 = random.choice(consonants)
    #    L6 = random.choice(vowels)
    #    L7 = random.choice(consonants)
    #    L8 = random.choice(vowels)
        L9 = str(random.randint(1,9))

        # fulllogin = L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
        fulllogin = L2 + L9
        return fulllogin

    # Ten kawałek sprawdza czy login znajduje się już na liście loginów.
    def checkifonlist(self, loginslist):
        loglistlen = len(loginslist)
        newlogin = self.gen_login()
        while loglistlen > 0:
            for login in loginslist:
                loglistlen -= 1
                print(loglistlen)
                if login == newlogin:
                    print("repeats " + newlogin)
                    loglistlen = len(loginslist)
                    newlogin = self.gen_login()
                    break
        print(newlogin)
        return newlogin


loginslist = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']

mnemlog = Mnemo_logger()
mnemlog.checkifonlist(loginslist)
