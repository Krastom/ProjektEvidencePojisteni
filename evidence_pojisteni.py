from pojisteny import Pojisteny

class EvidencePojisteni:

    def __init__(self):
        self.pojisteni_list = []

    def pridat_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni_list.append(pojisteny)

    def zobrazit_seznam_pojistenych(self):
        print("Seznam pojištěných:")
        for pojisteny in self.pojisteni_list:
            print(pojisteny)

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        print(f"Vyhledávání pojistěného s jménem '{jmeno} {prijmeni}':")
        for pojisteny in self.pojisteni_list:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny)

    def __str__(self):
        return f"Celkový počet pojistěných osob: {len(self.pojisteni_list)}"