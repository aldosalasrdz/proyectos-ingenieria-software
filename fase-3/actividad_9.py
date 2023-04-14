"""Actividad 9. Stop List"""
import PyPDF2
import time
import os
from hash_table import HashTable

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()
with open("log9.txt", "w") as log_file:
    start_punto3_time = time.time()
    hash_table = HashTable(20)

    def exists_dict(word, dict):
        return dict.get(word) is not None

    with open("stop_list.txt", "w") as stop_list_file:
        file = open("Actividad9_stoplist.pdf", "rb")
        readPDF = PyPDF2.PdfReader(file)

        for i in range(0, 11):
            page = readPDF._get_page(i)
            stop_list_file.write(page.extract_text())
        stop_list_file.close()

    new_dict = {}

    with open("dictionary.txt", "r") as dictionary:
        lines = dictionary.readlines()

        for line in lines:
            line = line[:-1]
            row = line.split(";")
            new_dict[row[0]] = {"Rep": row[1], "Pos": row[2]}

    stop_list = open("stop_list.txt", "r")
    stop_lines = stop_list.readlines()

    for line in stop_lines:
        start_sl_time = time.time()
        word = line.split()[0]
        if exists_dict(word, new_dict):
            del new_dict[word]
        end_sl_time = time.time()
        log_file.write(f"Palabra: {word}\t{end_sl_time - start_sl_time}\n")
    end_punto3_time = time.time()
    log_file.write(
        f"Tiempo de ejecución punto 3:\t{end_punto3_time - start_punto3_time}\n"
    )

    start_punto4_time = time.time()
    wordList = []
    for element in new_dict:
        wordList.append(element)

    for element in wordList:
        start_nd_time = time.time()
        if len(element) == 1 or int(new_dict[element]["Rep"]) <= 3:
            del new_dict[element]
        end_ND_time = time.time()
        log_file.write(f"Palabra: {element}\t{end_ND_time - start_nd_time}\n")
    end_punto4_time = time.time()
    log_file.write(
        f"\nTiempo de ejecución punto 4:\t{end_punto4_time - start_punto4_time}\n"
    )
    start_punto5_time = time.time()

    def hash_table_words():
        for word in new_dict:
            hash_table.add(word, 1)

    hash_table_words()

    word_count = 0
    with open("newHashTable.txt", "w", encoding="utf-8") as hash_table_file:
        for i in range(len(hash_table.table)):
            if not hash_table.table[i]:
                hash_table_file.write("0\n")
            else:
                for word, count in hash_table.table[i]:
                    hash_table_file.write(
                        f"{word}{' ' * (8 - len(word))}\t{count}\t\t{word_count}\n"
                    )
                    word_count += count
        hash_table_file.write(
            f"\nNumero total de colisiones: {hash_table.count_collisions()}\n"
        )

    with open("newDictionary.txt", "w") as NewDictionary:
        for element in new_dict:
            NewDictionary.write(
                f"{element};{new_dict[element]['Rep']};{new_dict[element]['Pos']}\n"
            )

    end_punto5_time = time.time()
    log_file.write(
        f"\nTiempo de ejecución punto 5:\t{end_punto5_time - start_punto5_time}\n"
    )
    end_execution_time = time.time()
    log_file.write(
        f"\nTiempo de ejecución total:\t{end_execution_time - start_execution_time}"
    )
log_file.close()
