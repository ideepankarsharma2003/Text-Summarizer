from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME= 'Data Ingestion Stage'

try:
    logger.info(f'{">"*20} stage: {STAGE_NAME} started {"<"*20}')
    pipeline = DataIngestionTrainingPipeline()
    pipeline.run()
    logger.info(f'{">"*20} stage: {STAGE_NAME} completed {"<"*20}')
except Exception as e:
    logger.exception(e)
    raise e








STAGE_NAME= 'Data Validation Stage'

try:
    logger.info(f'{">"*20} stage: {STAGE_NAME} started {"<"*20}')
    pipeline = DataValidationTrainingPipeline()
    pipeline.run()
    logger.info(f'{">"*20} stage: {STAGE_NAME} completed {"<"*20}')
except Exception as e:
    logger.exception(e)
    raise e







STAGE_NAME= 'Data Transformation Stage'

try:
    logger.info(f'{">"*20} stage: {STAGE_NAME} started {"<"*20}')
    pipeline = DataTransformationTrainingPipeline()
    pipeline.run()
    logger.info(f'{">"*20} stage: {STAGE_NAME} completed {"<"*20}')
except Exception as e:
    logger.exception(e)
    raise e










STAGE_NAME= 'Model Trainer Stage'

try:
    logger.info(f'{">"*20} stage: {STAGE_NAME} started {"<"*20}')
    pipeline = ModelTrainerTrainingPipeline()
    pipeline.run()
    logger.info(f'{">"*20} stage: {STAGE_NAME} completed {"<"*20}')
except Exception as e:
    logger.exception(e)
    raise e