import zipfile

with zipfile.ZipFile('./files.zip', 'r') as meu_zip:
    meu_zip.extractall('./files')
