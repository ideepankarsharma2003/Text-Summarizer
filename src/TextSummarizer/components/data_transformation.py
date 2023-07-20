import os
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataTransformationConfig




class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig) -> None:
        self.config= data_transformation_config
        self.tokenizer= AutoTokenizer.from_pretrained(data_transformation_config.tokenizer_name)





    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    

    def transform(self):
        logger.info('Transformation Started')
        dataset_samsum= load_from_disk(self.config.data_path)
        dataset_samsum_pt= dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(
            os.path.join(self.config.root_dir, "samsum_dataset")
            )