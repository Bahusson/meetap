
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
