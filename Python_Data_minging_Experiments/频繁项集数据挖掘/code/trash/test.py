import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    data = []
    for item in reader:
        print(item)
        data.append(item)
    print(data)
