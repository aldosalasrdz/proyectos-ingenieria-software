"""Actividad 10. Weight tokens"""
import time
import os

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log10.txt", "w") as log_file:
    start_time = time.time()

    MAX_FILE_NAME_LENGTH = 10

    with open("newDictionary.txt", "r") as dictionary_file:
        start_time_read = time.time()
        dictionary_file_lines = dictionary_file.readlines()
        total_word_count = len(dictionary_file_lines)

    with open("posting.txt", "r") as posting_file:
        posting_file_lines = posting_file.readlines()

        with open("newPosting.txt", "w") as new_posting_file:
            for line in posting_file_lines:
                count = int(line.split(";")[1])
                file_name = line.split(";")[0]
                weight = round((count * 100) / total_word_count, 3)

                file_name_str = str(file_name).ljust(MAX_FILE_NAME_LENGTH + 2)
                new_posting_file.write(f"{file_name_str}{weight}\n")

                end_time_read = time.time()
                read_time = end_time_read - start_time_read
                log_file.write(
                    f"{os.path.join(absolute_path, file_name)}: {read_time}\n"
                )

    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time

    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
