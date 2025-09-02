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
        self.BUCKET_NAME = os.getenv("BUCKET_NAME")
        aws_access_key = os.getenv("ACCESS_KEY_ID")
        aws_secret_key = os.getenv("SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION", "us-east-1")

        if not all([self.BUCKET_NAME, aws_access_key, aws_secret_key, aws_region]):
            raise ValueError("❌ Missing one or more AWS credentials in .env file")

        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )
        logging.info("✅ S3 connection initialized")