"""Actividad 7. Archivo posting"""
import os
import time
import re

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log7.txt", "w") as log_file:
    start_time = time.time()
    #Se le pasa un archivo y retorna un diccionario
    def dictionary_words(file_name: str) -> dict:
        start_time_read = time.time()
        words_dict = {}

        #Se abre el archivo que se paso
        with open(os.path.join(folder, file_name), "r") as text_file:
            #Se lee el contenido del archivo en minusculas
            content = text_file.read().lower()
            #print(content)
            #Se sacan las palabras
            words = re.findall(r"\b[a-zA-Z]+\b", content)
            #Por cada palabra
            for word in words:
                #Si la palabra ya existe dentro del diccionario
                if word in words_dict:
                    #Se le suma una repeticion
                    #print(words_dict[word])
                    words_dict[word]["RepDic"][file_name] += 1
                    #Si el archivo no esta en el arreglo dentro del diccionario de la palabra
                    if file_name not in words_dict[word]["files"]:
                        #Se agrega
                        words_dict[word]["RepDic"][file_name] = 1
                        words_dict[word]["fileCount"] += 1
                        words_dict[word]["files"].append(file_name)
                else:
                    #Se guarda la palabra en el diccionario
                    words_dict[word] = {"count": 1, "files": [file_name], "fileCount": 1, "RepDic": {file_name: 1}}
        text_file.close()

        end_time_read = time.time()
        read_time = end_time_read - start_time_read
        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

        #Se escribe el posting
        #Se abre el posting
        return words_dict

    all_words_dict = {}
    #Por cada archivo txt
    for file_name in os.listdir(folder):
        #print(file_name)
        
        #Aqui se le meten las cosas al all_words_dict
        file_words = dictionary_words(file_name)
        
        #print(file_words)
        """
        for row in file_words.items():
            with open("a.txt", "a") as a:
                a.write(str(row)+"\n")
        """    
        
        for word, count in file_words.items():
            #Si la palabra esta en el diccionario
            if word in all_words_dict:
                #El count
                #words_dict[word][file_name] += 1
                all_words_dict[word]["fileCount"] += count["count"]
                #all_words_dict[word][file_name] += 1
                
                if file_name not in all_words_dict[word]["files"]:
                    all_words_dict[word]["RepDic"][file_name] = count["RepDic"][file_name]
                    #all_words_dict[word][file_name] = file_words[word][file_name]
                    all_words_dict[word]["files"].append(file_name)
            else:
                all_words_dict[word] = count
                #print(count)
                #all_words_dict[word][file_name] = file_words[word][file_name]

    #for word in all_words_dict:
    #   print(str(all_words_dict[word])+"\n")
    #print()
    with open("posting.txt", "w") as posting_file:
            #Por cada palabra en el diccionario
            for word in all_words_dict:
                #print(all_words_dict[word])
                for file in all_words_dict[word]['files']:

                    posting_file.write(f"{file};{all_words_dict[word]['RepDic'][file]}\n")
                    #posting_file.write(f"{file};{word};{all_words_dict[word]['150.txt']}\n")

#Se escribe el dictionary
    with open("dictionary.txt", "w", encoding="utf-8") as dictionary_file:
        word_count = 0
        for word, data in all_words_dict.items():
            dictionary_file.write(f"{word};{len(data['files'])};{word_count}\n")
            word_count += len(data['files'])
    dictionary_file.close()

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()

#print(words_dict["cdt"])
"""
with open("postingPrueba.txt", "a") as posting_file:
    with open("dictionary.txt", "r") as dic:
        dicLines = dic.readlines()
        
        for line in dicLines
    for word in words_dict:
        posting_file.write(f"{file_name};{words_dict[word]['count']}\n")
"""
