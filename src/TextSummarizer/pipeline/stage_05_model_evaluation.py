from TextSummarizer.logging import logger
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_evaluation import ModelEvaluation


# 6. Update the pipeline

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def run(self):
        """
        run the pipeline
        """
        config= ConfigurationManager()
        model_evaluation_config= config.get_model_evaluation_config()
        model_evaluation= ModelEvaluation(model_evaluation_config= model_evaluation_config)
        logger.info('Started Model Evaluation')
        model_evaluation.evaluate()

