from genericpath import isfile
import os
import sys
import shutil

import marshal
import zlib
import base64


# get from user path to target project
try:
    target_path = sys.argv[1]
except:
    target_path = input("Please, enter path to project folder -> ")

# check if target is folder or separated file
targetisfolder = True
if os.path.isfile(target_path):
    targetisfolder = False

# get copy of project folder
if targetisfolder:
    target_folder_copy = target_path.replace(target_path, f"{target_path} (hidden code)")
    try:
        shutil.copytree(target_path, target_folder_copy)
    except FileExistsError as e:
        print(str(e))
        print("Copy of the project is already exist")
else:
    target_file_copy = target_path.split(".py")[0]+"(hidden code).py"
    try:
        shutil.copy(target_path, target_file_copy)
    except Exception as e:
        print(str(e))
        print("Copy of the project is already exist")

# define encryption function
def encryptor(file_path):
    # open and read python file
    with open(file_path, "r") as target_file:
        file_code = target_file.read()
    
    # encode python code
    comp = compile(file_code, 'test_marshal1', 'exec')
    mar = marshal.dumps(comp)
    zl = zlib.compress(mar)
    encoded_b = base64.b64encode(zl)
   
    # create new content of the file
    new_code = f"""import marshal, zlib, base64\n\nencoded_b = {encoded_b}\n\nexec(marshal.loads(zlib.decompress(base64.b64decode(encoded_b))))
    """
    
    # rewrite content of the file
    with open(file_path, "w") as target_file:
        target_file.write(new_code)


# get files with ".py" extension in the given directory
if targetisfolder:
    lst_files = [os.path.join(path, name) for path, subdirs, files in 
                os.walk(target_folder_copy) for name in files if 
                os.path.splitext(name)[1]=='.py']
else:
    lst_files = [target_file_copy]

# encrypt target files code
def run():
    for tf in lst_files:
        encryptor(tf)
        print(f"Done encryption with file - {tf}")

if __name__ == "__main__":
    run()