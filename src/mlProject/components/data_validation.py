import pandas as pd
from src.mlProject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            validation_status_dtype = None
            data = pd.read_csv('artifacts/data_ingestion/winequality-red.csv')
            all_cols = list(data.columns)
            all_schema_dict = self.config.all_schema
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                # print(all_schema_dict.get(col) == data[col].dtype)
                if col in all_schema and (all_schema_dict.get(col) == data[col].dtype):
                    validation_status = True
                    validation_status_dtype = True
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation Status: {validation_status}\nData Type Validation: {validation_status_dtype}")
                else:
                    validation_status = False
                    validation_status_dtype = False
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation Status: {validation_status}\nData Type Validation: {validation_status_dtype}")

            return validation_status and validation_status_dtype

        except Exception as e:
            raise e