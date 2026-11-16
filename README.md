# Scanner de ports TCP en Python

Projet étudiant.

Le programme teste les ports d'une machine et affiche ceux qui sont ouverts, avec le nom du service associé (SSH, HTTP, HTTPS…).

## Fonctionnalités

- Scan d'une **plage de ports** (exemple : de 20 à 25)
- Scan d'une **liste de ports précis** (exemple : 22, 80, 443)
- Affichage du service des ports ouverts
- Vérification des saisies et gestion des erreurs (adresse introuvable, lettres à la place d'un port, Ctrl + C)

## Prérequis

- Python 3
- Aucune bibliothèque à installer (modules `socket` et `sys` inclus dans Python)

## Utilisation

```
python scannerport.py
```

Le programme demande ensuite :
1. l'adresse IP ou le nom de domaine de la cible ;
2. le mode : `1` pour une liste de ports, `2` pour une plage ;
3. les ports à scanner.

## Avertissement

Scanner une machine sans autorisation est interdit (article 323-1 du Code pénal).
N'utilisez ce programme que sur vos propres machines ou sur des cibles prévues pour ça, comme `scanme.nmap.org`.
