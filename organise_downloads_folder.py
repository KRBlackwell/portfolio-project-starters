# print time ran
# check space on disk
# check space in downloads folder
#copy it as downloads_backup
#stuff thats older than X archive in separate subfolder
#python organize_downloads_folder.py > organized_report_08jan24.txt
import os
import shutil
from datetime import datetime


def organize_downloads_folder():
    create_folders = ["PTA", "School", "Data", "Images", "Documents", "Videos", "Screenshots", "Executables", "Zips", "scripts", "Calendar", "PDFs", "Others"]
    for folder in create_folders:
        folder_path = os.path.join(organized_folder_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)
        print("file_path:", file_path)

        if os.path.isfile(file_path):
            file_destination = get_destination(filename)
            print("file_destination:", file_destination)
            if file_destination:
                destination_folder = os.path.join(organized_folder_path, file_destination)
                print("destination_folder")
                print()
                print("move files:"
                move_it(file_path, destination_folder)
    print()
    print()
    print("...***....Congrats! Don't you feel organized? ******")

def get_destination(filename):
    # You can extend this function to recognize more file types
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    document_extensions = [".pdf", ".doc", ".docx", ".txt"]
    video_extensions = [".mp4", ".mov", ".avi"]
    script_extensions = [".py", ".ipynb", ".ksh", ".sh", ".sas", ".java", ".h", ".html", ".bat", ".ps1"]
    compress_extensions = [".zip", ".gz", ".tar"]
    calendar_extensions = [".ical", ".ics"]
    executables_extensions = [".exe", ".bin"]
    minecraft_extensions = [".mcaddon"]
    data_extensions = [".json", ".csv", ".xls", ".sas"]
    school_substrings = ["weekly calendar", "nurse", "sick children", "festival", "open house"]
    pta_substrings = ["pta", "contact", "students-list", "family-list", "givebacks", "memberhub"]
    file_extension = os.path.splitext(filename)[1].lower()
    print("ext:", file_extension)
    
    file_name = os.path.splitext(filename)[0].lower()
    print("name:", file_name)

    if "screenshot" in file_name:
        return "Screenshots"
    # elif ("weekly calendar" in file_name) | ("nurse" in file_name) | ("sick children" in file_name) | ("open house" in file_name):
    elif any(substr in file_name for substr in school_substrings):
        return "School"
    # elif ("pta" in file_name) | ("contact" in file_name) | ("students-list" in file_name) | ("family-list" in file_name):
    elif any(substr in file_name for substr in pta_substrings):
        return "PTA"
    elif ("calendar" in file_name) | (file_extension in calendar_extensions):
        return "Calendar"
    elif file_extension in image_extensions:
        return "Images"
    elif ("data" in file_name) | ("census" in file_name) | (file_extension in data_extensions):
        return "Data"
    elif file_extension in document_extensions:
        return "Documents"
    elif file_extension in video_extensions:
        return "Videos"
    elif file_extension in executables_extensions:
        return "Executables"
    elif file_extension in compress_extensions:
        return "Zips"
    elif file_extension in ".pdf":
        return "PDFs"
    elif file_extension in script_extensions:
        return "scripts"
    else:
        return "Others"

def move_it(source_path, destination_path):
    # shutil will preserve file metadata 
    try:
        shutil.move(source_path, destination_path)
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    #if your path uses your username:
    folder_username = os.getenv('USERNAME') #to get your windows username
    # folder_username = os.getenv('USER') #to get your linux or mac username
    print("username:", folder_username)
    # downloads_path = os.path.join("~", "downloads") #For Linux. Same for mac?
    downloads_path = os.path.join("C:\\",'Users',folder_username,'downloads')  # Replace with the actual path
    print("downloads folder:", downloads_path)
    organized_folder_path = os.path.join("C:\\",'Users',folder_username,'downloads','organized')  # Replace with the desired path
    print()
    try:
        os.makedirs(organized_folder_path)
    except FileExistsError:
        print("Directory already exists:", organized_folder_path)
    print(organized_folder_path)
    print()
    organize_downloads_folder()
