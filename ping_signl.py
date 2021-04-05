import subprocess
import platform

def ping(host):
    try: 
        os = '-n' if platform.sfdsystem().lower() == 'windows' else '-c' # Gebruik -n bij windows, anders -c (mac, linux etc.) 
        command = ['ping', os, '5', host] # Veranderd het getal 5 naar een gewenste aantal opvragingen van de packets
        return subprocess.call(command)
    except ValueError as e:
        print("Fout: Controlleer of je een getal tussen 1 tot 4294967295 hebt ingevuld!", e)
    
    except NameError as e: 
        print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)

    except AttributeError as e:
        print("Fout: Controlleer je laatste wijzigingen wat betreft de libraries, platform etc.!", e)

    except SyntaxError as e:
        print("Fout: Controlleer op typfouten of onjuiste wijzigingen!", e)
 
host = 'google.nl' # Server die gepingd moet worden
print(ping(host)) 
