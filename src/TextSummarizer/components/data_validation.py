import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataValidationConfig




class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig):
        self.config= data_validation_config
    
    def validate_all_files_exist(self)-> bool:
        logger.info("Validation of all file existing started. ")
        try:
            validation_status= None

            with open(self.config.STATUS_FILE, 'w') as f:
                pass
            
            all_files= os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status= False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"File '{file}' not found in required files list\n")
                        f.write(f'validation status: {validation_status}\n\n')
                
                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"File '{file}' found in required files list\n")
                        f.write(f'validation status: {validation_status}\n\n')

            return validation_status
        except Exception as e:
            raise(e)