import csv

# csv.reader(f)
with open('example.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line[1])

# csv.DictReader(f)
with open('example.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line['Country'])

# csv.writer(f)
with open('sample.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(['value1', 'value2'])
    writer.writerow(['value3', 'value4'])

# csv.Dictwriter(f)
with open('sample.csv', mode='w') as f:
    writer = csv.DictWriter(f, ['col1', 'col2'])
    writer.writeheader() # headerを定義する
    writer.writerow({'col1': 'value1', 'col2': 'value2'})
    writer.writerow({'col1': 'value3', 'col2': 'value4'})