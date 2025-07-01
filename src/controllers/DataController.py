from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes
    def validate_upload_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
              return {
                   "Error": "The file type is not supported!",
                   "The types are allowed": [".txt",".pdf",".docx"],
                   "status": False
              }

                
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale: # file.size is the size of file in byte unit
                return {
                      "Error":"You are uploading a file that exceeds the maximum allowed size!",
                      "The size of file that are allowed": str(self.app_settings.FILE_MAX_SIZE) + " MB",
                      "Your file size is":str(file.size) + " Byte(s)",
                      "status": False
                }

        return {
                      "message":"file uploaded!",
                      "status": True
                }