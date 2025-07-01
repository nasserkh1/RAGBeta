from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from helpers.config import get_settings, Settings
from controllers import DataController
data_router = APIRouter(
    prefix= "/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{specific_topic}") #specifi_task for example course, departments staffs, semester staffs.
async def upload_data(specific_topic: str, file: UploadFile,app_settings: Settings=Depends(get_settings)):

    isvaild = DataController().validate_upload_file(file = file)

    return isvaild 