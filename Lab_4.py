import math
import requests as req
import json
import pandas as pd

user_num = 23
k = 5
data = pd.read_csv("data.csv", sep=",", skiprows=[0], header=None)

def Sim_Finder(I, J):
    sum = 0
    sum_sqrtI = 0
    sum_sqrtJ = 0
    for i in range(1, 31):
        if data[i][I] != -1 and data[i][J] != -1:
            sum += data[i][I] * data[i][J]
            sum_sqrtI += pow(data[i][I], 2)
            sum_sqrtJ += pow(data[i][J], 2)
    return round((sum / (math.sqrt(sum_sqrtI) * math.sqrt(sum_sqrtJ))), 2)


def Get_Metrics():
    metric = {}
    for i in range(40):
        if i != user_num - 1:
            metric.update({(i + 1): Sim_Finder(user_num - 1, i)})
    return sorted(metric.items(), key=lambda x: x[1], reverse=True)

def Finding_k_Users(Similarity):
    arr_k = []
    for i in range(k):
        arr_k.append(Similarity[i][0])
    return arr_k

def Get_Films():
    cur_Films = []
    for i in range(1, 31):
        if data[i][user_num - 1] == -1:
            cur_Films.append(i)
    return cur_Films

def Get_Average():
    arrAver = []
    for j in range(0, 40):
        average = 0
        count = 0
        for i in range(1, 31):
            if data[i][j] != -1:
                average += data[i][j]
                count += 1
        arrAver.append(round((average / count), 3))
    return arrAver

def Get_Result(Simularity, K_Users, cur_Films, Average):
    result = {}
    for i in cur_Films:
        res = 0
        nominator = 0
        denominator = 0
        for j in K_Users:
            if data[i][j - 1] != -1:
                nominator += Simularity[j][1] * (data[i][j - 1] - Average[j - 1])
                denominator += abs(Simularity[j][1])
        res = round((Average[user_num - 1] + nominator / denominator), 3)
        result.update({i: round(res, 3)})
    return result


arr_Sim = Get_Metrics()
arr_k_Users = Finding_k_Users(arr_Sim)
arr_Films = Get_Films()
arr_Averages = Get_Average()
res_Movies = Get_Result(arr_Sim, arr_k_Users, arr_Films, arr_Averages)


Result = sorted(res_Movies.items(), key=lambda x: x[0], reverse=False)
Str=''
for i in Result:
    str1 = '"movie ' +str(i[0])+ '":'+ str(round(i[1],2))+', '
    Str+=str1
print (Str[0:len(Str)-2])

url = 'https://cit-home1.herokuapp.com/api/rs_homework_1'
headers = {'content-type': 'application/json'}
Data = json.dumps({'user': 23, '1':{"movie 3":2.65, "movie 6":2.94, "movie 7":3.34, "movie 9":2.82, "movie 21":4.08, "movie 22":3.0, "movie 26":4.18}})
r = req.post(url, data=Data, headers=headers)
print(r)
print(r.json())