# ReadMe

## Introduction rapide

Les scripts fournis sont conçus pour convertir des fichiers PDF en texte brut (plaintext) ou en format XML. Le script principal est `main.py`, qui prend en charge la conversion en texte et en XML. Il utilise deux scripts auxiliaires, `script_xml.py` pour la conversion en XML et `script_plaintext.py` pour la conversion en texte brut.

## Fonctionnalités de chaque script

### main.py

- Le script principal gère la conversion des fichiers PDF en texte brut ou en XML.
- Il utilise la bibliothèque argparse pour permettre à l'utilisateur de spécifier le répertoire source et les options de conversion.
- L'utilisateur peut choisir les fichiers à convertir et spécifier s'il souhaite générer des fichiers texte ou XML. Il y a un système de choix,
s'il tape `esc` il sort du choix, `all` pour convertir tous les fichiers, et `y/n` pour convertir ce fichier ou pas.
- Les fichiers de sortie sont stockés dans un répertoire appelé "PlainText" dans le répertoire source.
- La conversion en texte brut utilise le programme externe "pdftotext" pour extraire le texte brut des fichiers PDF.
- La conversion en XML utilise également "pdftotext" pour créer un fichier HTML intermédiaire, puis applique le script `script_xml.py` pour générer le fichier XML final.

### script_xml.py

- Le script gère la conversion d'un fichier HTML (généré à partir du PDF) en un fichier XML structuré.
- Il récupère des informations telles que le titre, les auteurs, les e-mails, l'abstract, la conclusion et la bibliographie à partir du fichier HTML.
- Ces informations sont ensuite écrites dans un fichier XML structuré.

### script_plaintext.py

- Le script ajoute des informations supplémentaires au fichier texte brut généré à partir du PDF.
- Il récupère l'abstract du fichier PDF et l'ajoute au début du fichier texte brut.
- Il utilise également le programme "pdftotext" pour extraire le texte brut du PDF avec une mise en page, puis ajoute cet extrait au fichier texte brut.
- Le fichier de sortie est mis à jour avec ces informations supplémentaires.

## Outils nécessaires pour que la conversion fonctionne

- Les scripts utilisent le programme externe "pdftotext" pour extraire le texte brut des fichiers PDF.
- Les scripts Python nécessitent les bibliothèques argparse, os, shutil, sys, et re.
- Les scripts dépendent également d'autres scripts spécifiques (`script_xml.py` et `script_plaintext.py`) pour la conversion en XML et en texte brut.

Assurez-vous que ces dépendances sont satisfaites pour que les scripts fonctionnent correctement.
