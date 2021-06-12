import sys
from config import *
from os import makedirs
from os.path import dirname
from os.path import exists

import requests
from sys import stdout


class DownloadFileFromGoogleDrive():
    '''
    Downloading file from google drive with different permissions
    '''


    @staticmethod
    def download_file_from_gdrive(file_id, dest_path, overwrite=True):
        '''
        download_file_From_gdrive('23234', '/test.docx', overwrite=True)
        :return: final size downloaded - optional
        '''

        destination_directory = dirname(dest_path)
        if not exists(destination_directory):
            makedirs(destination_directory)

        if not exists(dest_path) or overwrite:
            try:
                session = requests.Session()

                print('Downloading {} into {}... '.format(file_id, dest_path), end='')
                stdout.flush()

                response = session.get(GDRIVE_URL, params={'id': file_id}, stream=True)

                token = DownloadFileFromGoogleDrive.return_token_warning(response)
                if token:
                    params = {'id': file_id, 'confirm': token}
                    response = session.get(GDRIVE_URL, params=params, stream=True)

                current_download_size = [0]
                finalsize = DownloadFileFromGoogleDrive.download_file_with_chunk(response, dest_path,current_download_size)
                # print('Final size',finalsize)
                print("Completed file Downloading...")
                # return ReadableSize.human_readable_size(finalsize), response.headers
            except:
                print("Not able to download file, Please check download URL or the passed file_id")
                sys.exit(0)


    @staticmethod
    def get_file_header_details(file_id):
        try:
            response = requests.get(GDRIVE_URL, params={'id': file_id}, stream=True)
            return response.headers
        except:
            print("NOT WORKING: Please check google download URL or the passed file_id")
            sys.exit(0)

    @staticmethod
    def get_url_status_details(url, file_id):
        try:
            response = requests.get(url, params={'id': file_id})
            # print(response)
            print("response status", response.ok)
            return response.ok
        except:
            print("NOT WORKING: Please check google download URL")
            sys.exit(0)


    @staticmethod
    def download_file_with_chunk(response, dest, current_size):
        print("Writing content into file: ",dest)
        with open(dest, FILE_WRITE_MODE) as dfile:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  #checking if the value is present or not
                    dfile.write(chunk)
                    current_size[0]+=CHUNK_SIZE
        return current_size[0]

    @staticmethod
    def return_token_warning(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None



