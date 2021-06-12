import os
import re
import sys

from basemodule.filedownlader.downloader import DownloadFileFromGoogleDrive as downloadfile
from basemodule.utils.readable_size import ReadableSize
from basemodule.utils.get_header_details import get_header_values
from config import *
from basemodule.utils.check_file_time_diff import TimeDiff


def download_file_with_size_status(file_id, filename, filetype):
    '''
        download_file_with_size_status()
        This is to download file with checking size after file download as verification step
        :param file_id:  string
        :param filename:  string
        :return: file downloaded or not as "YES/NO"
    '''

    fl=''
    actual_gdrive_file_size=0
    actual_gdrive_file_name=''

    try:
        if downloadfile.get_url_status_details(GDRIVE_URL, file_id):
            #Finding out filetype from the google drive file, if not present then adding it from predefined value
            full_filename=get_header_values(file_id, CONTENT_DISPOSITION)
            if full_filename is None:
                fl = filetype
                actual_gdrive_file_name = filename
            else:
                fl = full_filename.split(".")[-1]
                actual_gdrive_file_name = full_filename.split(".")[0]
                print("file_type=", fl.strip(), "\nfilename=", actual_gdrive_file_name)

            #Getting the Fiile Size from google driver
            actual_gdrive_file_size = get_header_values(file_id, CONTENT_LENGTH)
            if actual_gdrive_file_size is None:
                actual_gdrive_file_size = ReadableSize.human_readable_size(int(filesize))


            print("Actual File size in GDrive: ",actual_gdrive_file_size)
            #downloading file here
            filename=FILE_PATH+actual_gdrive_file_name.strip()+'.'+fl.strip()
            # Before File download, checking for file exists or not
            last_time=99999999999.9
            present=False
            if os.path.exists(filename):
                last_time = os.path.getmtime(filename)
                present=True

            downloadfile.download_file_from_gdrive(file_id, filename, overwrite=True)
            # print(size)
            disk_file_size=ReadableSize.human_readable_size(os.stat(filename).st_size)
            print("file size on disk=",disk_file_size)


            #After file downloaded:
            present_time = 0.0
            file_downloaded = "NO"
            if os.path.exists(filename):
                present_time = os.path.getmtime(filename)
                file_downloaded = "YES"

            if present:
                if TimeDiff.check_time_diff(last_time, present_time):
                    print("file downloaded again by overwriting existing one")
                else:
                    print("new file downloaded")

            return disk_file_size, actual_gdrive_file_size, file_downloaded
    except:
        print("Url trying to download file is not valid, Please check")
        sys.exit(0)

# if __name__=='__main__':
#     download_file_with_size_status('1_9v1ghPwVc42tUHrAcLXhh9sqEfFvGOJ', 'test', 'docx', 1)
