from datetime import datetime, timedelta
from math import log
import sys

def seconds_since(date):
    td = date - datetime(2016, 10, 30) #somewhere near the time when site goes live
    return td.days * 86400 + td.seconds


def hotness(likes, dlikes,submissions, date):

    score = likes - (dlikes/1.5) + 10*submissions #submissions also judge , how many people are able to contribute in a post the more is this number the more likly it is , that our new user will find it interesting and may want to add hit own subbmissions , the early he submits something, he will find himself more engaged in our forum

    union = likes+dlikes # becuase 50000-50000 is a hotter topic than 10-2 in that too when the two in comparison have the same age
    
    return  log(max(abs(score), 1), 10)*log(max(union,1),10)  -  seconds_since(date)/ 45000

arg=sys.argv
print(hotness(int(arg[1]),int(arg[2]),int(arg[3]),datetime(int(arg[6]),int(arg[5]),int(arg[4]))))# likes dlikes submissions dd mm yyyy