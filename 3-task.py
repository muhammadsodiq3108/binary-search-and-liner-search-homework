students = ["bobur", "mansur", "sardor", "aziz", "madina"]

ism = input("ism kiriting : ")

topildi = False

for i in range(len(students)):
    if students[i] == ism.strip():
        print(f"{ism} topildi")
        print("index:", i)
        topildi = True
    
if not topildi:
    print("noo")
