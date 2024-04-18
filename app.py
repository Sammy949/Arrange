import os
import shutil
import time

# Checks Work Directory
def check_cwd():
    while True:
        current_cwd = input("Enter Directory: ")
        if os.path.isdir(current_cwd):
            return current_cwd.lower()
        else: print("Invalid Directory. Please enter a valid directory")
    
# Lists the files in the chosen directory
def list_files(directory):
    try:
        cwd_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        file_num = len(cwd_files)

        if file_num >= 1:
            return {"cwd_files": cwd_files, "file_num": file_num}
        else:
            print("File number in the chosen directory is too low to continue.")
            return {"cwd_files": [], "file_num": 0}
            
    except OSError as e:
        print(f"Error occured: {e}")
        return {"cwd_files": [], "file_num": 0}
        
    
# Static Folders
def create_static_folders(directory):
    try:
        # Creates folders for file grouping
        image_folder = os.path.join(directory, "Images")
        audio_folder = os.path.join(directory, "Audio")
        document_folder = os.path.join(directory, "Docs")
        others_folder = os.path.join(directory, "Others")

        # Checks folder existence
        os.makedirs(image_folder, exist_ok=True)
        os.makedirs(audio_folder, exist_ok=True)
        os.makedirs(document_folder, exist_ok=True)
        os.makedirs(others_folder, exist_ok=True)
        
        return {"image_folder": image_folder, "audio_folder": audio_folder, "document_folder": document_folder, "others": others_folder}
    except OSError as e:
        print(f"Error occured: {e}")
        return {"image_folder": None, "audio_folder": None, "document_folder": None, "others": None}

def sort_files(directory, folders):
    try:
        files = list_files(directory)
        organized_files = 0
        unorganized_files = 0

        for file in files["cwd_files"]:
            file_path = os.path.join(directory, file)
            file_extension = os.path.splitext(file)[-1]
            
            if file_extension.lower() in [".jpg", ".jpeg", ".png", ".gif"]:
                shutil.move(file_path, folders["image_folder"])
                organized_files += 1
            elif file_extension.lower() in [".mp3", ".wav", ".wma"]:
                shutil.move(file_path, folders["audio_folder"])
                organized_files += 1
            elif file_extension.lower() in [".pdf", ".doc", ".docx", ".txt"]:
                shutil.move(file_path, folders["document_folder"])
                organized_files += 1
            else:
                print(f'- Could not sort file: {file} as its type is not recognized.')
                shutil.move(file_path, folders["others"])
                
                unorganized_files += 1
        return {"organized_files": organized_files, "unorganized_files": unorganized_files}

    except Exception as e:
        print(f'Error occured: {e}')
        return {"organized_files": 0, "unorganized_files": 0}

def main():
    try:
        cwd = check_cwd()
        print(f"Chosen Work Directory: \"{cwd}\"")
        print("----------------------------------------------")
        
        files = list_files(cwd)
        print(f"Number of files:", files["file_num"])
        time.sleep(1)
        print("----------------------------------------------")

        print("Process Initiating...")
        time.sleep(2)

        folders = create_static_folders(cwd)
        if None in folders.values():
            print("Error creating folders. Exiting.")
            return
        print("----------------------------------------------")

        sort_function = sort_files(cwd, folders)
        print("----------------------------------------------")

        time.sleep(2)
        print("Total Number of Organized Files:", sort_function["organized_files"])
        print("Total Number of Unorganized Files:", sort_function["unorganized_files"])
        print("----------------------------------------------")

    except Exception as e:
        print(f"An unexpected error occured: {e}")

    except KeyboardInterrupt:
        print(f"\nProcess interrupted by user.")

if __name__ == "__main__":        
    main()