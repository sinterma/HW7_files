import os
import zipfile


def create_zip_archive(zip_filename, files):
    if os.path.exists(zip_filename):
        os.remove(zip_filename)

    os.makedirs(os.path.dirname(zip_filename), exist_ok=True)

    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for file in files:
            zip_file.write(file, arcname=os.path.basename(file))


zip_filename = "tmp/archive.zip"
files_to_zip = ["tmp/test.pdf", "tmp/train.csv", "tmp/import_empl_xlsx.xlsx"]
