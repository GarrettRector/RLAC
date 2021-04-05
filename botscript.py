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
    df = pd.read_csv("database.csv")
    df.combine("parent", "child")

    with open("intents.json") as file:
        data = json.load(file)

    try:
        with open("data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
    except:
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [stemmer.stem(w.lower()) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)

        training = numpy.array(training)
        output = numpy.array(output)

        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)

    tensorflow.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    try:
        model.load("model.tflearn")
    except:
        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save("model.tflearn")

    def bag_of_words(s, word):
        fullbag = [0 for _ in range(len(word))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(word):
                if w == se:
                    fullbag[i] = 1

        return numpy.array(fullbag)

    inp = msg
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
    return random.choice(responses)



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
