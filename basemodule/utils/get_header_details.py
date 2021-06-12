import re
import sys
from basemodule.filedownlader.downloader import DownloadFileFromGoogleDrive as downloadfile
from basemodule.utils.readable_size import ReadableSize


def get_header_values(file_id, header_value):
    header_response = downloadfile.get_file_header_details(file_id)

    try:
        if header_value == 'Content-Disposition':
            if header_response['Content-Disposition']:
                return re.search(r'filename="(.*)"', header_response['Content-Disposition']).group(1)
        elif header_response[header_value]:
            return ReadableSize.human_readable_size(int(header_response[header_value]))
        else:
            return None
    except:
        print("Not able to get header details for passed values, "
              "please check permissions on File, header_value and file_id are present in GDRIVE or NOT")
        sys.exit(1)

def get_header_check(file_id, header_value):
    header_response = downloadfile.get_file_header_details(file_id)

    try:
        if header_value == 'Content-Disposition':
            if header_response['Content-Disposition']:
                return re.search(r'filename="(.*)"', header_response['Content-Disposition']).group(1)
        elif header_response[header_value]:
            return ReadableSize.human_readable_size(int(header_response[header_value])), header_response[header_value], header_response
        else:
            return None
    except:
        print("Not able to get header details for passed values, "
                  "please check permissions on File, header_value and file_id are present in GDRIVE or NOT")
        sys.exit(1)

# if __name__=='__main__':
#     # a,b, c=get_header_values("1gsxY0cS4ix1SUz6eijWmobqlglwqWyCB", 'Content-Length')
#     # print(a,b, "\n", c)
#     print(get_header_check("1Q8vJLDNdTl4Lkgr8Ih3fQ_nZAHj-7iji", 'Content-Length'))
