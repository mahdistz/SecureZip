import os
from pathlib import Path

import pyzipper
import secrets
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] [%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)
BASE_DIR = Path(__file__).resolve().parent


def create_zip_with_password(item_path, password, zip_files_path):
    try:
        if os.path.isfile(item_path):
            item_name = os.path.splitext(os.path.basename(item_path))[0]
            zip_file_path = os.path.join(zip_files_path, f"{item_name}.zip")
            with pyzipper.AESZipFile(zip_file_path, 'w', compression=pyzipper.ZIP_STORED,
                                     encryption=pyzipper.WZ_AES) as zf:

                zf.setpassword(bytes(password, 'utf-8'))
                zf.write(item_path, os.path.basename(item_path))

        elif os.path.isdir(item_path):
            zip_file_path = os.path.join(zip_files_path, f"{os.path.basename(item_path)}.zip")
            with pyzipper.AESZipFile(zip_file_path, 'w', compression=pyzipper.ZIP_STORED,
                                     encryption=pyzipper.WZ_AES) as zf:

                zf.setpassword(bytes(password, 'utf-8'))
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zf.write(file_path, os.path.relpath(file_path, item_path))

        logging.info(f"Zip file created at: {zip_file_path}")
        logging.info(f"Password: {password}")

    except Exception as e:
        logging.error(f'An error occurred: {e}')


def main():
    item_path = input("Enter the file or folder path: ").strip().strip('"').replace("\\", "/")
    user_password = input("Enter a password for the zip file (leave blank to use a random password): ").strip()

    zip_files_path = os.path.join(BASE_DIR, 'zip_files')
    if not os.path.exists(zip_files_path):
        os.makedirs(zip_files_path)

    if not user_password:
        password = secrets.token_urlsafe(16)
        create_zip_with_password(item_path=item_path, password=password, zip_files_path=zip_files_path)
    else:
        create_zip_with_password(item_path=item_path, password=user_password, zip_files_path=zip_files_path)


if __name__ == "__main__":
    main()
