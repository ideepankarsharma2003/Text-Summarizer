import os
import torch
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.config.configuration import ModelTrainerConfig
from TextSummarizer.logging import logger


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig) -> None:
        self.config= model_trainer_config

    def train(self):
        device= 'cuda' if torch.cuda.is_available() else 'cpu'
        # device= 'cpu'
        logger.info(f'Device in use for training is: {device}')
        
        torch.cuda.empty_cache()
        tokenizer= AutoTokenizer.from_pretrained(self.config.model_ckpt)
        torch.cuda.empty_cache()
        # model_pegasus= AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        logger.info('Model loading.')
        model_pegasus= AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        torch.cuda.empty_cache()
        logger.info('Data Collator loading.')
        seq2seq_data_collator= DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)


        # loading data
        logger.info('Dataset loading.')
        dataset_samsum_pt= load_from_disk(self.config.data_path)

        # print(f'save steps= {self.config.save_steps}')
        trainer_args= TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            # learning_rate=self.config.learning_rate,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps, 
            gradient_accumulation_steps= self.config.gradient_accumulation_steps
        )


        trainer= Trainer(
            model=model_pegasus,
            args=trainer_args,
            data_collator=seq2seq_data_collator,
            tokenizer=tokenizer,
            train_dataset=dataset_samsum_pt['train'],
            eval_dataset=dataset_samsum_pt['validation']
        )

        torch.cuda.empty_cache()
        logger.info('Training started')
        trainer.train()
        logger.info('Training finished')

        # save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        logger.info(f'Model saved at {os.path.join(self.config.root_dir, "pegasus-samsum-model")}')
        # save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
        logger.info(f'Tokenizer saved at {os.path.join(self.config.root_dir, "tokenizer")}')
                