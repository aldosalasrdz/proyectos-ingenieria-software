"""Actividad 5. Exclusión de palabras duplicadas"""
import os
import time
import re

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log5.txt", "w") as log_file:
    start_time = time.time()

    def save_unique_words(file_name: str) -> dict:
        start_time_read = time.time()

        words_dict = {}

        with open(os.path.join(folder, file_name), "r") as text_file:
            content = text_file.read().lower()
            words = re.findall(r"\b[a-zA-Z]+\b", content)
            for word in words:
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
        text_file.close()

        end_time_read = time.time()
        read_time = end_time_read - start_time_read
        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

        return words_dict

    all_words_dict = {}
    for file_name in os.listdir(folder):
        file_words = save_unique_words(file_name)
        for word, count in file_words.items():
            if word in all_words_dict:
                all_words_dict[word] += count
            else:
                all_words_dict[word] = count

    with open("unique_words.txt", "w", encoding="utf-8") as unique_words_file:
        for word, count in sorted(all_words_dict.items()):
            unique_words_file.write(f"{word} {count}\n")
    unique_words_file.close()

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()
