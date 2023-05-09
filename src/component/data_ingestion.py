from src.exception import CustomException 
from src.logger import logging
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.utils.utilis import read_yaml_file
from src.constant.training_pipeline import SCHEMA_FILE_PATH
import os, sys
from pandas import DataFrame    
from src.data_access.sensor_data import SensorData
from sklearn.model_selection import train_test_split
class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e, sys)

    def export_data_to_feature_store(self) -> DataFrame:
        """
        Description : Export the MongoDB collection Record into Feature Store
        """
        try:
            
            logging.info("Exporting data from MongoDB to Feature Store")
            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            #Creating Folder 
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False,header=True)
            return dataframe



        except Exception as e:
            raise CustomException(e,sys)

    def split_data_as_train_test(self, dataframe : DataFrame):
        """
        Description : Performs the train test split on the Feature Store dataset for the training and validation purpose 
        """
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )

            logging.info("Performed Train Test Split on the dataframe.")

            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info("Exported train and test file path")
        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try :
            dataframe = self.export_data_to_feature_store()
            dataframe = dataframe.drop(self._schema_config["drop_columns"], axis=1)
            self.split_data_as_train_test(dataframe=dataframe)
            data_ingestion_artifact= DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, 
                                  test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)
        
