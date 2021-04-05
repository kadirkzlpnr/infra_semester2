#import van benodigde librarie voor het lezen van de .txt file
import csv

def main():
    try:
        with open("users.txt","r") as file: # lezen van de .txt file met de users data
            file_reader = csv.reader(file)
            user_find(file_reader)
            file.close()
    except NameError as e:
        print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)
    except FileNotFoundError as e:
        print("Fout: Controlleer of je de juiste data file hebt toegewezen!")
    except SyntaxError as e:
        print("Fout: Controlleer op typfouten of onlogische wijzigingen!", e)
    except AttributeError as e:
        print("Fout: Controlleer je laatste wijzigingen m.b.t. libraries, platform etc.!", e)

def user_find(file): # gebruikersnaam controle
    user = input("Typ je gebruikersnaam in : ")
    for row in file:
        if row[0] == user:
            print("Gebruikersnaam gevonden!", user)
            user_found = [row[0],row[1]] # opslaan van de gebruikersnaam en de wachtwoord in een list
            pass_check(user_found)
            break
        else:
            print("Gebruikersnaam niet gevonden!")

def pass_check(user_found): # wachtwoord overeenkomst controle
    user = input("Typ je wachtwoord in : ")
    if user_found[1] == user:
        print("Wachtwoord gevonden!")
    else:
        print("Wachtwoord komt niet overheen!")

main()
input('Druk op ENTER om het venster te sluiten')
