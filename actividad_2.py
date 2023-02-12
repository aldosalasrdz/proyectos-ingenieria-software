"""Actividad 2. Remover las etiquetas HTML"""
import os
import time
import re

folder = "Files"
new_folder = "NewFiles"
absolute_path = os.path.abspath(folder)

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

start_execution_time = time.time()

with open("log2.txt", "w") as log_file:
    start_time = time.time()

    def remove_html_tags(file_name: str) -> None:
        start_time_file = time.time()
        with open(os.path.join(folder, file_name), "rb") as html_file:
            html = html_file.read().decode("ISO-8859-1")
            # Regular expression to remove HTML tags and HTML entities.
            # More information about HTML entities:
            # https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references
            content = re.sub(r"<[^>]*>|&.*?;", "", html)
            content = content.replace("\r", "")
            content = "\n".join([line for line in content.split("\n") if line.strip()])
            new_file_name = file_name.replace(".html", ".txt")
            new_file_path = os.path.join(new_folder, new_file_name)
            with open(new_file_path, "w", encoding="utf-8") as new_file:
                new_file.write(content)
            new_file.close()
        html_file.close()
        end_time = time.time()
        read_time = end_time - start_time_file

        log_file.write(f"{os.path.join(absolute_path, file_name)}: {read_time}\n")

    for file_name in os.listdir(folder):
        remove_html_tags(file_name)
    total_time = time.time() - start_time
    total_execution_time = time.time() - start_execution_time
    log_file.write(f"\nTiempo total en abrir los archivos: {total_time}\n")
    log_file.write(f"Tiempo total de ejecucion: {total_execution_time}\n")
log_file.close()
