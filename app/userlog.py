from SmiToText.util.util import Util
import json
import os
import datetime

util = Util()


def user_log_write(type, source, target):
    now_date = datetime.datetime.now().strftime("%y%m%d")

    root_path = util.getRootPath("app.userlog")
    log_file = root_path + os.path.sep + "log" + os.path.sep + type + "-log_" + now_date + ".txt"



    log_sentence = {}
    log_sentence["type"] = type
    log_sentence["source"] = source
    log_sentence["target"] = target
    log_sentence["date"] = str(datetime.datetime.now())
    log_sentence_json = json.dumps(log_sentence, ensure_ascii=False, indent=4)

    print(log_sentence_json)

    write_log = open(log_file, mode="a", encoding="utf-8")
    write_log.writelines(log_sentence_json + os.linesep)
    write_log.close()
