import argparse
import os
import sys
import shutil


def creationoutputfile(inpath):
	if "PlainText" in os.listdir(inpath):
		shutil.rmtree(inpath+"/PlainText")
	os.makedirs(inpath+"/PlainText")
	return inpath+"/PlainText"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PDF to text or XML')
    parser.add_argument('directory', help='The directory containing the PDF files.')
    parser.add_argument('-t', '--text', help='Generate text output.', action='store_true')
    parser.add_argument('-x', '--xml', help='Generate XML output.', action='store_true')

    args = parser.parse_args()
    inpath = args.directory
    outpath = creationoutputfile(inpath)
    choosefile=[]
    print("Merci de choisir les fichiers que vous voulez convertir. taper \"esc\" à tout moment pour arreter le choix et y/n pour choisir all pour tout choisir")
    for filename in os.listdir(inpath):
         if ".pdf" in filename:
            choix = input("Voulez-vous convertir le fichier "+filename.strip()+": ")
            if choix=="y":
                choosefile.append(filename)
            elif choix=="n":
                continue
            elif choix=="esc":
                break
            elif choix=="all":
                choosefile=os.listdir(inpath)
                break
            else:
                print("Choix non reconnu next")
            
    if args.text:
        for filename in choosefile:
            if ".pdf" in filename:
                outfile="./"+outpath+"/"+ filename.replace(" ","_").replace(".pdf",".txt")
                fileopen = inpath+"/"+filename
                cmd = f"pdftotext -raw -nopgbrk -enc TIS-620 {fileopen}"
                os.system(cmd)
                filesortie=fileopen.replace("pdf","txt")
                os.system("python3 ./Scripts/script_plaintext.py " + filesortie+" "+filename+" "+fileopen)
                cmd= f"mv {filesortie} {outpath}"
                os.system(cmd)

    if args.xml:
        for filename in choosefile:
            if ".pdf" in filename:
                outfile="./"+outpath+"/"+ filename.replace(" ","_").replace(".pdf",".xml")
                fileopen = inpath+"/"+filename
                
                cmd = f"pdftotext -htmlmeta -nopgbrk -enc TIS-620 {fileopen}"
                os.system(cmd)
                cmd = f"pdftotext -raw -nopgbrk -enc TIS-620 {fileopen}"
                os.system(cmd)
                #Création fichier 
                
                filesortie=fileopen.replace("pdf","html")
                os.system("python3 ./Scripts/script_xml.py " + filesortie+" "+filename)
                filesortie=fileopen.replace("pdf","xml")
                cmd= f"mv {filesortie} {outpath}"
                os.system(cmd)
