"""Actividad 9. Stop List"""
import PyPDF2
import time

#Inicio de tiempo de ejecucion
start_execution_time = time.time()
#Se abre el log de la act8
with open("log9.txt", "w") as log_file:
    log_file.write("#Punto 3:\n")
    start_Punto3_time = time.time()
    #Punto 3. Leer el pdf
    #Metodo para saber si en el diccionario existe una palabra como llave
    def existsDic(word, Dic):
        if Dic.get(word) is not None:
            return True
        else:
            return False

    #Se abre el archivo stopList
    with open("stopList.txt", "w") as stopListFile:

        #Se lee el pdf
        file = open("Actividad9_stoplist.pdf", "rb")
        readPDF = PyPDF2.PdfReader(file)

        #Se extrae el texto del pdf y se excribe en stopList.txt
        for i in range(0,11):
            page = readPDF._get_page(i)
            stopListFile.write(page.extract_text())
        stopListFile.close()

    #Se crea el nuevo diccionario
    newDic = {}

    #Se lee el archivo del diccionario
    with open("dictionary.txt", "r") as dictionary:
        
        #Se lee por lineas
        Lines = dictionary.readlines()
        
        #Por cada linea se agrega al nuevo diccionario
        for line in Lines:
            line = line[:-1]
            #Se divide la linea por ;
            row = line.split(";")
            #Se agrega la palabra + rep + pos al diccionario nuevo
            newDic[row[0]] = {"Rep": row[1], "Pos": row[2]}

    #Se leen las lineas de StopList
    stopList = open('stopList.txt', 'r')
    stopLines = stopList.readlines()

    #Punto 3: Eliminar las palabras dentro de stopList
    for line in stopLines:
        start_SL_time = time.time()
        #Se limpia la palabra para que no tenga saltos de linea ni espacios
        word = line.split()[0]
        #Si la palabra de stopList existe en el diccionario se elimina
        if existsDic(word, newDic):
            del newDic[word]
        end_SL_time = time.time()
        log_file.write("Palabra: "+word+"\t"+str(end_SL_time-start_SL_time)+"\n")
    end_Punto3_time = time.time()
    log_file.write("Tiempo de Ejecucion punto 3:\t"+str(end_Punto3_time-start_Punto3_time)+"\n")

    #Punto 4.a: Eliminar tokens con repeticiones bajas
    #Punto 4.b: Eliminar tokens con 1 solo caracter
    log_file.write("\n#Punto 4:\n")
    start_Punto4_time = time.time()
    #Se guardan las palabras del diccionario en una lista
    wordList = []
    for element in newDic:
        wordList.append(element)

    #Se elimina del diccionario las palabras de 1 caracter y las que se repiten menos de 3 veces
    for element in wordList:
        start_ND_time = time.time()
        if len(element) == 1 or int(newDic[element]["Rep"]) <= 3:
            del newDic[element]
        end_ND_time = time.time()
        log_file.write("Palabra: "+element+"\t"+str(end_ND_time-start_ND_time)+"\n")
    
    with open("newDictionary.txt", "w") as NewDictionary:
        for element in newDic:
            NewDictionary.write(element+";"+newDic[element]["Rep"]+";"+newDic[element]["Pos"]+"\n")
    
    end_Punto4_time = time.time()
    log_file.write("\nTiempo de Ejecucion punto 4:\t"+str(end_Punto4_time-start_Punto4_time)+"\n")
    end_execution_time = time.time()
    log_file.write("\nTiempo de Ejecucion Total:\t"+str(end_execution_time-start_execution_time))
log_file.close()