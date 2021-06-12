import os

CHUNK_SIZE = 1024
GDRIVE_URL = 'https://docs.google.com/uc?export=download'
GDRIVE_INVALID_URL = 'https://test23498sdfaprasd.com'
FILE_WRITE_MODE = 'wb'
FILE_PERMISSION = 0o777
CONTENT_DISPOSITION = 'Content-Disposition'
CONTENT_LENGTH = 'Content-Length'
FILE_PATH = os.getcwd() + "/downloadedfiles/"