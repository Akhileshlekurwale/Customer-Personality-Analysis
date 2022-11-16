import os
from customer_personality.constant.s3_bucket import TRAINING_BUCKET_NAME

# TARGET_COLUMN = "class"
PIPELINE_NAME : str = "customer_personality"
ARTIFACT_DIR : str = "artifact"
FILE_NAME : str = 'customer.csv'

TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"