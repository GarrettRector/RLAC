import random
import csv
string = str(input())
parent = input(string)
response = 0
child = response
chanceval = 0
num = 0
prob = 1
a = parent
line_request = 0
open("database.csv")

chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = [0, 1, 0, 1]


def explore():
    return random.choice(chance)


def exploit():
    return values.index(max(values))


def choose():
    if (random.randint(0, 100)) > 10:
        return values.index(max(values))
    else:
        return random.choice(chance)


print(choose())

# basic writer
with open('database.csv', mode='a') as db_file:
    fieldnames = ['parent', 'child', 'chance_rank', 'time_said', 'chance_boolean']
    db = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if parent != ('Good', 'good', 'Bad', 'bad'):
        db.writerow([parent, child, chanceval, num, prob])

# basic reader
with open('database.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')


if line_request == 1:
    with open("database.csv") as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            print(line)
            if a in line:
                print("String found in first row of csv")
                line_request = 0
            else:
                print("Error: Term", parent, "Not found. Line not printed.",
                      "Epsilon will be attempted.")
                line_request = 0
