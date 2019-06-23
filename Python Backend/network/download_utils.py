import requests
import zipfile
import os


def download_file(url, name, location):
    myfile = requests.get(url + name)

    if not os.path.exists(location):
        os.makedirs(location)

    open(location + name, 'wb').write(myfile.content)


def unzip_file_and_delete(name):
    zip_ref = zipfile.ZipFile(name, 'r')
    zip_ref.extractall(name[0:len(name)-4])
    zip_ref.close()

    os.remove(name)
