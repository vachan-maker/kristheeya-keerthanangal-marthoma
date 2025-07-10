import json
for i in range(1,505):
    with open(f'kristheeya_keerthanagal/{i}.txt','r',encoding='utf-8') as file:
        lyrics = file.read()
        with open(f'kristheeya_keerthanagal/json/{i}.json','w') as jsonfile:
            json.dump({"songNumber":i,"lyrics":lyrics},jsonfile,indent=4,ensure_ascii=False)