#!/usr/bin/env bash

# Script para ejecutar todos los archivos de python
start_time=$(date +%s.%N)

BLUE='\033[0;34m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

for file in $(find fase* -name "*.py" | sort -t_ -k2,2n); do
    printf "${BLUE}Running file: ${NC}${file}\n"
    file_start_time=$(date +%s.%N)
    python3 "$file"
    file_end_time=$(date +%s.%N)
    printf "${YELLOW}The file ${file} took $(echo "$file_end_time - $file_start_time" | bc) seconds to execute.${NC}\n\n"
done

end_time=$(date +%s.%N)
printf "${CYAN}The script took $(echo "$end_time - $start_time" | bc) seconds to execute.${NC}\n"
