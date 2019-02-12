#from Propozitii import Propozitie
class Citire:

    def read(self, f):
        # citesc linie cu linie, adica propozitie cu propozitie din fisier si adaug la lista
        lista = []
        line = f.readline().strip()
        while line != "":
            t = line.split("\n")
            l = []
            for i in range(len(t)):
                l = t[i].split(" ")
            lista.append(l)
            line = f.readline().strip()
        f.close()
        return lista


class Propozitii(Citire):
    lista_propozitii = []

    def __init__(self):
        self.lista_propozitii = []

    def read_propozitii(self):
        #citesc fiecare propozitie din propozitii.txt, is le pun in lista_propozitii
        f = open('D:\FAC\PyCharm\lab6\propozitii.txt', 'r')
        return Citire.read(self,f)


class Propozitii_Magice(Citire):
    lista_propozitii_magice = []

    def __init__(self):
        self.lista_propozitii_magice = []

    def read_propozitii_magice(self):
        f = open('propozitiiMagice.txt', 'r')
        return Citire.read(self,f)