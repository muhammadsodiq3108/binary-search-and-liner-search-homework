kontakt = [
    "bobur",
    "mansur",
    "sardor",
    "aziz",
    "madina"
]

ism = input("Ism kiriting: ")

if ism.strip() in kontakt:
    print("Kontakt topildi")
else:
    print("Kontakt topilmadi")