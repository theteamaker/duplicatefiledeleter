import os

files_list = []
unique_files_list = []
duplicate_files = []
files_removed = 0

class FileClass:
    def __init__(self, name, data):
        self.name = name
        self.data = data

for FileOBJ in os.listdir():
    data = open(FileOBJ, 'rb').read()
    files_list.append(FileClass(FileOBJ, data))

for FileOBJ in files_list:
    is_a_duplicate = False
    for FileBeingCompared in unique_files_list:
        if FileOBJ.data == FileBeingCompared.data:
            is_a_duplicate = True
            break
        else:
            continue
    
    if is_a_duplicate is False:
        unique_files_list.append(FileOBJ)

for FileOBJ in files_list:
    if FileOBJ in unique_files_list:
        pass
    else:
        os.remove(FileOBJ.name)
        files_removed += 1

print(f"Removed {files_removed} files.")