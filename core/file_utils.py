import os
import glob


def read_files_from_path(path, file_format) :
    path_to_read = os.path.join(path, f"*.{file_format}")
    files = glob.glob(path_to_read, recursive=False)
    return files
