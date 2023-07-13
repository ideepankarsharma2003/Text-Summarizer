from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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