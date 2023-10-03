import os
from pathlib import path
import logging
FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

logging.basicConfig(level=logging.info,format=FORMAT)

PROJECT_NAME = "ML_PROJECT"

LIST_OF_FILES=[
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "research/trials.ipynb",
       
]


for file_path in LIST_OF_FILES:
    file_path = path(file_path)
    
    file_dr,file_name = os.path.split(file_path)
    
    if file_dr != " ":
        os.makedirs(file_dr,exist_ok=True)
        logging.info(f"creating directory ;{file_dr} for the file:{file_name}")
        
        
        
        
    if(not os.path.exists(file_path)) or (os.path.getsize(filepath)==0):
        with open(file_path, "w") as f:
            pass 
        logging.info(f"creating empty file:{file_path}")
        
    else:
        logging.info(f"{file_name}:already exists")