from unicodedata import name


def run():
    pass

total = 0
for i in range(10, 21):   
    if i % 2 != 0:
        continue 
    total = total + i
    
    print(i)
print("El total es = " , total)

# x = input("Hasta que numero quieres contar: " )

# for x in range(x):
#     print(x)


if __name__ == "__main__":
    run()