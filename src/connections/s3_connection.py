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
    def __init__(self, BUCKET_NAME, ACCESS_KEY_ID, SECRET_ACCESS_KEY, region_name="us-east-1"):
        """
        Initialize the s3_operations class with AWS credentials and S3 bucket details.
        """
        self.BUCKET_NAME = BUCKET_NAME
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        ) 
        logging.info("Data Ingestion from S3 bucket initialized")

    def fetch_file_from_s3(self, file_key):
        """
        Fetches a CSV file from the S3 bucket and returns it as a Pandas DataFrame.
        :param file_key: S3 file path (e.g., 'data/data.csv')
        :return: Pandas DataFrame
        """
        try:
            logging.info(f"Fetching file '{file_key}' from S3 bucket '{self.BUCKET_NAME}'...")
            obj = self.s3_client.get_object(Bucket=self.BUCKET_NAME, Key=file_key)
            df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
            logging.info(f"Successfully fetched and loaded '{file_key}' from S3 that has {len(df)} records.")
            return df
        except Exception as e:
            logging.exception(f"❌ Failed to fetch '{file_key}' from S3: {e}")
            return None