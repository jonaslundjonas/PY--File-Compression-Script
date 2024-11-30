'''
File Compression Script
Written by Jonas Lund 2024

Description:
    This script compresses all files in the current folder into a zip file,
    excluding the script itself. The user will be prompted to enter a name
    for the zip file.

Setup:
    1. Place this script in the folder containing the files you want to compress
    2. Make sure you have Python installed on your system

How to run:
    1. Open a terminal/command prompt
    2. Navigate to the folder containing this script
    3. Run the script using: python script_name.py
    4. Enter a name for the zip file when prompted (don't include .zip extension)

What to expect:
    - The script will create a zip file with your chosen name
    - It will show progress as each file is added to the archive
    - At the end, it will display the total number of files compressed
    - The script itself will not be included in the zip file
'''

import os
import zipfile
from datetime import datetime

def zip_folder_contents(folder_path='.'):
    # Get the script filename
    script_name = os.path.basename(__file__)
    
    # Ask user for zip file name
    while True:
        zip_name = input("Enter name for the zip file (without .zip extension): ").strip()
        if zip_name:
            zip_filename = f'{zip_name}.zip'
            # Check if file already exists
            if os.path.exists(zip_filename):
                overwrite = input("File already exists. Overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    continue
            break
        else:
            print("Please enter a valid name")
    
    # Get all files in the folder
    files_to_zip = [f for f in os.listdir(folder_path) 
                    if os.path.isfile(os.path.join(folder_path, f))
                    and f != script_name  # Exclude the script itself
                    and f != zip_filename]  # Exclude the zip file being created
    
    if not files_to_zip:
        print("No files found to zip!")
        return
    
    try:
        # Create the zip file
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            print("\nStarting compression...")
            for file in files_to_zip:
                print(f"Adding {file} to archive...")
                zipf.write(file)
        
        print(f"\nArchive created successfully: {zip_filename}")
        print(f"Files compressed: {len(files_to_zip)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("=== File Compression Script ===")
    zip_folder_contents()
    input("\nPress Enter to exit...")
