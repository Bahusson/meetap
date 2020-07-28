import random


def menu_switcher(*args):
    # Podajesz listy argumentów w formacie:
    # [numer menu, menu_item, link_item]
    # Kolejność dowolna. Klucz ma ten numer menu który podałeś/aś w liście.
    menusdict = {}
    x = 0
    for arg in args:
        menusdict['menu'+str(args[x][0])] = args[x]
        x = x + 1
    return menusdict


class Mnemo_logger(object):
    # Program generuje unikalny login z losowych sylab i 3 cyfr, który
    # jest w ten sposób stosunkowo łatwy do zapamiętania.

    def gen_login(self):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        consonants = [
         'b', 'c', 'd', 'f', 'g', 'h', 'j',
         'k', 'l', 'm', 'n', 'p', 'r', 's',
         't', 'w', 'z']

        L1 = random.choice(consonants).capitalize()
        L2 = random.choice(vowels)
        L3 = random.choice(consonants)
        L4 = random.choice(vowels)
        L5 = random.choice(consonants)
        L6 = random.choice(vowels)
        L7 = random.choice(consonants)
        L8 = random.choice(vowels)
        L9 = str(random.randint(100, 999))

        fulllogin = L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
        return fulllogin

    # Ten kawałek sprawdza czy login znajduje się już na liście loginów.
    def checkifonlist(self, loginslist):
        loglistlen = len(loginslist)
        newlogin = self.gen_login()
        while loglistlen > 0:
            for login in loginslist:
                loglistlen -= 1
                # print(loglistlen)
                if login == newlogin:
                    # print("repeats " + newlogin)
                    loglistlen = len(loginslist)
                    newlogin = self.gen_login()
                    break
        # print(newlogin)
        return newlogin
