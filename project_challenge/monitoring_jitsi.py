# benodigde libraries 
import requests
import os
import configparser
from vmwc import VMWareClient
import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# config file
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

# online/offline status
def status():
    try:
        url = (config['HOST'].get('url'))
        r = requests.post(url)

# zodra offline voer de volgende taken uit
        if r.status_code != 200:
            print('Je server is Offline gepingd!')
            res_gebruik()
            meld_admin()
            start()
        else:
            print("Je server is Online gepingd!")

    except KeyError as e:
        print("Fout: Er is een probleem ontstaan wat betreft de config.ini file! Controleer de file op de juiste KEY benoemingen etc.!", e)
    except requests.exceptions.MissingSchema as e:
        print("Fout: Typ een geldige domain-naam in inclusief .com, .net etc.!", e)
    except NameError as e:
        print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)
    except Exception:
        print('Je server is Offline gepingd!')
        res_gebruik()
        meld_admin()
        start()

# resourse usage script opvragen
def res_gebruik():
    os.system('python gebruik_datacenter.py')   

# beheerder informeren zodra server offline wordt gepingd            
def meld_admin():
    try:
        email_user = (config['EMAIL'].get('email_user'))
        email_password = (config['EMAIL'].get('email_password'))
        email_send = (config['EMAIL'].get('email_user'))

        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Jitsi server is offline'] = subject

        body = 'Je server is Offline gepingd! \nJe server wordt automatisch opnieuw opgestart! \n\n Het gebruik van de resources van de datacenters:'
        msg.attach(MIMEText(body,'plain'))

        filename='gebruik.txt'
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)

        server.sendmail(email_user,email_send,text)
        server.quit()
        print("Email wordt verzonden...")
        
    except smtplib.SMTPAuthenticationError as e:
        print("Fout: Controlleer of je de juiste email en wachtwoord hebt ingevoerd!", e)
    except NameError as e:
        print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)

#rebooten zodra offline
def start():
    try:
        host = (config['NETLAB'].get('host'))
        username = (config['NETLAB'].get('username'))
        password = (config['NETLAB'].get('password'))
        with VMWareClient(host, username, password) as client:
            for vm in client.get_virtual_machines():
                print('Rebooting "{}" ...'.format(vm.name))
                vm.reboot()
            
    except NameError as e:
        print("Fout: Controlleer of je de juiste functie naam hebt gebruikt!", e)
    except TimeoutError as e:
        print("Fout: Controlleer je verbinding met de Cisco VPN en je inloggegevens van Vcenter!", e)
    except Exception:
        pass

if __name__ == "__main__":
    status()
