from typing import Union
from PyPDF2 import PdfReader, PdfWriter

def secure_pdf(input_path: str, password: str, output_path: Union[str, None] = None) -> str:
    """
    Шифрует PDF-файл паролем и сохраняет в новый файл.

    :param input_path: Путь к исходному PDF-файлу.
    :param password: Пароль для шифрования PDF.
    :param output_path: Путь к зашифрованному файлу. Если не указан — формируется автоматически.
    :return: Путь к зашифрованному PDF-файлу.
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    if not output_path:
        output_path = f'encrypted_{input_path}'

    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

    return output_path

if __name__ == '__main__':
    file = 'secret.pdf'
    password = 'pythontoday'
    result = secure_pdf(file, password)
    print(f'✅ Зашифрованный файл создан: {result}')
