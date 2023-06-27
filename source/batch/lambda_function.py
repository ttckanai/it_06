# coding : utf-8
import boto3
import json
import util

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    table_name = "ChatHistory" # 正しいテーブル名？
    filter = {}
    # filter = {
    #     "Username":{
    #         "AttributeValueList":[{
    #             "S":event["Username"]}],
    #         "ComparisonOperator": "EQ"
    #     },
    #     "Tag":{
    #         "AttributeValueList":[{
    #             "S":event["Tag"]}],
    #         "ComparisonOperator": "EQ"
    #     }
    # }
    res = dynamodb.scan(TableName=table_name, ScanFilter=filter)
    items = res["Items"]
    docs = []
    s3 = boto3.client("s3")
    bucket_name = "lambda-functions-ttckanai" # 正しいテーブル名？
    for item in items:
        attr = {}
        filename = "token"
        for k,v in item.items():
            attr[k] = v["S"]
            if k != "Text":
                filename += "_"+v["S"]

        filename += ".json"
        attr["tokens"] = util.tokenize(attr["Text"])
        data = json.dumps(attr).encode("utf-8")
        s3.put_object(Body=data, Bucket=bucket_name, Key=filename)

    return 
