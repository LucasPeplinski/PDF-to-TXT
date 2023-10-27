# Readme du code de conversion PDF vers texte avec informations supplémentaires

Ce script Python vise à convertir des fichiers PDF en fichiers texte tout en ajoutant des informations supplémentaires extraites des fichiers PDF d'origine. Il est conçu pour traiter un dossier contenant des fichiers PDF et produire des fichiers texte en sortie. Voici une vue d'ensemble de son fonctionnement et des outils nécessaires pour son exécution :

## Fonctionnalités du script

Le script effectue les opérations suivantes :

1. **Extraction de l'abstract et du titre** : Le script recherche des informations dans le fichier PDF d'origine, telles que l'abstract et le titre. Si ces informations sont présentes, elles sont extraites et utilisées ultérieurement.

2. **Conversion PDF en texte** : Le script utilise l'outil `pdftotext` pour convertir le contenu du fichier PDF en texte brut. Le texte résultant est sauvegardé dans un fichier texte distinct.

3. **Enrichissement du fichier texte** : Les informations extraites de l'étape 1 (titre et abstract) sont ajoutées en haut du fichier texte résultant.

4. **Structure du dossier de sortie** : Les fichiers texte sont sauvegardés dans un dossier de sortie spécifié.

## Outils nécessaires

Pour que ce script fonctionne correctement, vous devez disposer des outils suivants :

1. **Python** : Le script est écrit en Python, vous devez donc avoir Python installé sur votre système.

2. **pdftotext** : Le script utilise l'outil `pdftotext` pour convertir les fichiers PDF en texte brut. Assurez-vous d'avoir installé cet outil sur votre système.

## Comment exécuter le script

Pour exécuter le script, suivez ces étapes :

1. Assurez-vous d'avoir Python installé.

2. Assurez-vous que l'outil `pdftotext` est installé et accessible depuis la ligne de commande.

3. Placez tous les fichiers PDF que vous souhaitez convertir dans un dossier.

4. Exécutez le script Python en ligne de commande en spécifiant le chemin du dossier contenant les fichiers PDF comme argument. Par exemple : `python script.py chemin_vers_dossier_PDF`

5. Le script créera un dossier de sortie (nommé "PlainText") contenant les fichiers texte résultants avec les informations supplémentaires.

Assurez-vous que le script Python est placé dans le même répertoire que les fichiers PDF que vous souhaitez convertir, ou spécifiez le chemin complet vers le script lorsque vous l'exécutez.

**Note :** Assurez-vous d'avoir une connaissance préalable de l'installation et de l'utilisation de Python et de l'outil `pdftotext` pour exécuter ce script avec succès.
