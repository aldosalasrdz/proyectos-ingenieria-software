#!/bin/bash

# Script para ejecutar todos los archivos de python
find fase-1 fase-2 fase-3 -name "*.py" | xargs -I{} python3 {}
