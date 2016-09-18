import urllib2
import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
app = Flask(__name__)
# If you are using Python 3+, import urllib instead of urllib2

import json 


url = 'https://ussouthcentral.services.azureml.net/workspaces/8049738fe88d45f58bb4118fdb4c607a/services/7c088f03d34a4b93bd06a56b9d95db33/execute?api-version=2.0&details=true'
url ="https://ussouthcentral.services.azureml.net/workspaces/8049738fe88d45f58bb4118fdb4c607a/services/0eda4e2671ba4d7683148f4b6eeedb5a/execute?api-version=2.0&details=true"

api_key = 'bA82Pv0ZQJh0QH0lsohys8DJYigm72+g6bZCztm0AoMxPjNANs2PAR5AhHheTQ2NjA7toQbnUqge+xb2jvVkQw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

states = ['WEST BENGAL', 'MANIPUR', 'State', 'TRIPURA', 'PUNJAB', 'SIKKIM', 'CHANDIGARH', 'UTTARANCHAL', 'GOA', 'HIMACHAL PRADESH', 'PONDICHERRY', 'BIHAR', 'MADHYA PRADESH', 'D & N HAVELI', 'RAJASTHAN', 'MIZORAM', 'ARUNACHAL PRADESH', 'A & N ISLANDS', 'CHHATTISGARH', 'ORISSA', 'MEGHALYA', 'ASSAM', 'JHARKHAND', 'JAMMU & KASHMIR', 'TAMIL NADU', 'MAHARASHTRA', 'GUJARAT', 'DELHI', 'ANDHRA PRADESH', 'NAGALAND', 'HARYANA', 'KERALA', 'KARNATAKA', 'UTTAR PRADESH']


'''@app.route('/result',methods=['POST','GET'])
def result():

  return render_template('')'''


@app.route('/')
def index():
    print "sumthin happened"

   
    return render_template('index.html')

@app.route('/chartest')
def chartest():
    print "sumthin happened"

   
    return render_template('charttest.html')

@app.route('/state',methods=['POST','GET'])
def state():
        

  dict_states={}
  count_states={}
  with open('data.json', 'r') as read_file:
      list_json=json.load(read_file)
  # print list_json['Results']['output1']['value']['Values']
  for l in list_json['Results']['output1']['value']['Values']:
      dict_states[str(l[1])]=0.0
      count_states[l[1]]=0
      # print dict_states[l[1]]

  for l in list_json['Results']['output1']['value']['Values']:
      dict_states[str(l[1])]=dict_states[str(l[1])]+float(l[8])
      count_states[l[1]]=count_states[l[1]]+1
  list_state=list(dict_states)

  newlist = []
  for i in list_state:
    temp = str(i)
    newlist.append(temp)
  print newlist
  # print dict_states
  # print list_state
  for l in newlist:
      dict_states[l]=dict_states[l]/count_states[l]
      if  dict_states[l] < 0:
         dict_states[l] = 0
  dictlist = []
  for key, value in dict_states.items():
    temp = [key,value]
    dictlist.append(temp)
  res = dictlist
  return render_template('chart.html',**locals())

@app.route('/chart',methods=['POST','GET'])
def chart():
    print "sumthin happened"
    select = request.form['chart']
    count_districts={}
    dict_temp={}
    dict_state_district={}
    dict_districts={}
    list_district=[]
    state=select
    with open('data.json', 'r') as read_file:
        list_json=json.load(read_file)
    # print list_json['Results']['output1']['value']['Values']
    for l in list_json['Results']['output1']['value']['Values']:
        if l[1] in state:
            dict_districts[l[2]]=0.0
            count_districts[l[2]]=0
        # print dict_states[l[1]]
    # list_district=[]
    for l in list_json['Results']['output1']['value']['Values']:
        if l[1] in state:
            dict_districts[l[2]]=dict_districts[l[2]]+float(l[8])   
            # dict_state_district[l[1]].append(dict_districts)
            # dict_temp={l[2]:float(l[8])}
            # list_district.append(dict_temp)
            count_districts[l[2]]=count_districts[l[2]]+1
    # print list_district
    list_district=list(dict_districts)

    for l in list_district:
        dict_districts[l]=dict_districts[l]/count_districts[l]

    # for l in list_json['Results']['output1']['value']['Values']:
        # dict_districts[l[1]]=[dict_districts[l[2]],]

    

    list_temp=[]
    list_state_district=[]
    # dict_state_district={}
    for l in list_district:
        list_temp.append(str(l))
        list_temp.append(dict_districts[l])
        list_state_district.append(list_temp)
        dict_state_district
        list_temp=[]
    print list_state_district

    res = list_state_district

    print select

   
    return render_template('chart.html',**locals())

@app.route('/district', methods=['POST','GET'])
def district():
  states = ['WEST BENGAL', 'MANIPUR', 'State', 'TRIPURA', 'PUNJAB', 'SIKKIM', 'CHANDIGARH', 'UTTARANCHAL', 'GOA', 'HIMACHAL PRADESH', 'PONDICHERRY', 'BIHAR', 'MADHYA PRADESH', 'D & N HAVELI', 'RAJASTHAN', 'MIZORAM', 'ARUNACHAL PRADESH', 'A & N ISLANDS', 'CHHATTISGARH', 'ORISSA', 'MEGHALYA', 'ASSAM', 'JHARKHAND', 'JAMMU & KASHMIR', 'TAMIL NADU', 'MAHARASHTRA', 'GUJARAT', 'DELHI', 'ANDHRA PRADESH', 'NAGALAND', 'HARYANA', 'KERALA', 'KARNATAKA', 'UTTAR PRADESH']

  return render_template('district.html',**locals())

@app.route('/field', methods=['POST','GET'])
def field():
  state = request.form['state'].upper()
  district = request.form['district'].upper()
  year = request.form['year']
  season = request.form['season']
  crop = request.form['crop']
 
  processed_text = state.upper() + district + season
  import csv

  #jsonob = {"states":["karnataka":["Mndya"],]}
  '''with open('update.csv', 'rb') as f:
      reader = list(csv.reader(f))


  # newreader = []
  for r in reader[1:4]:
    temp=r[1].rstrip()
    r[1]=temp'''
    
  
  #for state in states:
  for i in range(2016,2017):
    data =  {
        "Inputs": {
          "input1": {
            "ColumnNames": [
              "Year",
              "State",
              "District",
              "Crop",
              "Season",
              "Area(in Hectares)",
              "Production(in Tonnes)",
              "Yield"
            ],
            "Values":[[year,state,district,crop,season,"1000","1000","1"],]
          }
        },
        "GlobalParameters": {}
      }

  

    body = str.encode(json.dumps(data))
    req = urllib2.Request(url, body, headers) 
    #print body
      

    try:
          response = urllib2.urlopen(req)

          # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
          # req = urllib.request.Request(url, body, headers) 
          # response = urllib.request.urlopen(req)

          result = json.loads(response.read())
          print result
          result = result['Results']['output1']['value']['Values'][0][8]
          print(result) 
    except urllib2.HTTPError, error:
          print("The request failed with status code: " + str(error.code))

          # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
          print(error.info())
          result = json.loads(error.read())
          print(json.loads(error.read()))
    print type(result)
    #return result
    #es = [[(str('name')),float(str('1.1'))], [(str('blah')),float(str('10'))]]
    #aux.append(res)
  #print res, type(res)
  #return result
  return render_template('result.html',**locals())






if __name__ == '__main__':
    app.run(debug= True,host='0.0.0.0',port=81)
