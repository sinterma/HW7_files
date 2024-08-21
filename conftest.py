import pytest
import zipfile
import os

@pytest.fixture(scope="function", autouse=True)
def create_zip_archive():
    def _create_zip_archive(zip_filename, files):
        if os.path.exists(zip_filename):
            os.remove(zip_filename)

        os.makedirs(os.path.dirname(zip_filename), exist_ok=True)

        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            for file in files:
                zip_file.write(file, arcname=os.path.basename(file))
    return _create_zip_archive
