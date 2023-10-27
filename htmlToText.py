import os
import shutil
import sys

def add_info(fichier_entree, fichier_origine,pdf):
    filestr = open(fichier_entree,"r").read()
    strabstract =""
    if "abstract" in filestr.lower():
        strabstract += filestr.lower().split("abstract")[1].split("introduction")[0].replace("1. ","").replace("1 ","").replace("\r","")
        strabstract= ' '.join(strabstract.split("\n")[:len(strabstract)-2])
    title = ""
    if "<title>" in filestr.lower():
        title = filestr.lower().split("<title>")[1].split("</title>")[0]
    os.remove(fichier_entree)
    cmd = f"pdftotext -layout -nopgbrk -enc TIS-620 {pdf}"
    fichier_entree=fichier_entree.replace("html","txt")
    os.system(cmd)
    oldfile = open(fichier_entree, 'r').read()
    with open(fichier_entree, 'w') as file_out:
        file_out.write(fichier_origine + '\n')
        file_out.write(title + '\n')
        file_out.write(strabstract + '\n')
        file_out.write(oldfile)
    

def convertpdftxt(inpath,outpath):
    print(os.listdir(inpath))
    if "PlainText" in os.listdir(inpath):
        shutil.rmtree(outpath)
    os.makedirs(outpath)
    for filename in os.listdir(inpath):
        if ".pdf" in filename:
            outfile="./"+outpath+"/"+ filename.replace(" ","_").replace(".pdf",".txt")
            fileopen = inpath+"/"+filename
            cmd = f"pdftotext -htmlmeta -nopgbrk -enc TIS-620 {fileopen}"
            os.system(cmd)
            filesortie=fileopen.replace("pdf","html")
            add_info(filesortie,filename,fileopen)
            filesortie=fileopen.replace("pdf","txt")
            cmd= f"mv {filesortie} {outpath}"
            os.system(cmd)
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Spécifiez le dossier contenant les pdf")
    else:
        dossier_entree = sys.argv[1]
        dossier_sortie = sys.argv[1]+"/PlainText"
        convertpdftxt(dossier_entree,dossier_sortie)