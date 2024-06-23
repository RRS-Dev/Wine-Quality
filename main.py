from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage04_model_trainer import ModelTrainerPipeline



# logger.info('Welcome to custom logging')

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nxxxxxxxxx")
except Exception as e:
    raise e
    

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nxxxxxxxxx")
except Exception as e:
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nxxxxxxxxx")
except Exception as e:
    raise e

STAGE_NAME = "Model Trainer"

try:
    logger.info(">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    raise e

