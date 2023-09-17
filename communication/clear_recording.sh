#!/bin/bash

# Define the path to the recordings folder
recordings_folder="recordings"

# Check if the folder exists
if [ -d "$recordings_folder" ]; then
    # Remove all files and subdirectories within the folder
    find "$recordings_folder" -mindepth 1 -delete
    echo "All contents of $recordings_folder have been deleted."
else
    echo "$recordings_folder does not exist or is not a directory."
fi
