import logging
import os
import uuid

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

resource = boto3.resource(
    "dynamodb",
    region_name="sa-east-1",
    endpoint_url="http://localhost:8000",
    aws_access_key_id=os.environ.get("ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("SECRET_KEY"),
)


class Artists:
    def __init__(self, dyn_resource):
        self.dyn_resource = dyn_resource
        self.table = dyn_resource.Table("Artists")

    def find_one(self, artist_name):
        try:
            response = self.table.query(
                KeyConditionExpression=Key("artistName").eq(artist_name)
            )
        except ClientError as err:
            logger.error(
                "Couldn't get movie %s from table %s. Here's why: %s: %s",
                artist_name,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response["Items"]

    def find_all(self):
        return self.table.scan()["Items"]

    def save(self, artist_name):
        id = uuid.uuid4().hex
        try:
            self.table.put_item(
                Item={
                    "id": id,
                    "artistName": artist_name,
                }
            )
            return id
        except ClientError as err:
            logger.error(
                "Couldn't add movie %s to table %s. Here's why: %s: %s",
                artist_name,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise


def create_artist_table(resource):
    table_name = "Artists"
    try:
        resource.create_table(
            TableName=table_name,
            KeySchema=[
                {"AttributeName": "artistName", "KeyType": "HASH"},
                {"AttributeName": "id", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"},
                {"AttributeName": "artistName", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
    except ClientError as err:
        logger.error(
            "Couldn't create table %s. Here's why: %s: %s",
            table_name,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )


def init_app():
    create_artist_table(resource)
