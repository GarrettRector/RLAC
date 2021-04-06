import random
import csv
import pandas as pd
import tflearn
import tensorflow
import numpy
import nltk
import json
import pickle
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
df = pd.read_csv("database.csv")
chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = [0, 1, 0, 1]


def record_response_score(msg, Score, resp):
    df = pd.read_csv("database.csv")
    val = df.loc[(df["parent"] == msg) & (df["child"] == resp), "chance_rank"]
    row = val.to_string(index=False)
    row = int(row)
    df.loc[row, 'chance_rank'] += Score
    df.to_csv(r'database.csv', index=False)


def generate_response(msg):



def get_response(msg):
    df = pd.read_csv("database.csv")
    try:
        hold = (df[df['parent'] == msg].index[0])
        filtered = df[df['parent'] == msg]
        df = filtered[filtered['chance_rank'] == filtered['chance_rank'].max()]
        dfresp = (df["child"])
        return dfresp.to_string(index=False)
    except:
        print("Cannot find", msg, "Epsilon being attempted")
        response = generate_response(msg)
        record_message(msg, response)
        return response


def record_message(message, response):
    with open('database.csv', mode='a') as db:
        writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([message.lower(), response.lower(), '0', '0', '1'])


def choose():
    if (random.randint(0, 100)) < 20:
        return 1
    else:
        return 0


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
    choose = choose()
    if choose == 1:
        generate_response(message)
    else:
        response = get_response(message)
        print("AI:", response)
        score = input('Good response? > ')
        if response is not None:
            if score.lower() == "good":
                record_response_score(message, 1, response)
            elif score.lower() == "bad":
                record_response_score(message, -1, response)
