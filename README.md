# Zipped Font Files Extractor

This Python script is designed to extract `.ttf` and `.otf` font files from ZIP archives in the current directory. It organizes the extracted fonts into a dedicated folder.


## Usage

1. Place the script (`zip_font_extractor.py`) in the directory containing your ZIP files.
2. Run the script using Python:

   ```bash
   python zip_font_extractor.py


## Features

- **Extracts Fonts**: Extracts `.ttf` and `.otf` files from ZIP archives.
- **Prioritizes `.ttf` Files**: If both `.ttf` and `.otf` versions of a font exist, only the `.ttf` file is extracted.
- **Skips Hidden Files**: Ignores files that start with `.` (e.g., `._font-italic.ttf`), which are often metadata or hidden files.
- **Organizes Output**: Creates a `FONT FILES` directory to store all extracted fonts.
- **Handles Errors**: Gracefully handles corrupt ZIP files and other errors.



## Requirements

- Python 3.x
- No additional libraries are required (uses built-in `os` and `zipfile` modules).

