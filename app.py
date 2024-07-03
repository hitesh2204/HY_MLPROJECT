import os
import sys
from src.HY_MLPROJECT.exception import CustomException
from src.HY_MLPROJECT.logger import logging
from src.HY_MLPROJECT.components.data_ingestion import DataIngestion
from src.HY_MLPROJECT.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("Execution has started.")

    try:
        data_ingestion=DataIngestion()
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)