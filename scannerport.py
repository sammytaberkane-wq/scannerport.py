import socket
import sys

def tester_connexion(adresse_ip, port):
    Socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM )
    Socket.settimeout(0.5)
    resultat_de_connexion = Socket.connect_ex((adresse_ip, port))
    Socket.close()
    if resultat_de_connexion == 0:
        return True
    else:
        return False


def calculer_nombre_ports(debut, fin):
    return fin - debut + 1


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
    else:
        return "Inconnu"



def est_port_valide(port):
    if port < 0 or port > 65535:
        return False
    else:
        return True


adresse_ip = input("Donne moi l'adresse IP ")
try:
    socket.gethostbyname(adresse_ip)
except socket.gaierror:
    print("Adresse IP introuvable")
    sys.exit()
choix_mode = input("Taper 1 pour choisir des ports précis, 2 pour choisir une plage de port ")
 

if choix_mode == "1":
    print("Mode liste")
    listes_ports = []
    port_a_rentrer = input("Donne moi tes différents ports à tester exemple: 22, 80, 443 : ")
    morceau_texte = port_a_rentrer.split(",")
    
    for morceau in morceau_texte:
        morceau_chiffre = int(morceau)
        listes_ports.append(morceau_chiffre)
    print(f"{listes_ports}")

    nombre_ports_trouves = 0

    for port_mode_liste in listes_ports:
        if tester_connexion(adresse_ip, port_mode_liste):
            nombre_ports_trouves += 1
            print (f"Connexion réussie { port_mode_liste } { nom_service (port_mode_liste) } ")
    if nombre_ports_trouves == 0:
        print ("Aucun port trouvé")



elif choix_mode == "2":
    port_de_debut = int(input ("Donne moi ton port de début entre 0 et 65535 "))
    while not est_port_valide(port_de_debut):
        print("Port non reconnu, recommencez")
        port_de_debut = int(input ("Donne moi ton port de début entre 0 et 65535 "))
    port_de_fin = int(input("Donne moi ton port de fin entre 0 et 65535 "))
    while not est_port_valide(port_de_fin):
        print("Port non reconnu, recommencez")
        port_de_fin = int(input("Donne moi ton port de fin entre 0 et 65535 "))
    while port_de_fin < port_de_debut:
        print("Le port de fin doit être supérieur ou égal au port de début")
        port_de_fin = int(input("Donne moi ton port de fin entre 0 et 65535 "))
    print(f"Il y a {calculer_nombre_ports (port_de_debut, port_de_fin)} ports à scanner")

    nombre_ports_trouves = 0
    for port_en_test in range(port_de_debut, port_de_fin + 1):
        if tester_connexion (adresse_ip, port_en_test):
            nombre_ports_trouves += 1
            print (f"Connexion réussi { port_en_test } { nom_service (port_en_test) } ")
    if nombre_ports_trouves == 0:
        print ("Aucun port trouvé")
else:
    print("Choix invalide")



