import json
with open('remarkk.json','r',encoding='utf8') as fp:
    json_data1 = json.load(fp)
with open('remar.json','r',encoding='utf8') as fp:
    json_data2 = json.load(fp)
json_data=json_data1+json_data2
with open('remarks.json', 'w', encoding='UTF-8') as f:
    json.dump(json_data, f, ensure_ascii=False)