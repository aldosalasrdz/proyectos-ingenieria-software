"""Actividad 9. Stop List"""
import PyPDF2
import time
import os
import re
from hash_table import HashTable

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log9.txt", "w") as log_file:
    start_time = time.time()

    hash_table = HashTable(50_000)

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

    def stop_list_words(file_name: str):
        start_time_read = time.time()

        with open(os.path.join(folder, file_name), "r") as text_file:
            content = text_file.read().lower()
            words = re.findall(r"\b[a-zA-Z]+\b", content)

            # Remove stoplist words
            words = [word for word in words if word not in stoplist]

            for word in words:
                hash_table.add(word, 1)

        text_file.close()

        end_time_read = time.time()
        read_time = end_time_read - start_time_read
        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

    for file_name in os.listdir(folder):
        stop_list_words(file_name)

    # Remove words that appear less than 3 times
    for i in range(len(hash_table.table)):
        if hash_table.table[i]:
            hash_table.table[i] = [
                (word, count) for word, count in hash_table.table[i] if count >= 3
            ]

    # Remove words of length 1
    for i in range(len(hash_table.table)):
        if hash_table.table[i]:
            hash_table.table[i] = [
                (word, count) for word, count in hash_table.table[i] if len(word) > 1
            ]

    MAX_WORD_LENGTH = 26
    MAX_COUNT_LENGTH = 5

    with open("newHashTable.txt", "w", encoding="utf-8") as hash_table_file:
        hash_word_count = 0
        for i in range(len(hash_table.table)):
            if not hash_table.table[i]:
                hash_table_file.write("0\n")
            else:
                for word, count in hash_table.table[i]:
                    word_count_str = str(hash_word_count)
                    count_str = str(count).ljust(MAX_COUNT_LENGTH + 2)
                    word_str = str(word).ljust(MAX_WORD_LENGTH + 2)
                    hash_table_file.write(f"{word_str}{count_str}{word_count_str}\n")
                    hash_word_count += count
        hash_table_file.write(
            f"\nNumero total de colisiones: {hash_table.count_collisions()}"
        )

    with open("newDictionary.txt", "w", encoding="utf-8") as new_dictionary_file:
        dict_word_count = 0
        for i in range(len(hash_table.table)):
            if hash_table.table[i]:
                for j, (word, count) in enumerate(hash_table.table[i]):
                    new_dictionary_file.write(f"{word};{count};{dict_word_count}\n")
                    dict_word_count += count

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
