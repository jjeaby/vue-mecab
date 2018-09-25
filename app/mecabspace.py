from SmiToText.spacing.mecabSpacing import *
import json
from app.userlog import user_log_write


def mecabspace(text):
    print(text)
    result_mecab_spacing = mecabSpacing(text)
    print(result_mecab_spacing)

    # return_json_mecab_spacing = {}
    # return_json_mecab_spacing["count"] = len(result_mecab_spacing)
    #
    # for idx, item in enumerate(result_mecab_spacing):
    #
    #     json_item = {}
    #     json_item[item[0]] = item[1]
    #     return_json_mecab_spacing[idx + 1] = json_item

    user_log_write("mecabspace", text, result_mecab_spacing)

    return result_mecab_spacing
