from data.gdrive_file_data import *
from basemodule.utils.check_file_pass_fail_status import TestResult
from aggregators.download_gdrive_files import download_file_with_size_status
from aggregators.donwload_without_comparision import download_without_comp



def download_valid_doc_file_text():
    '''
        This test is to download a valid docx file with permission to download
        Expectation: This Test has to PASS
        :return:
        '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status(docx_file['id'], docx_file['filename'], docx_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** validate test data")


def download_ppt_without_permission_test():
    '''
    This test is to download a PPT file without permission to download/readonly file
    Expectation: This Test has to FAIL
    :return:
    '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status\
        (ppt_file['id'], ppt_file['filename'], ppt_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")
        print("TEST CASE RESULT:-----   FAIL")


def donwload_valid_ppt_file_with_permissions_test():
    '''
    This test is to download a valid ppt file with permission to download
    Expectation: This Test has to PASS
    :return:
    '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status \
            (valid_ppt_file['id'], valid_ppt_file['filename'], valid_ppt_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")


def download_large_mp4_file_without_permissions():
    '''
        This test is to download a mp4 file without permission to download/readonly file
        Expectation: This Test has to FAIL
        :return:
        '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status \
            (mp4_file['id'], mp4_file['filename'], mp4_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")
        print("TEST CASE RESULT:-----   FAIL")


def download_corrupt_pdf_file_with_permissions_test():
    '''
    This test is to download a Corrupt pdf file without permission to download
    Expectation: This Test has to PASS
    :return:
    '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status \
            (pdf_corrupt_file['id'], pdf_corrupt_file['filename'], pdf_corrupt_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")
        print("TEST CASE RESULT:-----   FAIL")

def download_valid_jpg_file_with_permissions_test():
    '''
    This test is to download a valid JPG file with permission to download
    Expectation: This Test has to PASS
    :return:
    '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status \
            (jpb1mg_file['id'], jpb1mg_file['filename'], jpb1mg_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")


def download_valid_csv_file_with_permissions_test():
    '''
    This test is to download a valid csv_file file with permission to download
    Expectation: This Test has to PASS
    :return:
    '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status \
            (csv_file['id'], csv_file['filename'], csv_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")

def download_valid_txt_file_with_zerobytes_test():
    '''
    This test is to download a valid csv_file file with permission to download
    Expectation: This Test has to PASS
    :return:
    '''
    try:
        disk_file_size, actual_gdrive_file_size, download_status = download_file_with_size_status \
            (text_file['id'], text_file['filename'], text_file['file_type'])
        TestResult.test_result(disk_file_size, actual_gdrive_file_size)
    except:
        print("ERROR:*** Not a Valid test, please check test data")

#Downloading files without proper Content Details in Google drive and validating by just checking the file downloader or not
def nocontent_download_largejpg_test():
    try:
        file_downloaded = download_without_comp(jpg_large['id'], jpg_large['filename'], jpg_large['file_type'])
        TestResult.comp_result(file_downloaded)
    except:
        print("ERROR:*** Not a Valid test, please check test data")


def nocontent_download_large_zipfile_test():
    try:
        file_downloaded = download_without_comp(large_zip['id'], large_zip['filename'], large_zip['file_type'])
        TestResult.comp_result(file_downloaded)
    except:
        print("ERROR:*** Not a Valid test, please check test data")



if __name__=='__main__':
    '''
    Gdrive details: username/password   pradeeptestredhat@gmail.com/redhat@2
    github details: username/password   pradeeptestredhat/redhattestpradeep@2
    '''
    print("="*150,"\nDownloading files with Content-Legnth, Content-Disposition Details in Google drive and validating using final size")
    print("="*150,"\n")
    print("-"*150)
    print("STARTING GOOGLE DRIVE FILE DOWNLOAD TEST CASES HERE")
    print("-"*150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_valid_doc_file_text.__name__)
    download_valid_doc_file_text()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_ppt_without_permission_test.__name__)
    download_ppt_without_permission_test()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", donwload_valid_ppt_file_with_permissions_test.__name__)
    donwload_valid_ppt_file_with_permissions_test()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_large_mp4_file_without_permissions.__name__)
    download_large_mp4_file_without_permissions()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_corrupt_pdf_file_with_permissions_test.__name__)
    download_corrupt_pdf_file_with_permissions_test()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_valid_jpg_file_with_permissions_test.__name__)
    download_valid_jpg_file_with_permissions_test()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_valid_csv_file_with_permissions_test.__name__)
    download_valid_csv_file_with_permissions_test()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", download_valid_txt_file_with_zerobytes_test.__name__)
    download_valid_txt_file_with_zerobytes_test()
    print("****ENDOF-TEST****")
    print("=" * 150,"\nDownloading files without proper Content Details in Google drive and validating by just checking the file downloader or not")
    print("=" * 150, "\n")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", nocontent_download_largejpg_test.__name__)
    nocontent_download_largejpg_test()
    print("****ENDOF-TEST****")
    print("-" * 150)
    print("****STARTOF-TEST****")
    print("Executing Test: ", nocontent_download_large_zipfile_test.__name__)
    nocontent_download_large_zipfile_test()
    print("****ENDOF-TEST****")