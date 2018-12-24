import os
import pandas as pd

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.client import GoogleCredentials

from google.colab import auth

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)


def ls():
    return drive.ListFile({'q': "trashed=false"}).GetList()


def read_file_with(read_function, file_id, *args, **kwargs):
    """
    Reads a file with file_id using read_function from GoogleDrive. Additional args/kwargs passed to read_function.
    """
    download_path = os.path.expanduser('~/data')
    try:
        os.makedirs(download_path)
    except FileExistsError:
        pass

    output_file = os.path.join(download_path, 'test.csv')
    temp_file = drive.CreateFile({'id': file_id})
    temp_file.GetContentFile(output_file)
    return read_function(output_file, *args, **kwargs)
