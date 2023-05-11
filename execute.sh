#!/usr/bin/env bash

# Script para ejecutar todos los archivos de python
start_time=$(date +%s.%N)

BLUE='\033[0;34m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

for dir in fase-{1..4}; do
  for file in $(find $dir -name "*.py" | sort -t_ -k2,2n); do
      printf "${BLUE}Running file: ${NC}${file}\n"

      if [[ "$file" == "fase-4/actividad_12.py" || "$file" == "fase-4/actividad_13.py" ]]; then
        read -p "Enter a word input: " word_input
        file_start_time=$(date +%s.%N)

        python3 "$file" "$word_input"

        file_end_time=$(date +%s.%N)
        printf "${YELLOW}The file ${file} took %.2f seconds to execute.${NC}\n\n" $(echo "$file_end_time - $file_start_time" | bc)
      else
        file_start_time=$(date +%s.%N)

        python3 "$file"

        file_end_time=$(date +%s.%N)
        printf "${YELLOW}The file ${file} took %.2f seconds to execute.${NC}\n\n" $(echo "$file_end_time - $file_start_time" | bc)
      fi
  done
done

end_time=$(date +%s.%N)

printf "${CYAN}The script took %.2f seconds to execute.${NC}\n" $(echo "$end_time - $start_time" | bc)
