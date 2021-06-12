# Download Files From Google Driver using Google Drive Download API
This is to Download files from google repository using google driver download API: 'https://docs.google.com/uc?export=download'

Approach:
    Here we have used pythons Requests library to query and download the files from google download API: 'https://docs.google.com/uc?export=download'
    
         To download google drive files from google drive using 'https://docs.google.com/uc?export=download' url, one has to have a google drier account or publicly shared google document/file's file_id. 
         
         Idea is to download the file from google drive which has the permissions to download(public) using the file_id through above mentioned url. If the file does not have permissions, lets say its resitricted file, then your will be prompted with the appropriate error message.
         
         If the file is already downloaded, then it will be overwritten(by default, overwrite option is present if the file is already there). If the file is not present, then it will be downloaded. 
         
        There are two types of downloads here:
            1. Download files which are having Content details like Content-Disposition, Content-Length etc in the headers when queried with get request to google download link.
            2. Download files which does not have correct content details ilike Content-Disposition, Content-Length etc in the headers when queried with get request to google download link.

      Files with Content details:
          For these files, I have already kept the file details like file_id, file_name, file_type in one of the files called data/gdrive_file_data.py. User will take these file details and trigger the download form runners/TestExecutor.py file. I have not used pytest/robot framework to reduce the dependecy of libraries to be installed to run these tests
          
HOW TO RUN:
            
            Clone Git Repository, Go to folder where is downloaded.
            ex: /users/test/work/FileDownloadFromFile
            export PYTHONPATH=<path of project>. ex: 
            Execute python3 runner/TestExecutor.py


User will be able to see downloaded files here: <project>/downloadedfiles

User will be result something like this:



            PRADEEPs-MacBook-Air:FileDownloadFromDrive pradeepmallapuragowdru$ python3 runners/TestExecutor.py
            ====================================================================================================================================================== 
            Downloading files with Content-Legnth, Content-Disposition Details in Google drive and validating using final size
            ====================================================================================================================================================== 

            ------------------------------------------------------------------------------------------------------------------------------------------------------
            STARTING GOOGLE DRIVE FILE DOWNLOAD TEST CASES HERE
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_valid_doc_file_text
            response status True
            file_type= docx 
            filename= calendardoc
            Actual File size in GDrive:  238.7 KiBB
            Downloading 1xhRMnjjIVp2DRSBKizIhKjdxoZVuge2i into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/calendardoc.docx... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/calendardoc.docx
            Completed file Downloading...
            file size on disk= 238.7 KiBB
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_ppt_without_permission_test
            response status True
            Not able to get header details for passed values, please check permissions on File, header_value and file_id are present in GDRIVE or NOT
            Url trying to download file is not valid, Please check
            ERROR:*** Not a Valid test, please check test data
            TEST CASE RESULT:-----   FAIL
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  donwload_valid_ppt_file_with_permissions_test
            response status True
            file_type= pptx 
            filename= validppt
            Actual File size in GDrive:  404.2 KiBB
            Downloading 1a3ymqk7CNNTazBIBRKdZhSOzTi5F0ZGO into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/validppt.pptx... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/validppt.pptx
            Completed file Downloading...
            file size on disk= 404.2 KiBB
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_large_mp4_file_without_permissions
            response status True
            Not able to get header details for passed values, please check permissions on File, header_value and file_id are present in GDRIVE or NOT
            Url trying to download file is not valid, Please check
            ERROR:*** Not a Valid test, please check test data
            TEST CASE RESULT:-----   FAIL
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_corrupt_pdf_file_with_permissions_test
            response status True
            file_type= pdf 
            filename= yoga_ebook
            Not able to get header details for passed values, please check permissions on File, header_value and file_id are present in GDRIVE or NOT
            Url trying to download file is not valid, Please check
            ERROR:*** Not a Valid test, please check test data
            TEST CASE RESULT:-----   FAIL
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_valid_jpg_file_with_permissions_test
            response status True
            file_type= jpg 
            filename= jpg1mb
            Actual File size in GDrive:  1009.2 KiBB
            Downloading 11_jb-8qr-3OSiBfWOtQepWhp7nZUXJf9 into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/jpg1mb.jpg... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/jpg1mb.jpg
            Completed file Downloading...
            file size on disk= 1009.2 KiBB
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_valid_csv_file_with_permissions_test
            response status True
            file_type= csv 
            filename= SampleCSVFile_1109kb
            Actual File size in GDrive:  1.1 MiBB
            Downloading 1VJYaiXRNW24iXFYO3zjxXkkSVP-j2udL into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/SampleCSVFile_1109kb.csv... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/SampleCSVFile_1109kb.csv
            Completed file Downloading...
            file size on disk= 1.1 MiBB
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  download_valid_txt_file_with_zerobytes_test
            response status True
            file_type= txt 
            filename= test
            Actual File size in GDrive:  0.0 BB
            Downloading 1Q8vJLDNdTl4Lkgr8Ih3fQ_nZAHj-7iji into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/test.txt... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/test.txt
            Completed file Downloading...
            file size on disk= 0.0 BB
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            ====================================================================================================================================================== 
            Downloading files without proper Content Details in Google drive and validating by just checking the file downloader or not
            ====================================================================================================================================================== 

            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  nocontent_download_largejpg_test
            Downloading 1wVfWw7HqO_ZQHx-0xJuPukzPvVTUH8-4 into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/SampleJPGImage_20mbmb.jpg... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/SampleJPGImage_20mbmb.jpg
            Completed file Downloading...
            1623504209.6696184
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            ****STARTOF-TEST****
            Executing Test:  nocontent_download_large_zipfile_test
            Downloading 1mkXpoHt7-m-EkOG7vtZju82zy0Saft5g into /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/SampleZIPFile_100mbmb.zip... Writing content into file:  /Users/pradeepmallapuragowdru/PycharmProjects/downloadedfiles/SampleZIPFile_100mbmb.zip
            Completed file Downloading...
            1623504418.3116255
            File Downloaded correctly
            ****************************************************************************************************
            TEST CASE RESULT:-----   PASS
            ****ENDOF-TEST****
            PRADEEPs-MacBook-Air:FileDownloadFromDrive pradeepmallapuragowdru$ 
