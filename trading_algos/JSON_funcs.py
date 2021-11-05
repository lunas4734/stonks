def save_json (dictionary, json_local, file_name):
    import json
    json.dump(dictionary, open(json_local + file_name + ".json", "w"))