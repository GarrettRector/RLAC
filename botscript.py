import random
import csv
import pandas as pd
# child is response. Link to response with Epsilon Greed policy later
child = 0
chanceval = 0
num = 0
prob = 1
line_request = 0
df = pd.read_csv("database.csv")
chancerequest = 0
chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = [0, 1, 0, 1]

def line_find(message):
    df = pd.read_csv("database.csv")
    filtered_df = df[df['parent'].str.contains(message, na=False)]
    return filtered_df.index[0]


def record_response_score(message, score, response):
    df = pd.read_csv("database.csv")
    val = df.loc[(df["parent"] == message) & (df["child"] == response), "chance_rank"]
    row = (val.to_string(index=False))
    print(row)
    df.loc[row, "chance_rank"] += score
    df.to_csv(r'database.csv', index=False)


def get_response(msg):
    df = pd.read_csv("database.csv")
    try:
        hold = (df[df['parent'] == msg].index[0])
        filtered = df[df['parent'] == msg]
        df = filtered[filtered['chance_rank'] == filtered['chance_rank'].max()]
        dfresp = (df["child"])
        return dfresp.to_string(index=False)
    except:
        print("Cannot find", msg)


def record_message(message):
    pass


def addchance(message):
    if message.lower == "good":
        print("Added to Database")
        return df("chance_rank") + 1

    if message.lower == "bad":
        print("Added to Database")
        return df("chance_rank") - 1


def explore():
    return random.choice(chance)


def exploit():
    return values.index(max(values))


def choose():
    if (random.randint(0, 100)) > 10:
        return values.index(max(values))
    else:
        return random.choice(chance)


def read_data():
    found = 0
    with open("database.csv") as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if message in line:
                found = found + 1
                if message.lower not in ["good", "bad"]:
                    if message > found-1:
                        print("String", f'"{message}"', "found", f'{found} times')
                    else:
                        print("Error: Could not find term", message, "Epsilon will be attempted")


while True:
    message = input('> ')
    record_message(message)
    response = get_response(message)
    print("AI:", response)
    score = input('Good response? > ')
    if score.lower() == "good":
        record_response_score(message, 1, response)
    elif score.lower() == "bad":
        record_response_score(message, -1, response)
    else:
        record_response_score(message, -0.1, response)
