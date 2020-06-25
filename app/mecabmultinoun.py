from SmiToText.find.extract_mecab_multi_noun import extract_multi_noun
from app.userlog import user_log_write
import re

def mecabextractmultinoun(text):

    result_text_list = {}
    text = text.replace('\n', ' ')
    text = re.sub("[\s]+", " ", text)

    _, result_mecab_multi_noun = extract_multi_noun(text)
    result_text_list.update(result_mecab_multi_noun)
    user_log_write("mecabextractmultinoun", text, result_mecab_multi_noun)

    print("mecabextractmultinoun : ", result_text_list)

    return list(result_text_list)
