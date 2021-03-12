import random
import csv
import pandas as pd
import time
string = input()
parent = string
check = 1
response = 0
child = response
chanceval = 0
num = 0
prob = 1
a = input()
line_request = 0
found = 0
col_list = ['parent', 'child', 'chance_rank', 'time_said', 'chance_boolean']
df = pd.read_csv("database.csv", usecols=col_list)
chancerequest = 0

if string != ():
    check = 1


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


if input() is not None:
    if input().lower() not in ["good", "bad"]:
        with open('database.csv', mode='a') as db_file:
            db = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            db.writerow([parent, child, chanceval, num, prob])


if input() != ():
    line_request = 1

if line_request == 1:
    with open("database.csv") as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if a in line:
                found = found + 1
                line_request = 0
            else:
                line_request = 0

if found == 1:
    if input().lower() not in ["good", "bad"]:
        print("String", f'"{input()}"', "found", f'{found} times')
    else:
        print("Error: Could not find term", input(), "Epsilon will be attempted")

if input().lower() in "good":
    print("Added to Database")
    chancerequest = df("chance_rank") + 1

if input().lower() in "bad":
    print("Added to Database")
    chancerequest = df("chance_rank") - 1
