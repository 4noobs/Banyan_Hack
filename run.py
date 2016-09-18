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


@app.route('/')
def index():
    print "sumthin happened"

   
    return render_template('index.html')

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
  with open('update.csv', 'rb') as f:
      reader = list(csv.reader(f))


  # newreader = []
  for r in reader:
    temp=r[1].rstrip()
    r[1]=temp
    
  aux = []
  params = []
  param = []
  """[
              [
               year,
                state,
                district,
                crop,
                season,
                "1000",
                "1000",
                "1"
              ],
              
            ]"""
  #for state in states:
  for state in range(2016,2017):
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
            "Values":reader
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
          result = result['Results']['output1']['value']['Values'][0][8]
          #print(result) 
    except urllib2.HTTPError, error:
          print("The request failed with status code: " + str(error.code))

          # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
          print(error.info())
          result = json.loads(error.read())
          print(json.loads(error.read()))
    print type(result)
    #return result
    #res = [(str(state)),float(str(result))]
    #aux.append(res)
  #print res, type(res)
  return result
  return render_template('test1.html',**locals())






if __name__ == '__main__':
    app.run(debug= True,host='0.0.0.0',port=81)
