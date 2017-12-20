import math
import pandas as pd
import Lab_4

user_num = Lab_4.user_num
context = pd.read_csv("context.csv", sep=",", skiprows=[0], header=None)
arr_Weekend = [" Sat", " Sun"]
check = True
resMovie = ''

#Находим список фильмов, которые вероятнее просмотреть в будни
FilmsWeekday = []
for i in Lab_4.arr_Films:
    probWeekday = 0
    probWeekend = 0
    count = 0
    for x in range(0,40):
        if x != user_num - 1:
            if context[i][x] != " -":
                count += 1
                if context[i][x] in arr_Weekend:
                    probWeekend += 1
                else:
                    probWeekday += 1
    if (probWeekday /count) > (probWeekend / count):
        FilmsWeekday.append(i)


#Находим фильм, который подойдет пользователю в будний день
for x in Lab_4.Result:
    if x[0] in FilmsWeekday and (x[1] - Lab_4.arr_Averages[user_num - 1]) > 0 and check:
        check = False
        resMovie = x[0]

if not check:
    print("Your recommend movie: ", resMovie)
else:
    print("Sorry, we can not find a movie for you")