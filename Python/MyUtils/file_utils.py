import os
import shutil
import datetime
             

def generate_extension_list_txt_for_source_dir(source_dir, output_file):
    '''
    Generate a text file that lists all the extensions found in a source directory, 

    # Example usage
    source_dir = "path/to/source/directory"
    output_file = "path/to/output/file.txt"

    generate_extension_list_txt_for_source_dir(source_dir, output_file)
    
    '''
    # Set to store unique extensions
    extensions = set()

    # Iterate through all the files and subfolders in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            _, extension = os.path.splitext(file)
            extensions.add(extension)

    # Write the extensions to the output file
    with open(output_file, 'w') as f:
        for extension in extensions:
            f.write(extension + '\n')

def delete_files_with_externsion_from_list(source_dir, file_types):
    '''
    To recursively delete all files in a source directory
    that have an extension included in a list of file types 

    # Example usage

    source_dir = "path/to/source/directory"
    file_types = [".txt", ".csv", ".xlsx"]

    delete_files_with_externsion_from_list(source_dir, file_types)
    '''

    # Iterate through all the files and subfolders in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if the file extension is in the list of file types to delete
            if file_path.endswith(tuple(file_types)):
                # Delete the file
                os.remove(file_path)            


def classify_files_in_folder_YYYY_MM(source_path, destination_path):
    '''
    # Classify all files from a source path and reclusively subfolders
    move to a destination path tree with a main year folder and monthly sub folders
    
    # Example usage
    source_path = "path/to/source/folder"
    destination_path = "path/to/destination/folder"

    classify_files(source_path, destination_path)

    '''
    # Iterate through all the files and subfolders in the source path
    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Get the creation date of the file
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.datetime.fromtimestamp(creation_time)
            
            # Create the destination path based on the year and month of creation
            year_folder = str(creation_date.year)
            month_folder = creation_date.strftime("%B")
            destination_folder = os.path.join(destination_path, year_folder, month_folder)
            
            # Create the destination folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)
            
            # Move the file to the destination folder
            shutil.move(file_path, destination_folder)

