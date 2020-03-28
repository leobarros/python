import zipfile

with zipfile.ZipFile('files.zip', 'w',
                     compression=zipfile.ZIP_DEFLATED) as meu_zip:
    meu_zip.write('./texto.txt')
    meu_zip.write('./fireball.jpg')
