import os

def rename_files():
    #get file names from a folder
    file_list = os.listdir(r"C:\Users\Chris\Downloads\prank\prank")
    # for each file, rename filenames
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Chris\Downloads\prank\prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
        
rename_files()
