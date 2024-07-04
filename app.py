import os
import sys
from src.HY_MLPROJECT.exception import CustomException
from src.HY_MLPROJECT.logger import logging
from src.HY_MLPROJECT.components.data_ingestion import DataIngestion
from src.HY_MLPROJECT.components.data_ingestion import DataIngestionConfig
from src.HY_MLPROJECT.components.data_transformation import DataTransformation,DataTransformationConfig

if __name__=="__main__":
    logging.info("Execution has started.")
    try:
        data_ingestion=DataIngestion()
        #data_ingestion_config=DataIngestionConfig()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    except Exception as e:
        raise CustomException(e,sys)