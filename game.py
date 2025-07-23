hp = 100
rifle = 40
sword = 20
gun = 15
menu = input("เลือก ")

if menu == "y" :
    print("Welcome to Gamepaly ")
    round_attack = int(input("คุณต้องการตีกี่รอบ : "))
    print("Rifle Sword Gun")
    for i in range(round_attack) :
        
        select = input("Choose your Weapon : ")
        if select == "R" or select == "r" :
            hp = hp - rifle 
            print("เลือดปีศาจเหลือ : " , hp )
        elif select == "S" or select == "s":
            hp = hp - sword
            print("เลือดปีศาจเหลือ : " , hp )
        elif select == "G" or select == "g":
            hp = hp - gun
            print("เลือดปีศาจเหลือ : " , hp )
else :
    print("exit")
