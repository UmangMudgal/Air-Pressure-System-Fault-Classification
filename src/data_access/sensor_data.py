import sys
from typing import Optional

import numpy as np
import pandas as pd

from src.configuration.mongodb_connection import MongoDBClient
from src.constant.database import DATABASE_NAME
from src.exception import CustomException


class SensorData:
    """
    Description : This class help to export the MongoDB record as dataframe
    """

    def __init__(self):
        try:
            self.mongodb_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise CustomException(e, sys)
        
    def export_collection_as_dataframe(
            self, collection_name : str , database_name:Optional[str]=None
            )-> pd.DataFrame:
        try:
            """
            Description : Export Entire Collection as DataFrame
            Returns : Pandas DataFrame
            """
            if database_name is None:
                collection = self.mongodb_client.database[collection_name]
            else:
                collection = self.mongodb_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df= df.drop(columns=["_id"], axis=1)

            df.replace({"na":np.nan}, inplace = True)

            return df
        
        except Exception as e:
            raise CustomException(e, sys)
        




