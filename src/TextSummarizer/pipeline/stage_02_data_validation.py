from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.logging import logger


# 6. Update the pipeline

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def run(self):
        """
        run the pipeline
        """
        config= ConfigurationManager()
        data_validation_config= config.get_data_validation_config()
        data_validation= DataValidation(data_validation_config=data_validation_config)
        data_validation.validate_all_files_exist()
