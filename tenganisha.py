# Programu ya AI ya kutenganisha maneno
def tenganisha_maneno(sentensi):
    maneno = sentensi.split()
    return maneno

print("PROGRAMU YA KUTENGANISHA MANENO")
sentensi = input("Andika sentensi: ")
matokeo = tenganisha_maneno(sentensi)

print(f"Maneno {len(matokeo)} yamepatikana:")
for i, neno in enumerate(matokeo, 1):
    print(f"{i}. {neno}")
