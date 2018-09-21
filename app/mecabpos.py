from SmiToText.tokenizer.mecab import *
import json


def mecabpos(text):
    result_mecab_spacing = mecabAnalize(text)

    return_json_mecab_spacing = {}
    return_json_mecab_spacing["count"] = len(result_mecab_spacing)

    for idx, item in enumerate(result_mecab_spacing):

        json_item = {}
        json_item[item[0]] = item[1]
        return_json_mecab_spacing[idx + 1] = json_item


    return return_json_mecab_spacing
