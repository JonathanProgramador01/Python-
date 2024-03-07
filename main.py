import random
letter=['a',' b', 'c', 'd',' e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A',' B', 'C', 'D',' E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        ]

num=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','#','$','%','&','(',')','*','+']

print("Welcomee to the generator password: ")
nr_leter=int(input("Enter your number of leters: "))
nr_symbols=int(input("Enter the number of symbols: "))
nr_num=int(input("Enter the number of: "))


# letra=""
# for i in range(nr_leter):
#     ran=random.randint(0,51)
#     letra+=letter[ran]

# for i in range(nr_symbols):
#     ran=random.randint(0,8)
#     letra+=symbols[nr_symbols]

# for i in range(nr_num):
#     ran=random.randint(0,9)
#     letra+=num[ran]

# print(letra)

letra_list=[]
for i in range(1,nr_leter+1):
    letra_list.append(random.choice(letter))

for i in range(1,nr_symbols+1):
    letra_list.append(random.choice(symbols))

for i in range (1,nr_num+1):
    letra_list.append(random.choice(num))

random.shuffle(letra_list)
leter=""
for i in letra_list:
    leter+=i

print(leter)
