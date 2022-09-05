import random
import json
import pickle
import datetime
import csv

class Data(object):
    def __init__(self):
        self.date = str(datetime.datetime.now()).split()[0]
        self.daily = 0
        self.total = 0

def main() -> None:
    """Random dict :D"""
    f = open("todo.txt", "r")
    with open('dict.json') as json_file:
        dict = json.load(json_file)
    sum = 0
    for line in f:
        if line[0] == "#":
            continue
        if line in dict.keys():
            dict[line] += 1
        else:
            dict[line] = 1
        sum += dict[line]
    choice = random.random()*sum
    chosenTask = "Default"
    f = open("todo.txt", "r")
    for line in f:
        if line[0] == "#":
            continue
        print(f"The task {line[:-1]} had a {100*dict[line]/sum}% chance of being selected.")
        choice -= dict[line]
        if choice < 0 and chosenTask == "Default":
            chosenTask = line
    print(f"{chosenTask[:-1]} was selected!")
    del dict[chosenTask]

    jdict = json.dumps(dict)

    # open file for writing, "w"
    f = open("dict.json","w")

    # write json object to file
    f.write(jdict)

    # close file
    f.close()
    try:
        data = load_object("data.txt")
        print("hi")
    except:
        data = Data()
    data.total += 1
    if data.date == str(datetime.datetime.now()).split()[0]:
        data.daily += 1
    else:
        append_csv(data)
        data.date = str(datetime.datetime.now()).split()[0]
        data.daily = 1

    save_object(data, "data.txt")
    print(f"You have complete {data.daily} tasks today and {data.total} since this code broke!")


def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    with open(filename, 'rb') as inp:
        data = pickle.load(inp)
        return data

def append_csv(data):
    with open('calendar.csv','a') as fd:
        myCsvRow = [data.date, data.daily]
        fd.write(myCsvRow)

if __name__ == "__main__":
    main()
