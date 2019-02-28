from SmiToText.spacing.mecabSpacing import *
import json
from app.userlog import user_log_write
import os

def mecabspace(text):
    # print(text)
    text_list = text.split( os.linesep )
    result_text_list = []

    for line in text_list:
        result_mecab_spacing = mecabSpacing(line)
        result_text_list.append(result_mecab_spacing)
        user_log_write("mecabspace", line, result_mecab_spacing)

    # print(result_mecab_spacing)

    # return_json_mecab_spacing = {}
    # return_json_mecab_spacing["count"] = len(result_mecab_spacing)
    #
    # for idx, item in enumerate(result_mecab_spacing):
    #
    #     json_item = {}
    #     json_item[item[0]] = item[1]
    #     return_json_mecab_spacing[idx + 1] = json_item


    return '\n'.join(result_text_list)
