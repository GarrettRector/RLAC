import random
import csv
import asyncio
import pandas as pd
import aiofiles
from aiocsv import AsyncReader, AsyncWriter
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
message = input()


async def reader():
    async with aiofiles.open("database.csv", mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncReader(afp):
            print(row)  # row is a list


async def writer():
    async with aiofiles.open("database.csv", mode="a", encoding="utf-8", newline="") as afp:
        asyncwriter = AsyncWriter(afp, dialect="unix")
        await asyncwriter.writerow([input(), child, chanceval, num, prob])
        await asyncwriter.writerows([
            [input(), child, chanceval, num, prob]
        ])


def record_message(message):
    async with aiofiles.open("database.csv", mode="a", encoding="utf-8", newline="") as afp:
        asyncwriter = AsyncWriter(afp, dialect="unix")
        await asyncwriter.writerow([message, child, chanceval, num, prob])
        await asyncwriter.writerows([
            [message, child, chanceval, num, prob]
        ])

def record_response_score(message, score):
    

def generate_response(message):


asyncio.run(reader())

if input().lower == "good":
    print("Added to Database")
    chancerequest = df("chance_rank") + 1

if input().lower == "bad":
    print("Added to Database")
    chancerequest = df("chance_rank") - 1


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
    if input() > found-1:
        print("String", f'"{input()}"', "found", f'{found} times')
    else:
        print("Error: Could not find term", input(), "Epsilon will be attempted")

while True:
    message = input('>')
    record_message(message)
    response = generate_response(message)
    print(response)
    score = input('Good? >')
    if score == "good":
        record_response_score(response, 1)
    else:
        record_response_score(response, -1)
