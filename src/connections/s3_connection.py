import boto3
import pandas as pd
import logging
from src.logger import logging
from io import StringIO
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

class s3_operations:
    def __init__(self):
        self.BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
        logging.info(f"S3 connection initialized for bucket: {self.BUCKET_NAME}")

    def fetch_file_from_s3(self, file_key):
        try:
            logging.info(f"Fetching file '{file_key}' from S3 bucket '{self.BUCKET_NAME}'...")
            obj = self.s3_client.get_object(Bucket=self.BUCKET_NAME, Key=file_key)
            df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
            logging.info(f"✅ Successfully fetched '{file_key}' with {len(df)} rows")
            return df
        except Exception as e:
            logging.exception(f"❌ Failed to fetch '{file_key}' from S3: {e}")
            raise