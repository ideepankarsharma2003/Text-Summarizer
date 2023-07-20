from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger


# 6. Update the pipeline

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def run(self):
        """
        run the pipeline
        """
        config= ConfigurationManager()
        data_transformation_config= config.get_data_transformation_config()
        data_transformation= DataTransformation(data_transformation_config=data_transformation_config)
        data_transformation.transform()
