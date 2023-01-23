#3-ий Вариант.
#Harjutus 1. 
print("Harjutus 1.")
n = int(input("Введи число: "))
for i in range(n):
    print("   ----- ", end="")
    if i != n-1:
        print("    ", end="")
print("")
for i in range(n):
    print("  |  O  |", end="")
    if i != n-1:
        print("    ", end="")
print("")
for i in range(n):
    print("  !  -  !", end="")
    if i != n-1:
        print("    ", end="")
print("")
for i in range(n):
    print("   ----- ", end="")
    if i != n-1:
        print("    ", end="")
print("")
