import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 
import csv


with open('update.csv', 'rb') as f:
    reader = list(csv.reader(f))


reader = reader[1:]
for r in reader:
	r[0] = '2016'
	r[7] = '1'
	r[6] = '1'
	temp=r[1].rstrip()
	r[1]=temp	



data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["Year", "State", "District", "Crop", "Season", "Area(in Hectares)", "Production(in Tonnes)", "Yield"],
                    "Values": reader
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url ="https://ussouthcentral.services.azureml.net/workspaces/8049738fe88d45f58bb4118fdb4c607a/services/0eda4e2671ba4d7683148f4b6eeedb5a/execute?api-version=2.0&details=true"

api_key = 'bA82Pv0ZQJh0QH0lsohys8DJYigm72+g6bZCztm0AoMxPjNANs2PAR5AhHheTQ2NjA7toQbnUqge+xb2jvVkQw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = json.loads(response.read())
    with open('data.txt', 'w') as outfile:
    	json.dump(result, outfile,sort_keys=True, indent=4)
    print (result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))        
    
