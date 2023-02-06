"""Actividad 3. Extraer palabras de archivos HTML"""
import os
import time
import re

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log3.txt", "w") as log_file:
    start_time = time.time()

    def save_words(file_name: str) -> list[str]:
        start_time_read = time.time()

        words = []

        with open(os.path.join(folder, file_name), "r") as text_file:
            content = text_file.read().lower()
            words += re.findall(r"\b[a-zA-Z]+\b", content)
        text_file.close()

        end_time_read = time.time()
        read_time = end_time_read - start_time_read
        log_file.write(
            f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

        return words

    all_words = []
    for file_name in os.listdir(folder):
        all_words += save_words(file_name)

    all_words = sorted(all_words)
    # Obtain unique words
    # all_words = sorted(set(all_words))
    with open("all_words.txt", "w") as all_words_file:
        all_words_file.write("\n".join(all_words))
    all_words_file.close()

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time
    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()
