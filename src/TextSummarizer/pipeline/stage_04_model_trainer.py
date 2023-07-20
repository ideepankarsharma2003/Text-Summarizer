from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger


# 6. Update the pipeline

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def run(self):
        """
        run the pipeline
        """
        config= ConfigurationManager()
        model_trainer_config= config.get_model_trainer_config()
        model_trainer= ModelTrainer(model_trainer_config=model_trainer_config)
        model_trainer.train()

