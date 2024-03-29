"""Actividad 8. Hash table"""
import os
import time
import re
from hash_table import HashTable

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log8.txt", "w") as log_file:
    start_time = time.time()

    hash_table = HashTable(250_000)

    file_count = {}

    def hash_table_words(file_name: str):
        start_time_read = time.time()

        with open(os.path.join(folder, file_name), "r") as text_file:
            content = text_file.read().lower()
            words = set(re.findall(r"\b[a-zA-Z]+\b", content))

            for word in words:
                hash_table.add(word, 1)

                if word not in file_count:
                    file_count[word] = set()

                file_count[word].add(file_name)

        text_file.close()

        end_time_read = time.time()
        read_time = end_time_read - start_time_read
        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

    for file_name in os.listdir(folder):
        hash_table_words(file_name)

    MAX_WORD_LENGTH = 60
    MAX_COUNT_LENGTH = 5

    with open("hashtable.txt", "w", encoding="utf-8") as hash_table_file:
        word_count = 0
        for i in range(len(hash_table.table)):
            if not hash_table.table[i]:
                hash_table_file.write("0\n")
            else:
                for word, count in hash_table.table[i]:
                    word_count_str = str(word_count)
                    count_str = str(len(file_count[word])).ljust(MAX_COUNT_LENGTH + 2)
                    word_str = str(word).ljust(MAX_WORD_LENGTH + 2)
                    hash_table_file.write(f"{word_str}{count_str}{word_count_str}\n")
                    word_count += count

        hash_table_file.write(
            f"\nNumero total de colisiones: {hash_table.count_collisions()}"
        )

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
