#!/bin/bash

# Loop through the list of files
for file in "$@"; do
    echo "Processing $file"
    # Remove the file extension
    filename="${file%.*}"

    # Run the command for each file, replacing the output file extension
    pipenv run python main.py --text-file "$file" --format aac --output-file "${filename}.aac"
done