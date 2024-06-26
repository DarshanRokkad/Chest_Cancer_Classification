import os
import zipfile
import gdown
from lung_cancer_classifier import logger
from lung_cancer_classifier.config.configuration import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
            
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''
        try: 
            os.makedirs(self.config.root_dir, exist_ok=True)
            
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")            
            
            prefix = 'https://drive.google.com/uc?/export=download&id='
            file_id = dataset_url.split("/")[-2]
            download_url = prefix + file_id
            gdown.download(download_url, zip_download_dir)
            
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f'Extracted data from zip file')