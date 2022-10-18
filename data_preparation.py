import os
import json

base_path = "/home/u.tanielian/mytheresa_dalle_format"
list_files = os.listdir(base_path)
dict_files = dict()
output_file = open("./metadata.jsonl", 'w', encoding='utf-8')

for elem in list_files:
    base_elem = elem.split(".")[0]
    
    if base_elem in dict_files:
        if elem.endswith("jpg"):
            dict_files[base_elem]["image"] = elem
        else:
            f = open(os.path.join(base_path, elem), "r")
            text_content = f.read()
            dict_files[base_elem]["text"] = text_content
    else:
        dict_files[base_elem] = dict()
        if elem.endswith("jpg"):
            dict_files[base_elem]["image"] = elem
        else:
            f = open(os.path.join(base_path, elem), "r")
            text_content = f.read()
            dict_files[base_elem]["text"] = text_content

for elem in dict_files.keys():
    dic = {"file_name": dict_files[elem]["image"], "text": dict_files[elem]["text"]}
    json.dump(dic, output_file) 
    output_file.write("\n")