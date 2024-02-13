import os
import shutil
import datetime
import random
             

def generate_extension_list_txt_for_source_path(source_path, output_file):
    '''
    Generate a text file that lists all the extensions found in a source directory, 

    # Example usage
    source_path = "path/to/source/directory"
    output_file = "path/to/output/file.txt"

    generate_extension_list_txt_for_source_path(source_path, output_file)
    
    '''
    # Set to store unique extensions
    extensions = set()

    # Iterate through all the files and subfolders in the source directory
    for root, dirs, files in os.walk(source_path):
        for file in files:
            _, extension = os.path.splitext(file)
            extensions.add(extension)

    # Write the extensions to the output file
    with open(output_file, 'w') as f:
        for extension in extensions:
            f.write(extension + '\n')

def delete_files_without_extension(source_path):
    '''
    # Example usage
    source_path = "path/to/source/directory"

    delete_files_without_extension(source_path) 
    '''
    # Iterate through all the files and subfolders in the source directory
    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if the file has no extension
            if not os.path.splitext(file_path)[1]:
                # Delete the file
                os.remove(file_path)
                print(f'No extension file found: {file_path}, Deleted...')

def delete_files_with_extension_from_list(source_path, file_types_list):
    '''
    To recursively delete all files in a source directory
    that have an extension included in a list of file types 

    # Example usage

    source_path = "path/to/source/directory"
    file_types_list = [".txt", ".csv", ".xlsx"]

    delete_files_with_extension_from_list(source_path, file_types_list)
    '''

    # Iterate through all the files and subfolders in the source directory
    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if the file extension is in the list of file types to delete
            if file_path.endswith(tuple(file_types_list)):
                # Delete the file
                os.remove(file_path)
                print(f'{file_path} removed...') 
           
def delete_empty_dirs(source_path):
    '''
    Function takes the source directory as a parameter. 
    It generates a list of all subdirectories in the source directory 
    using a list comprehension and the os.walk function. 
    
    The list is then iterated through in reverse order 
    to ensure that empty subdirectories are deleted 
    before their parent directories.

    For each subdirectory, it checks if the directory 
    is empty or contains only other directories 
    by using os.listdir and os.path.isfile. 
    
    If it's empty or contains only directories, 
    it uses os.rmdir to delete the directory.
    
    # Example usage
    source_path = "path/to/source/directory"

    delete_empty_dirs(source_path)
    '''
    # Generate a list of all subdirectories in the source directory
    subdirectories = [os.path.join(root, dir) for root, dirs, _ in os.walk(source_path) for dir in dirs]

    # Iterate through the subdirectories in reverse order
    for dir_path in reversed(subdirectories):
        # Check if the directory is empty or contains only other directories
        if not any(os.path.isfile(os.path.join(dir_path, file)) for file in os.listdir(dir_path)):
            try:
                # Delete the directory
                os.rmdir(dir_path)
                print(f'Empty dir found: \n( {dir_path} ) \nremoved...')
            except Exception as e:
                print(e) 

def rename_all_files_in_folder(source_path):
    '''
    Rename all files in a specified directory 
    by adding a random number 
    and "_renamed" to the filename.

    # Example usage
    source_path = "path/to/source/directory"

    rename_files(source_path)
    '''
    for filename in os.listdir(source_path):
        # split the filename into name and extension
        base, extension = os.path.splitext(filename)

        # generate a random number
        random_number = random.randint(100, 999)

        # create the new filename
        new_filename = f"{base}_{random_number}_renamed{extension}"

        # get the full path for the original file and the renamed file
        original_file = os.path.join(source_path, filename)
        renamed_file = os.path.join(source_path, new_filename)

        # rename the file
        os.rename(original_file, renamed_file)
        print(f'Renamed file {original_file} to {renamed_file}')

def classify_files_in_folder_by_date_creation(source_path, destination_path):
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
            try: 
                shutil.move(file_path, destination_folder)

            except Exception as e:
                print(e)

def classify_files_in_folders_by_extension(source_path):
    '''
    # Classifies all files in a source folder by their extension. 
    For each extension, it creates a new folder inside the source folder
    and moves each file to the corresponding folder. 

    # Example usage
    source_path = "path/to/source/folder"

    classify_files(source_path)    
    '''
    for filename in os.listdir(source_path):
        # split the filename into name and extension
        base, extension = os.path.splitext(filename)
        if extension:  # if the file has an extension
            # create a new folder for this extension, if it doesn't already exist
            new_folder = os.path.join(source_path, extension[1:])  # remove the dot from the extension
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

            # get the full path for the original file and the new location
            original_file = os.path.join(source_path, filename)
            new_location = os.path.join(new_folder, filename)

            # move the file
            shutil.move(original_file, new_location)
            print(f'Moved file {original_file} to {new_location}')

# Example usage
# source_path = "E:\\Life_log\\_to_clasify\\2024SamsungS21\\Almacenamiento interno"
# output_file = "E:\\Life_log\\_to_clasify\\2024SamsungS21\\file.txt"
# destination_path = "E:\\Life_log\\_to_clasify\\2024SamsungS21\\"
# file_types_list = [".webm", ".temp", ".0kmh", ".crt", ".proj_editor", ".grey", ".apk"]


# Functions 
# generate_extension_list_txt_for_source_path(source_path, output_file)
# delete_files_without_extension(source_path)
# delete_files_with_extension_from_list(source_path, file_types_list)
# delete_empty_dirs(source_path)
# rename_all_files_in_folder(source_path)
# classify_files_in_folder_by_date_creation(source_path, destination_path)
# classify_files_in_folders_by_extension(source_path)