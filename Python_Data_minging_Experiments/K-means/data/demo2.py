import csv
with open("../data/data1.csv") as datac:
    reader = csv.reader(datac)
    data = []
    for item in reader:
        data.append(item)
    for example in data:
        for index in range(len(example)):
            example[index] = float(example[index])
    print(data)