from Repository import *
from Controller import*

def meniu():
    '''
    Meniul are 2 optiuni numerotate de la 1 la 3. Daca optiunea aleasa
    nu exista se va afisa un mesaj de eroare si se va introduce o noua optiune
    pana la alegerea optiunii 3
    '''

    print(' ')
    print('1. Afisare propozitii magice')
    print('2. Afisare propozitii cu procent')
    print('3. Exit')
    print(' ')

    opt = input('Alegeti o optiune: ')
    while opt < '1' or opt > '5':
        print('Optiunea aleasa nu exista')
        opt = input('Alegeti o optiune: ')
    print(' ')

    prop_repo = Propozitii()
    prop_control = Controller_Propozitii(prop_repo)
    propozitii = prop_control.read_propozitii()  # preiau lista cu toate propozitile

    prop_m_repo = Propozitii_Magice()
    prop_m_control = Controller_Propozitii_Magice(prop_m_repo)
    propozitii_magice = prop_m_control.read_propozitii()  # preiau lista cu toate propozitile magice
    w = open('procent.txt', 'w')

    while '3':
        if opt == '1':
            # parcurg propozitile pe rand, iar in acelasi timp parcurg si propozitile magice
            # pentru fiecare propozitie
            for i in range (len(propozitii_magice)):
                for j in range (len(propozitii)):
                    if propozitii[j] == propozitii_magice[i]:
                        # daca sunt la fel le afisez impreuna cu linia in fisier
                        # pun i+1 deoarece in fisier primul rand are valoarea 1 iar i incepe de la 0
                        print(propozitii_magice[i], 'identica, linia', j+1) # j+1 deoarece in fisier primul rand are numarul 1

        if opt == '2':
            for i in range (len(propozitii_magice)): # parcurg lista de propozitii magice propozitie cu propozitie
                for j in range (len(propozitii)): # parcurg la fel lista de propozitii de la lab 6
                    procent = 0
                    for k in range (len(propozitii_magice[i])): # parcurg propozitile cuvant cu cuvant elem
                        for l in range(len(propozitii[j])): # si compar fiecare element cu fiecare din celalalt tip de propozitie
                            if propozitii_magice[i][k] == propozitii[j][l]: #daca e vreuna la fel o numar
                                procent += 1
                    if procent != 0: # inainte sa trec la urmatoarea propoztitie afisez propozitia si procentul
                        p = procent/len(propozitii[j]) * 100
                        format(p, '.2f')
                        print(propozitii[j], '-', p, '% identica')
                        w.write(str(propozitii[j]) + ' - ' + str(p) + '% identica\n')

        if opt == '3':
            break

        opt = input('\nAlegeti o optiune: ')
        while opt < '1' or opt > '5':
            print('Optiunea aleasa nu exista')
            opt = input('Alegeti o optiune: ')
        print(' ')

meniu()