from evidence_pojisteni import EvidencePojisteni

evidence = EvidencePojisteni()

while True:
    print("1. Přidat pojištěného")
    print("2. Zobrazit seznam pojištěných")
    print("3. Vyhledat pojistěného")
    print("4. Konec")
    volba = input("Vyberte akci: ")

    if volba == "1":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")
        evidence.pridat_pojisteneho(jmeno, prijmeni, vek, telefon)
        print("Pojištěný byl úspěšně přidán. Pokračujte libovolnou klávesou..")
        input()
    elif volba == "2":
        evidence.zobrazit_seznam_pojistenych()
    elif volba == "3":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        evidence.vyhledat_pojisteneho(jmeno, prijmeni)
    elif volba == "4":
        break
    else:
        print("Neplatná volba. Zvolte prosím číslo akce.")

print(evidence)