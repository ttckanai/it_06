# coding: utf-8
import util

def lambda_handler(event, context):
    janome_version = util.get_janome_version()
    text = "明日天気になあれ。"
    tokens = util.tokenize(text)
    result = {"janome_version":janome_version,
              "input_text":text,
              "tokens":tokens}
    response = {
        "result":result
    }
    return response