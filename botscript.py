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


def record_response_score(message, score):
    df = pd.read_csv("database.csv")
    datarow = (df[df['parent'] == message].index[0])
    filtered_df = df[df['parent'].str.contains(message, na=False)]
    row = filtered_df.index[0]
    print(datarow)
    print(row)
    print(df)
    if datarow == row:
        df.iloc[datarow, 2] += score
    print(df)
    df.to_csv(r'database.csv', index=False)


def get_response(message):
    df = pd.read_csv("database.csv")
    df = pd.DataFrame(df, columns=['parent'])
    getresponse = df.loc[df['parent'].str.match(message, case=False)]
    for getresponse in df:
        responses = {getresponse}
        df2 = pd.DataFrame(responses)
        print(df2)

def record_message(message):
    pass


if input().lower == "good":
    print("Added to Database")
    chancerequest = df("chance_rank") + 1

if input().lower == "bad":
    print("Added to Database")
    chancerequest = df("chance_rank") - 1


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
    response = get_response(message)
    print(response)
    score = input('Good? >')
    if score == "good":
        record_response_score(response, 1)
    elif score == "bad":
        record_response_score(response, -1)
    else:
        record_response_score(response, -0.1)
