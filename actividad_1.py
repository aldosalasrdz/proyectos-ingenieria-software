import os
import time

folder = "Files"

absolute_path = os.path.abspath(folder)

start_execution_time = time.time()

with open("log.txt", "w") as log_file:
    start_time = time.time()
    def open_file(file_name):
        start_time_file = time.time()
        with open(os.path.join(folder, file_name), "rb") as html_file:
            html_file.read()
        end_time = time.time()
        read_time = end_time - start_time_file

        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")
        
    for file_name in os.listdir(folder):
        open_file(file_name)
    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time
    log_file.write(f"Tiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()
