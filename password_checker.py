import csv

def main():
    with open("users.txt","r") as file: # lezen van de .txt file met de users data
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    user = input("Typ je gebruikersnaam in : ")
    for row in file:
        if row[0] == user:
            print("Gebruikersnaam gevonden!", user)
            user_found = [row[0],row[1]] # opslaan van de gebruikersnaam en de wachtwoord in een list
            pass_check(user_found)
            break
        else:
            print("Gebruikersnaam niet gevonden!")

def pass_check(user_found): # wachtwoord check als de gebruikersnaam terug komt in de .txt file
    user = input("Typ je wachtwoord in : ")
    if user_found[1] == user:
        print("Wachtwoord gevonden!")
    else:
        print("Wachtwoord komt niet overheen!")

main()