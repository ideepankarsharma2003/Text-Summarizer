# 5. Update the components

import os
import urllib.request as request
import zipfile
from pathlib import Path
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity import DataIngestionConfig




class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        self.data_ingestion_config= data_ingestion_config


    def download_file(self):
        if not os.path.exists(self.data_ingestion_config.local_data_file):
            filename, headers= request.urlretrieve(
                url= self.data_ingestion_config.source_URL,
                filename= self.data_ingestion_config.local_data_file
            )
            logger.info(f'{filename} is downloaded with following info: \n{headers}')
        
        else:
            logger.info(f'File already exists of size: {get_size(Path(self.data_ingestion_config.local_data_file))}')


    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory 
        Function returns None
        '''
        unzip_path= self.data_ingestion_config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        print(f' filename= {self.data_ingestion_config.local_data_file}')
        with zipfile.ZipFile(self.data_ingestion_config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'Unzipped {self.data_ingestion_config.local_data_file} at {unzip_path} successfully.')
