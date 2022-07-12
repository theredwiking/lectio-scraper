import json

def saveData(data, week):
    periode = week.replace(" ", "")[3:]
    f = open("./data/%s.txt"%periode, "w")
    f.write(str(data))
    f.close()

def convertToJson(data, arr):
    data_array = data.split('\n')
    arr.append('{"lesson": "%s", "date": "%s", "class": "%s", "teacher": "%s", "room": "%s"}'%(data_array[0], data_array[1], splitString(data_array[2]), splitString(data_array[3]), splitString(data_array[4])))

def splitString(string):
    splitted = string.split(":")
    return splitted[1][1:]