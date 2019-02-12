class Controller_Propozitii:
    propRepo = None

    def __init__(self, Propozitii):
        self.propRepo = Propozitii

    def read_propozitii(self):
        return self.propRepo.read_propozitii()

class Controller_Propozitii_Magice:
    propmagRepo = None

    def __init__(self, Propozitii_Magice):
        self.propmagRepo = Propozitii_Magice

    def read_propozitii(self):
        return self.propmagRepo.read_propozitii_magice()