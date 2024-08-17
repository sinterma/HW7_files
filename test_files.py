from pypdf import PdfReader
import zipfile
import csv
import io
from openpyxl import load_workbook
from io import BytesIO


def test_pdf_zip():

    pdf_filename = "tmp/test.pdf"
    zip_filename = "archive1.zip"


    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        zip_file.write(pdf_filename, arcname="test.pdf")

    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        with zip_file.open("test.pdf") as pdf_file:
            reader = PdfReader(pdf_file)
            page_text = reader.pages[0].extract_text()

            assert "Тестовый PDF файл" in page_text

test_pdf_zip()


def test_csv_zip():
    csv_filename = "tmp/train.csv"
    zip_filename = "archive2.zip"

    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        zip_file.write(csv_filename, arcname="train.csv")

    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        with zip_file.open("train.csv") as csv_file:

            csv_content = csv_file.read()
            csv_text = csv_content.decode('utf-8')
            csv_file_like = io.StringIO(csv_text)
            reader = csv.reader(csv_file_like)
            header = next(reader)

            assert "Name" in header

test_csv_zip()


def test_xlsx_zip():
    xlsx_filename = 'tmp/import_empl_xlsx.xlsx'
    zip_filename = 'archive3.zip'

    with zipfile.ZipFile(zip_filename, mode='w') as zip_file:
        zip_file.write(xlsx_filename, arcname="import_empl_xlsx.xlsx")

    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        with zip_file.open("import_empl_xlsx.xlsx") as xlsx_file:

            with BytesIO(xlsx_file.read()) as temp_file:

                workbook = load_workbook(temp_file)
                sheet = workbook.active

                text = sheet.cell(row=2, column=2).value
                assert "Иванова" in text

test_xlsx_zip()


