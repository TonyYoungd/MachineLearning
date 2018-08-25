import csv
with open("data1","r") as csvFile:
    reader = csv.reader(csvFile)
    data = []
    for item in reader:
        data.append(item)
