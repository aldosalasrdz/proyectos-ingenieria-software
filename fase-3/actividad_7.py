"""Actividad 7. Archivo posting"""
import os
import time
import re

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log7.txt", "w") as log_file:
    start_time = time.time()

    def dictionary_words(file_name: str) -> dict:
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

        with open("posting.txt", "a") as posting_file:
            for word in words_dict:
                posting_file.write(f"{file_name};{words_dict[word]['count']}\n")
        return words_dict

    all_words_dict = {}
    for file_name in os.listdir(folder):
        file_words = dictionary_words(file_name)
        for word, count in file_words.items():
            if word in all_words_dict:
                all_words_dict[word]["count"] += count["count"]
                if file_name not in all_words_dict[word]["files"]:
                    all_words_dict[word]["files"].append(file_name)
            else:
                all_words_dict[word] = count

    with open("dictionary.txt", "w", encoding="utf-8") as dictionary_file:
        word_count = 0
        for word, data in all_words_dict.items():
            dictionary_file.write(f"{word};{len(data['files'])};{word_count}\n")
            word_count += data["count"]
    dictionary_file.close()

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()
