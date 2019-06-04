import requests
import zipfile
import os


def download_file(url, name):
    myfile = requests.get(url)
    open(name, 'wb').write(myfile.content)


def unzip_file_and_delete(name):
    zip_ref = zipfile.ZipFile(name, 'r')
    zip_ref.extractall(name[0:len(name)-4])
    zip_ref.close()

    os.remove(name)
