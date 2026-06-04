import os
import shutil

def copy_files_recursive(source_dir_path: str, dest_dir_path: str) -> None:
    
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for path in os.listdir(source_dir_path):
        new_path = os.path.join(source_dir_path, path)
        if os.path.isfile(new_path):
            shutil.copy(new_path, os.path.join(dest_dir_path, path))
        else:
            copy_files_recursive(new_path, os.path.join(dest_dir_path, path))

    


