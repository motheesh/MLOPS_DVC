# creating template folder structure for this projects
# Author: Motheesh Jay
# Created at: 16/09/2021

import os

folders=[
os.path.join("data","raw"),
os.path.join("data","processed"),
"notebooks",
"saved_models",
"src",
]

files=[
    "params.yaml",
    "dvc.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

def create_folder(folders):
    """
    Function Name: create_folder 
    params:
        folders:
            data type: list
            Expected content: list of folders  that need to be created

    Return Type:
        on success returns True 
        on error returns False
    """
    try:
        for folder in folders:
            os.makedirs(folder,exist_ok=True)
            with open(os.path.join(folder,".gitkeep"),"w") as file:
                pass
        return True
    except Exception as e:
        return False
    


def create_files(files):
    """
    Function Name: create_files 
    params:
        folders:
            data type: list
            Expected content: list of files that need to be created

    Return Type:
        on success returns True 
        on error returns False
    """
    try:
        for file in files:
            with open(file,"w") as ff:
                pass
        return True
    except Exception as e:
        return False

create_folder(folders)
create_files(files)