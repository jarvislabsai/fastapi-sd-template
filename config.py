from dataclasses import dataclass

#AWS Creds
@dataclass
class AWSConfig:
    aws_access_key_id = '****************'
    aws_secret_access_key = '****************'
    bucket_name = '****************'