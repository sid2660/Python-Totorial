from csv import reader

with open("Read.csv","r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        print(row)