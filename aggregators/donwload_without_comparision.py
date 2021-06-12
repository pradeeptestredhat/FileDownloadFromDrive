import os
from basemodule.filedownlader.downloader import DownloadFileFromGoogleDrive as downloadfile
from basemodule.utils.check_file_time_diff import TimeDiff
from config import FILE_PATH

def download_without_comp(file_id, filename, filetype):
    '''
    download_without_comp()
    This is to download file without checking for length or size
    :param file_id:  string
    :param filename:  string
    :param filetype:  string
    :return: file downloaded or not as "YES/NO"
    '''

    file_name = FILE_PATH + filename.strip() + '.' + filetype.strip()
    # before download starts
    last_time=99999999999.9
    already_present = False
    if os.path.exists(file_name):
        last_time = os.path.getmtime(file_name)
        already_present = True
        print(last_time)

    downloadfile.download_file_from_gdrive(file_id, file_name, overwrite=already_present)

    #After file downloaded
    present_time = 0.0
    file_downloaded = "NO"
    if os.path.exists(file_name):
        present_time = os.path.getmtime(file_name)
        print(present_time)
        file_downloaded = "YES"

    if already_present:
        if TimeDiff.check_time_diff(last_time, present_time):
            print("file downloaded again by overwriting existing one")
        else:
            print("new file downloaded")

    return file_downloaded



# if __name__=='__main__':
#     download_without_comp('1B_ygjJgqNRoM9ViouJHsPX4RVPHOSYEU', '—Pngtree—stay safe and stay home_5339996', 'png')