import random

numbers = "0123456789"

while 1:
    try:
        num_count = int(input("Hoeveel 'burgerservicenummers' wil je genereren? : "))
        for a in range(0,num_count):
            bsn_num = ""
            for a in range(0, 9):
                num_char = random.choice(numbers)
                bsn_num      = bsn_num + num_char
            print("Je gegenereerde burgerservicenummer is : ", bsn_num)
    except ValueError as e:
        print("Fout: Controlleer of je laatste wijziging!", e)
    
    except NameError as e: 
        print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)

    except SyntaxError as e:
        print("Fout: Controlleer op typfouten of onjuiste wijzigingen!", e)