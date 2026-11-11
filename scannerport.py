import socket 

def tester_connexion(adresse_ip, port):
    Socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM )
    Socket.settimeout(0.5)
    resultat_de_connexion = Socket.connect_ex((adresse_ip, port))
    Socket.close()
    if resultat_de_connexion == 0:
        return True
    else:
        return False


def nom_service(port_test):
    if port_test == 22:
        return "SSH"
    elif port_test == 21:
        return "FTP"
    elif port_test == 80:
        return "HTTP"
    elif port_test == 443:
        return "HTTPS"
    elif port_test == 23:
        return "Telnet"
    elif port_test == 25:
        return "SMTP"
    elif port_test == 53:
        return "DNS"
    elif port_test == 3306:
        return "MySQL"

adresse_ip = input("Donne moi l'adresse IP ")
port_de_debut = int(input ("Donne moi ton port de début entre 0 et 65535 "))
port_de_fin = int(input("Donne moi ton port de fin entre 0 et 65535 "))

for port_en_test in range(port_de_debut, port_de_fin + 1):
    if tester_connexion (adresse_ip, port_en_test):
        print (f"Connexion réussi { port_en_test } { nom_service (port_en_test) } ")


