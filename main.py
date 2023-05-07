from src.configuration.mongodb_connection import MongoDBClient
from src.exception import CustomException
import os
from src.logger import logging
from src.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    train_pipe = TrainPipeline()
    train_pipe.run_pipeline()