"""Actividad 6. Sumar la misma palabra por archivos"""
import os
import time
import re

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log6.txt", "w") as log_file:
    start_time = time.time()

    def tokenize_words(file_name: str) -> dict:
        start_time_read = time.time()

        words_dict = {}

        with open(os.path.join(folder, file_name), "r") as text_file:
            content = text_file.read().lower()
            words = re.findall(r"\b[a-zA-Z]+\b", content)
            for word in words:
                if word in words_dict:
                    words_dict[word]["count"] += 1
                    if file_name not in words_dict[word]["files"]:
                        words_dict[word]["files"].append(file_name)
                else:
                    words_dict[word] = {"count": 1, "files": [file_name]}
        text_file.close()

        end_time_read = time.time()
        read_time = end_time_read - start_time_read
        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

        return words_dict

    all_words_dict = {}
    for file_name in os.listdir(folder):
        file_words = tokenize_words(file_name)
        for word, count in file_words.items():
            if word in all_words_dict:
                all_words_dict[word]["count"] += count["count"]
                if file_name not in all_words_dict[word]["files"]:
                    all_words_dict[word]["files"].append(file_name)
            else:
                all_words_dict[word] = count

    with open("tokenized.txt", "w", encoding="utf-8") as tokenized_words_file:
        for word, data in all_words_dict.items():
            tokenized_words_file.write(f"{word};{data['count']};{len(data['files'])}\n")
    tokenized_words_file.close()

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()
