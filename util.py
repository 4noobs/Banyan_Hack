'''import json
with open('data.json','rb') as f:
		f = json.loads(f.read())
		print type(f)


#for l in f:
f = f['Results']['output1']['value']['Values'][0][8]
print f'''

import os
import json

dict_states={}
count_states={}
with open('data.json', 'r') as read_file:
    list_json=json.load(read_file)
# print list_json['Results']['output1']['value']['Values']
for l in list_json['Results']['output1']['value']['Values']:
    dict_states[l[1]]=0.0
    count_states[l[1]]=0
    # print dict_states[l[1]]

for l in list_json['Results']['output1']['value']['Values']:
    dict_states[l[1]]=dict_states[l[1]]+float(l[8])
    count_states[l[1]]=count_states[l[1]]+1
list_state=list(dict_states)
# print dict_states
# print list_state
for l in list_state:
    dict_states[l]=dict_states[l]/count_states[l]
print dict_states
# print dict_states[0]
# for l in list_json['Results']['output1']['value']['Values']:
    # dict_states[l[1]]=dict_states[l[1]]/count_states[l[1]]
# print dict_states 
