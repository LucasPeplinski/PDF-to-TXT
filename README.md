# ReadMe

## Introduction rapide

Ce jeu de scripts Python est conçu pour convertir des fichiers PDF en texte brut (`.txt`) ou en format XML (`.xml`). Il offre deux scripts principaux, `script_txt.py` et `script_xml.py`, chacun avec des fonctionnalités spécifiques. Le script `main.py` sert de point d'entrée pour l'exécution des scripts en fonction des options choisies.

## Fonctionnalités de chaque script

### script_txt.py

Ce script prend en entrée un répertoire contenant des fichiers PDF et les convertit en fichiers texte brut (`.txt`). Il extrait également les résumés des articles, s'il y en a, et les ajoute au début de chaque fichier texte. Les étapes comprennent :

1. **Extraction du texte brut du PDF** : Utilisation de la commande `pdftotext` pour extraire le texte brut du PDF.
2. **Récupération de l'abstract** : Recherche du terme "abstract" dans le texte pour extraire la section abstract.
3. **Création du fichier final** : Ajout des informations extraites au début du fichier texte.

### script_xml.py

Ce script réalise une tâche similaire à `script_txt.py`, mais génère des fichiers au format XML (`.xml`). Les principales étapes incluent :

1. **Extraction du texte brut du PDF** : Utilisation de la commande `pdftotext` pour extraire le texte brut du PDF.
2. **Récupération de l'abstract** : Recherche du terme "abstract" dans le texte pour extraire la section abstract.
3. **Création du fichier XML** : Création d'un fichier XML avec des balises telles que `<article>`, `<preamble>`, et `<abstract>`. Les informations extraites sont insérées dans ces balises.

### main.py

Ce script est un point d'entrée permettant à l'utilisateur de choisir entre la conversion en texte brut (`-t` ou `--text`) ou en XML (`-x` ou `--xml`). Il utilise les arguments de ligne de commande pour appeler le script approprié avec le répertoire en tant qu'argument.

## Outils nécessaires

- Python 3
- `pdftotext` (un outil en ligne de commande pour extraire du texte à partir de fichiers PDF)
- Les bibliothèques Python standard (`os`, `shutil`, `sys`, `argparse`)

## Comment exécuter le script

1. Assurez-vous que Python 3 est installé sur votre système.
2. Installez l'outil `pdftotext` en suivant les instructions spécifiques à votre système d'exploitation.
3. Exécutez le script principal `main.py` avec le répertoire contenant les fichiers PDF en tant qu'argument. Utilisez les options `-t` ou `-x` pour spécifier le type de conversion.

   Exemple :

## Conversion en text

   ```bash
   python3 main.py -t repertoire
   ```

## Conversion en xml

```bash
   python3 main.py -x repertoire
   ```
