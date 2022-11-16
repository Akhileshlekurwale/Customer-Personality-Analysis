#from customer_personality.config.mongo_db_connection import MongoDBClient
from customer_personality.components.stage_00_data_Ingestion import DataIngestion
import sys
from customer_personality.exception.exception_handler import AppException
from customer_personality.logger.log import logging
from customer_personality.components.stage_00_data_Ingestion import DataIngestion
from customer_personality.components.stage_01_data_Validation import DataValidation
from customer_personality.components.stage_02_data_Transformation import DataTransformation
from customer_personality.components.stage_03_model_trainer import ModelTrainer
from customer_personality.pipeline.training_pipeline.training_pipeline import TrainingPipeline


if __name__ == '__main__':
 #   mongodb_client = MongoDBClient()
 #   print("collection name: ", mongodb_client.database.list_collection_names())
    train = TrainingPipeline()
    train.start_training_pipeline()


