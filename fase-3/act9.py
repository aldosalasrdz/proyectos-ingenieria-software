"""Actividad 9. Stop List"""
import PyPDF2
import time
import os
import re
from hash_table import HashTable

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

Dic = {}
stopDic = {}

# Se lee el dictionary.txt
with open("dictionary.txt", "r") as dic:
    dicLines = dic.readlines()

    for line in dicLines:
        word = line.split(";")[0]
        rep = line.split(";")[1]
        pos = line.split(";")[2]

        Dic[word] = {"Rep": rep, "Pos": pos}

    dic.close()

# Se lee el stopList
with open("Actividad9_stoplist.pdf", "rb") as stoplist_file:
    reader = PyPDF2.PdfReader(stoplist_file)
    stoplist = ""

    for page in reader.pages:
        stoplist += page.extract_text()

    # Remove everything but the words
    stoplist = set(re.findall(r"(?!.*TecMilenio).*\b[a-zA-Z]+\b", stoplist))

    # Remove white spaces in each word
    stoplist = [word.strip() for word in stoplist]

    with open("stoplist.txt", "w") as stoplist_file:
        stoplist_file.write("\n".join(sorted(stoplist)))
        stoplist_file.close()

# Se guardan las palabras del stop lost en un dictionary
with open("stoplist.txt", "r") as stopFile:
    sT = stopFile.readlines()

    for word in sT:
        stopDic[word[:-1]] = {}

    stopFile.close()

# Si el diccionario stoplist tiene la current palabra o tiene frecuencua <= 3 o es de 1 caracter -> no se escribe en el nuevo diccionario
with open("newDictionary.txt", "w") as newDic:
    for word in Dic:
        if word in stopDic or int(Dic[word]["Rep"]) <= 3 or len(word) == 1:
            # print(word)
            continue
        newDic.write(f"{word};{Dic[word]['Rep']};{Dic[word]['Pos']}")
