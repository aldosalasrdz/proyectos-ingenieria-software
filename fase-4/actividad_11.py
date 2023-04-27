"""Actividad 11. Índice de documentos"""
import time
import os

folder = "NewFiles"
absolute_path = os.path.abspath(folder)
start_time = time.time()

#Se lee posting
with open("log11.txt", "w") as log_file:
    with open("newPosting.txt", "r") as Pos:
        
        PosLines = Pos.readlines()
        Pos.close()
    
    #Se obtienen los archivos del posting
    with open("Documents.txt", "w") as Pos:
        
        dic = {}
        List = list()
        for line in PosLines:
            docNumber = line.split(".txt")
            List.append(docNumber[0])

        List = list(dict.fromkeys(List))

        indexID = 1
        
        #Se escribe archivo Documents
        for text in List:
            start_time_read = time.time()
            dic[text] = indexID
            newIndexID = str(indexID).ljust(12)
            Pos.write(f"{newIndexID}{text}.txt\n")
            indexID += 1
            end_time_read = time.time()
            read_time = end_time_read - start_time_read
            log_file.write(f"{os.path.join(absolute_path, text)}.txt: {read_time}\n")
        
        Pos.close()

    #Se actualiza el Posting
    with open("newPostingAct11.txt", "w") as PosW:
        for line in PosLines:
            docNumber = line.split(".txt")
            
            PosW.write(f"{dic[docNumber[0]]}{docNumber[1]}")
        
        PosW.close()

    total_execution_time = time.time() - start_time
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")