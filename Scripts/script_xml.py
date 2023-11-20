import os
import shutil
import sys
import re


def recup(filestr,strl):
	filestr=filestr.replace("\r","")
	filestr=filestr.replace(".\n\n",".\n#okfinddata#").replace("\nAcknowledgments","\n#okfinddata#").replace("\nAcknowledgements","\n#okfinddata#").replace("\nReferences","\n#okfinddata#")
	output=""
	ok =0
	for i in filestr.split("\n"):
		if ok==1 and "#okfinddata#" in i:
			break
		elif ok==1:
			output+=i+"\n"
		elif strl in i:
			ok=1
	return output

def recupcorps(filestr,deput):
	filestr = filestr.replace(deput,"##debut##").replace("Conclusion","##fin##").replace("Discussion\n","##fin##\n").replace("results\n","##fin##\n").replace("Results\n","##fin##\n")
	output=""
	ok =0
	for i in filestr.split("\n"):
		if ok==1 and "#fin#" in i:
			break
		elif ok==1:
			output+=i+"\n"
		elif "##debut##" in i:
			ok=1
	return output	
	
	

def create_xml(fichier_entree, fichier_origine):
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
	email = ""
	emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', filestr)
	for i in emails:
		email += i+" "
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

	strintroduction =""
	if "introduction" in filestr.lower():
		strintroduction += filestr.lower().split("introduction")[1].split("\n2 ")[0].replace("2. ","").replace("2 ","").replace("\r","")
		strintroduction = ' '.join(strintroduction.split("\n")[:len(strintroduction)-2])
	#Récupération de l'introduction

	strcorps = recupcorps(filestr,strintroduction[len(strintroduction)-10:])	
	#Récupération du corps

	strdiscuss =""
	if "Discussion\n" in filestr:
		strdiscuss += filestr.lower().split("discussion\n")[1].replace("conclusions\n","acknowledgments\n").replace("conclusion\n","acknowledgments\n").split("acknowledgments")[0]
		strdiscuss = '\n'.join(strdiscuss.split('\n')[:len(strdiscuss.split('\n'))-1])
	elif "results\n" in filestr.lower():
		strdiscuss += filestr.lower().split("results\n")[1].replace("conclusions\n","acknowledgments\n").replace("conclusion\n","acknowledgments\n").split("acknowledgments\n")[0]
		strdiscuss = '\n'.join(strdiscuss.split('\n')[:len(strdiscuss.split('\n'))-1])
	#Récupération de la discussion/des resultats

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
		file_out.write('    <auteur>'+author+' '+email+'</auteur>\n')
		file_out.write('	<abstract>'+strabstract+'</abstract>\n')
		file_out.write('	<introduction>'+strintroduction+'</introduction>\n')
		file_out.write('    <corps>'+strcorps+'</corps>\n')
		file_out.write('    <conclusion>'+recup(filestr,"Conclusion")+'</conclusion>\n')
		file_out.write('	<discussion>'+strdiscuss+'</discussion>\n')
		file_out.write('	<biblio>'+strbiblio+'</biblio>\n')
		file_out.write('</article>')
	#Ecriture données xml
	



fichier_entree = sys.argv[1]
fichier_origine = sys.argv[2]
create_xml(fichier_entree, fichier_origine)