import csv

#jsonob = {"states":["karnataka":["Mndya"],]}
with open('update.csv', 'rb') as f:
    reader = list(csv.reader(f))


newreader = []
for r in reader:
	temp=r[1].rstrip()
	r[1]=temp
	# newreader.append(r)
print reader[1]
    #for row in reader:
     #   print row