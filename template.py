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
    for folder in folders:
        os.makedirs(folder,exist_ok=True)
        with open(os.path.join(folder,".gitkeep"),"w") as file:
            pass


def create_files(files):
    for file in files:
        with open(file,"w") as ff:
            pass

create_folder(folders)
create_files(files)