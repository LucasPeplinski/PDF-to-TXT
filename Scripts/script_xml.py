import os
import shutil
import sys

def create_xml(fichier_entree, fichier_origine,pdf):
	filestr = open(fichier_entree,"r").read()	
	#Ouverture du html pdf
	
	title = ""
	if "<title>" in filestr.lower():
		title = filestr.lower().split("<title>")[1].split("</title>")[0].strip()
	#Récupération du title
	
	author = ""
	if '<meta name="Author" content="' in filestr: 
		author = filestr.split('<meta name="Author" content="')[1].split('"/>')[0].strip()
	#Récupération des auteurs
	
	cmd = f"rm {fichier_entree}"
	os.system(cmd)
	fichier_entree=fichier_entree.replace("html","txt")
	#Supression html
	
	filestr = open(fichier_entree,"r").read()	
	#Ouverture du txt pdf
	
	strabstract =""
	if "abstract" in filestr.lower():
		strabstract += filestr.lower().split("abstract")[1].split("introduction")[0].replace("1. ","").replace("1 ","").replace("\r","")
		strabstract= ' '.join(strabstract.split("\n")[:len(strabstract)-2])
	#Récupération de l'Abstract
	
	
	strbiblio =""
	if "references" in filestr.lower():
		strbiblio += filestr.lower().split("references\n")[1]
		strbiblio = '\n'.join(strbiblio.split('\n')[:len(strbiblio.split('\n'))-2])
	#Récupération de la biblio
		
	cmd = f"rm {fichier_entree}"
	os.system(cmd)
	#Supression raw text
	
	fichier_xml=fichier_entree.replace("txt","xml")
	#Création fichier final
	
	with open(fichier_xml, 'w') as file_out:
		file_out.write('<article>'+ '\n')
		file_out.write('	<preamble>'+fichier_origine[:-4]+'</preamble>\n')
		file_out.write('    <titre>'+title+ '</titre>\n')
		file_out.write('    <auteur>'+author+'</auteur>\n')
		file_out.write('	<abstract>'+strabstract+'</abstract>\n')
		file_out.write('	<biblio>'+strbiblio+'</biblio>\n')
		file_out.write('</article>')
	#Ecriture données xml
	

def convertpdfxml(inpath,outpath):
    if "PlainText" in os.listdir(inpath):
        shutil.rmtree(outpath)
    os.makedirs(outpath)
    #Création dossier
    
    for filename in os.listdir(inpath):
        if ".pdf" in filename:
            outfile="./"+outpath+"/"+ filename.replace(" ","_").replace(".pdf",".xml")
            fileopen = inpath+"/"+filename
            
            cmd = f"pdftotext -htmlmeta -nopgbrk -enc TIS-620 {fileopen}"
            os.system(cmd)
            cmd = f"pdftotext -raw -nopgbrk -enc TIS-620 {fileopen}"
            os.system(cmd)
            #Création fichier 
            
            filesortie=fileopen.replace("pdf","html")
            create_xml(filesortie,filename,fileopen)
            filesortie=fileopen.replace("pdf","xml")
            cmd= f"mv {filesortie} {outpath}"
            os.system(cmd)
            
            
if __name__ == "__main__":
	dossier_entree = sys.argv[1]
	dossier_sortie = sys.argv[1]+"/PlainText"
	convertpdfxml(dossier_entree,dossier_sortie)
