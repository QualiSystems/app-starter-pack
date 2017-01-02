import os
import zipfile


def zippit(source_path, zip_name, files, destination_path):
    with zipfile.ZipFile(os.path.join(destination_path, zip_name), mode='w') as zf:
        for file in files:
            zf.write(os.path.join(source_path, file), arcname=file)


def get_files(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            relDir = os.path.relpath(dirpath, path)
            relFile = os.path.join(relDir, filename)
            files.append(relFile)
    return files