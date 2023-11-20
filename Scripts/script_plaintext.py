import os
import shutil
import sys


def creationoutputfile(inpath):
	if "PlainText" in os.listdir(inpath):
		shutil.rmtree(inpath+"/PlainText")
	os.makedirs(inpath+"/PlainText")
	return inpath+"/PlainText"

def add_info(fichier_entree, fichier_origine,pdf):
	filestr = open(fichier_entree,"r").read()	
	#Ouverture du pdf
	
	strabstract =""
	if "abstract" in filestr.lower():
		strabstract += filestr.lower().split("abstract")[1].split("introduction")[0].replace("1. ","").replace("1 ","").replace("\r","")
		strabstract= ' '.join(strabstract.split("\n")[:len(strabstract)-2])
	#Récupération de l'Abstract
		
	cmd = f"pdftotext -layout -nopgbrk -enc TIS-620 {pdf}"
	os.system(cmd)
	#Création fichier final
	
	oldfile = open(fichier_entree, 'r').read()
	with open(fichier_entree, 'w') as file_out:
		file_out.write(fichier_origine + '\n'+strabstract + '\n'+oldfile)
	#Ecriture données supplémentaires en début de fichier
	
fichier_entree = sys.argv[1]
fichier_origine = sys.argv[2]
pdf = sys.argv[3]
add_info(fichier_entree,fichier_origine,pdf)
