import random
import csv
import pandas as pd
import multiprocessing as mp
# child is response. Link to response with Epsilon Greed policy later
child = 0
chanceval = 0
num = 0
prob = 1
line_request = 0
found = 1
col_list = ['parent', 'child', 'chance_rank', 'time_said', 'chance_boolean']
df = pd.read_csv("database.csv", usecols=col_list)
chancerequest = 0


def writer():
    if input().lower() not in ["good", "bad"]:
        with open('database.csv', mode='a') as db_file:
            db = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            db.writerow([input(), child, chanceval, num, prob])
            print("works")


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    p = ctx.Process(target=writer)
    p.start()
    print("test")
    p.join()


print("works")
if input().lower == "good":
    print("Added to Database")
    chancerequest = df("chance_rank") + 1

if input().lower == "bad":
    print("Added to Database")
    chancerequest = df("chance_rank") - 1


if input() is not None:
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


with open("database.csv") as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:
        if input() in line:
            found = found + 1

if input().lower not in ["good", "bad"]:
    print("String", f'"{input()}"', "found", f'{found} times')
else:
    print("Error: Could not find term", input(), "Epsilon will be attempted")
