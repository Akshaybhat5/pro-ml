#libraries
import os
import sys

from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pickle

#exception and logger libraries
from src.exception import CustomException
from src.logger import logging
from src.utils import save_objects

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join("artifact", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This function is responsible for creating a data transformer
        """
        try:
            numerical_columns = ["reading_score","writing_score"]
            categorical_columns = ["gender", "race_ethnicity","parental_level_of_education","lunch","test_preparation_course"]
            
            #numerical pipeline
            num_pipeline = Pipeline(steps= [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            #categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ("encoder", OneHotEncoder())
            ])

            #final pipeline
            preprocessor = ColumnTransformer(transformers= [
                ('num_part', num_pipeline, numerical_columns),
                ("cat_part", cat_pipeline, categorical_columns)
            ])
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test set completed")

            logging.info("data transformation initiated")
            preprocessor_obj = self.get_data_transformer_object()

            target_column = "math_score"
            
            #training set
            input_train_df = train_df.drop(columns=[target_column], axis=1)
            input_train_target_df = train_df[target_column]

            #test set
            input_test_df = test_df.drop(columns=[target_column], axis=1)
            input_test_target_df = test_df[target_column]

            logging.info(f"Preprocessing application on the data is initiated")

            #array
            input_train_array = preprocessor_obj.fit_transform(input_train_df)
            input_test_array = preprocessor_obj.transform(input_test_df)

            #complete array
            train_array = np.c_[input_train_array, np.array(input_train_target_df)]
            test_array = np.c_[input_test_array, np.array(input_test_target_df)]

            save_objects(
                file_path= self.data_transformation_config.preprocessor_obj_file_path,
                obj= preprocessor_obj
            )

            return(
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_obj_file_path
            )




        except Exception as e:
            raise CustomException(e, sys)


