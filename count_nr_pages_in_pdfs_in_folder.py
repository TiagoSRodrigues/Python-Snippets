from PyPDF2 import PdfFileReader
import os
import re
import subprocess


path = "C:\\Users\\Tiago\\Google Drive\\Tese\\Artigos\\imprimir\\"

file_list= os.listdir(path)

total=0

for file_name in file_list:
    if re.match("^.*\.pdf",file_name): 
        with open(path+file_name, "rb") as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            total+=pdf_reader.numPages
            print("{} pags no ficheiro: {}".format(pdf_reader.numPages, file_name))
print("\nTotal de {} pags".format(total))

sec = input("fechar?")
