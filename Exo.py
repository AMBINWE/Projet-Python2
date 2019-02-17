import random

mhd1_name = ""
mhd1_hp = 250

mhd2_name = ""
mhd2_hp = 250

random_attack = True
random_damage = 0

mhd1_name = input("joueur 1, choisissez un pseudo : ")
print(f"{mhd1_name}, est le joueur 1. ")

mhd2_name = input("joueur 2, choisissez un pseudo : ")
print(f"{mhd2_name}, est le joueur 2. ")

print("\n Le combat commence \n !")

# 1ère partie
input()
print(f"{mhd1_name}, à vous de commencer !")
print(f"{mhd1_name} : {mhd1_hp} PV / {mhd2_name} : {mhd2_hp} PV ")

random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attack réussit

    random_damage = random.randint(0, 100)
    print(f"{mhd2_name} subit une attaque de {mhd1_name} qui lui inflige {random_damage} points de dégats ")
    mhd2_hp -= random_damage

else:
    # Si l'attaque échoue
    print(f"{mhd1_name} rate son attaque...") 
    

# 2ème partie
input()
print(f"{mhd2_name}, à vous de jouer !")
print(f"{mhd1_name} : {mhd1_hp} PV / {mhd2_name} : {mhd2_hp} PV ")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attack réussit

    random_damage = random.randint(0, 100)
    print(f"{mhd1_name} subit une attaque de {mhd2_name} qui lui inflige {random_damage} points de dégats ")
    mhd1_hp -= random_damage

else:
    # Si l'attaque échoue
    print(f"{mhd2_name} rate son attaque...") 


# 3ème partie
input()
print(f"{mhd1_name}, à vous de jouer !")
print(f"{mhd1_name} : {mhd1_hp} PV / {mhd2_name} : {mhd2_hp} PV ")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attack réussit

    random_damage = random.randint(0, 100)
    print(f"{mhd2_name} subit une attaque de {mhd1_name} qui lui inflige {random_damage} points de dégats ")
    mhd2_hp -= random_damage

else:
    # Si l'attaque échoue
    print(f"{mhd1_name} rate son attaque...") 

# 4ème partie
input()
print(f"{mhd2_name}, à vous de jouer !")
print(f"{mhd1_name} : {mhd1_hp} PV / {mhd2_name} : {mhd2_hp} PV ")

random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attack réussit

    random_damage = random.randint(0, 100)
    print(f"{mhd1_name} subit une attaque de {mhd2_name} qui lui inflige {random_damage} points de dégats ")
    mhd1_hp -= random_damage

else:
    # Si l'attaque échoue
    print(f"{mhd2_name} rate son attaque...") 

# Résultat Final 
input()
print("\nFIN DU COMBAT \n")
print(f"{mhd1_name} : {mhd1_hp} PV / {mhd2_name} : {mhd2_hp} PV ")

if mhd1_hp > mhd2_hp :
    print(f"{mhd1_name}, remporte la victoire ! ")
elif mhd1_hp < mhd2_hp :
    print(f"{mhd2_name}, remporte la victoire ! ")
else :
    print("Match NUL !")


    
    
    