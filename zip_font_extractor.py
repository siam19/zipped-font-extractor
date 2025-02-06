import os
import zipfile

def extract_fonts_from_zips():
    # Create the 'FONT FILES' directory if it doesn't exist
    font_dir = 'FONT FILES'
    os.makedirs(font_dir, exist_ok=True)
    
    # Get current working directory
    current_dir = os.getcwd()
    
    # Track font names to avoid duplicates
    extracted_fonts = set()
    
    # Iterate through all files in the current directory
    for filename in os.listdir(current_dir):
        if filename.endswith('.zip'):
            file_path = os.path.join(current_dir, filename)
            
            # Skip directories named like zip files
            if not os.path.isfile(file_path):
                continue
            
            print(f"Processing: {filename}")
            
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    # First, collect all font files in the zip
                    font_files = []
                    for member_info in zip_ref.infolist():
                        # Skip directories
                        if member_info.is_dir():
                            continue
                        
                        member_name = member_info.filename
                        base_name = os.path.basename(member_name)
                        
                        # Skip files that start with '.' (hidden/metadata files)
                        if base_name.startswith('.'):
                            print(f"  Skipping hidden file: {base_name}")
                            continue
                        
                        # Check for font file extensions (case-insensitive)
                        if member_name.lower().endswith(('.ttf', '.otf')):
                            font_files.append((base_name, member_info))
                    
                    # Process font files, prioritizing .ttf over .otf
                    for base_name, member_info in font_files:
                        # Get the font name without extension
                        font_name = os.path.splitext(base_name)[0]
                        
                        # Skip if this font has already been extracted
                        if font_name in extracted_fonts:
                            continue
                        
                        # Check if there's a .ttf version of this font
                        has_ttf = any(
                            f[0].lower().startswith(font_name.lower()) and f[0].lower().endswith('.ttf')
                            for f in font_files
                        )
                        
                        # If this is an .otf file and a .ttf version exists, skip it
                        if base_name.lower().endswith('.otf') and has_ttf:
                            print(f"  Skipping: {base_name} (preferring .ttf version)")
                            continue
                        
                        # Extract the file
                        target_path = os.path.join(font_dir, base_name)
                        with zip_ref.open(member_info) as source_file:
                            content = source_file.read()
                        with open(target_path, 'wb') as target_file:
                            target_file.write(content)
                        
                        print(f"  Extracted: {base_name}")
                        extracted_fonts.add(font_name)
            
            except zipfile.BadZipFile:
                print(f"  [!] Error: {filename} is not a valid ZIP file")
            except Exception as e:
                print(f"  [!] Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    extract_fonts_from_zips()