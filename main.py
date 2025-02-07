import json
import re

data=open('data.json',"r")
data=json.load(data)


data[0]['items']['potentials']=[5]*len(data[0]['items']['potentials']) # set potential

ncards=open('cards.html',"r",encoding='UTF-8').read()
r=re.findall(r'info/cards/(\d+)',ncards)
for i in r:
    data[0]['cards'].append( {'id': int(i), 'level': 50, 'master': 0, 'skill': 0, 'ep': 0, 'train': 1, 'art': 1, 'exclude': False})

id=set()
cards=data[0]['cards']
data[0]['cards']=[]
for card in cards:
    if card['id'] not in id:
        data[0]['cards'].append(card)
        id.add(card['id'])
# print(data[0]['cards'])
# exit(0)


data=json.dumps(data)
with open('data.json',"w") as f:
    f.write(data)