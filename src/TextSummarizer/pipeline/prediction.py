from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self) -> None:
        self.config= ConfigurationManager().get_model_evaluation_config()


    def predict(self, text):
        tokenizer= AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs= {
            "length_probablity": 0.8,
            "num_beans": 8,
            "max_length": 128

        }

        logger.info("Initializing the prediction pipeline")
        pipe= pipeline("summarization", model= self.config.model_path, tokenizer= tokenizer)

        print("Dialogue: ")
        print(text)

        logger.info("Output is generated.")
        # output= pipe(text, **gen_kwargs)[0]["summary_text"]
        output= pipe(text)[0]["summary_text"]
        logger.info(f"Summary: {output}")
        print('\nModel Summary: ')
        print(output)



        return output