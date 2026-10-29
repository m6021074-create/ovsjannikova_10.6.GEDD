pareiza_parole="9"
atlikusie_meginajumi=3

while atlikusie_meginajumi > 0:
    parole = input("Ievadi paroli: ")
    if parole == pareiza_parole:
        print("Piekļuva atļauta")
        break

    atlikusie_meginajumi -= 1
    if atlikusie_meginajumi > 0:
        print(f"Nepareiza parole. Atlikušais mēģinājumu skaits: {atlikusie_meginajumi}")
    else:
        print("Piekļuve bloķēta")


