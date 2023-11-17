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
	

def convertpdftxt(inpath):
    outpath = creationoutputfile(inpath)
    for filename in os.listdir(inpath):
        if ".pdf" in filename:
            outfile="./"+outpath+"/"+ filename.replace(" ","_").replace(".pdf",".txt")
            fileopen = inpath+"/"+filename
            cmd = f"pdftotext -raw -nopgbrk -enc TIS-620 {fileopen}"
            os.system(cmd)
            filesortie=fileopen.replace("pdf","txt")
            add_info(filesortie,filename,fileopen)
            cmd= f"mv {filesortie} {outpath}"
            os.system(cmd)
            
convertpdftxt(sys.argv[1])
