#!/bin/bash

# Script para buscar palabras y que imprime en que archivo se encuentra y
# cuantas veces aparece

echo "Enter the word you want to search:"
read word

folder="./NewFiles"

if [ ! -d "$folder" ]; then
  echo "The directory does not exist."
  exit 1
fi

total_count=0

for file in "$folder"/*; do
  count=$(grep -i -o -w "$word" "$file" | wc -l)

  (( total_count += count ))

  if [ $count -gt 0 ]; then
    echo "$word found $count times in $file"
  fi
done

echo "$word found $total_count times in total"
