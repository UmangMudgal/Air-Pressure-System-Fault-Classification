import os
from src.constant.s3_bucket import TRAINING_BUCKET_NAME

#defining common constant variable for training pipeline
TARGET_COLUMN = 'class'
PIPELINE_NAME : str = 'aps'
ARTIFACT_DIR : str = 'artifact'
FILE_NAME : str = 'aps.csv'


TRAIN_FILE_NAME : str = 'train.csv'
TEST_FILE_NAME : str = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
MODEL_FILE_NAME = 'model.pkl'
SCHEMA_FILE_PATH = os.path.join('config', 'schema.yaml')
SCHEMA_DROP_COLS = 'drop_columns'

"""
Data Ingestion Related Constant
start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME : str = 'APS'
DATA_INGESTION_DIR_NAME : str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR :str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2



"""
Data Validataion Related Constant 
start with DATA_VALIDATION
"""
DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR :str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPOR_FILE_NAME : str = "report.yaml"
