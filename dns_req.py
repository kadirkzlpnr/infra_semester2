#import van benodigde libraries voor de data m.b.t. de domain
import socket
import whois 

try:
    dom = input("Voer een domain in : ")

    res = whois.whois(dom)

    print("ip_adress :", socket.gethostbyname(dom))
#type data m.b.t. de domain
    for x in res.status:
        print("status : ", x) 

    for x in res.creation_date:
        print("creation_date : ", x)

    for x in res.updated_date:
        print("updated_date : ", x)

    for x in res.expiration_date:
        print("expiration_date : ", x)

    for x in res.emails:
        print("email : ", x)

    for x in res.name_servers:
        print("name_server : ", xff)
#error handling
except TypeError as e:
    print("Controlleer of je de juiste functie naam hebt gebruikt!", e)
    
except socket.gaierror as e: 
    print("Fout: Typ een geldige domain-naam in inclusief .com, .net etc.!", e)

except NameError as e:
    print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)

except SyntaxError as e:
    print("Fout: Controlleer op typfouten of onlogische wijzigingen!", e)

except AttributeError as e:
    print("Fout: Controlleer je laatste wijzigingen m.b.t. libraries etc.!", e)
 
input('Druk op ENTER om het venster te sluiten')

