import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlProject.config.configuration import DataTransformationConfig
from src.mlProject import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted Data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
