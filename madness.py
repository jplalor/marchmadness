# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:06:23 2015

@author: JLALOR
"""

import sqlite3
import os
import random

os.chdir('C:\Users\jlalor\Documents\marchmadness')


infile = open('schoolstats.csv')

working_stats = infile.readlines()

infile.close()

stats = []

team_stats = {}

for line in working_stats:
    l = line.split(',')    
    try:
        int(l[0])
        stats.append(l)
    except:
        print 'line skipped'
        

for line  in stats:
    team_name = line[1]
    srs_score = line[6]
    team_stats[team_name] = float(srs_score)


teams = {
    1: 'Kentucky',
    2: 'Kansas',
    3: 'Notre Dame',
    4:'Maryland',
    5:'West Virginia',
    6:'Butler',
    7:'Wichita State',
    8:'Cincinnati',
    9:'Purdue',
    10:'Indiana',
    11:'Texas',
    12:'Buffalo',
    13:'Valparaiso',
    14:'Northeastern',
    15:'New Mexico State',
    16:'Manhattan',
    17:'Wisconsin',
    18:'Arizona',
    19:'Baylor',
    20:'North Carolina',
    21:'Arkansas',
    22:'Xavier',
    23:'Virginia Commonwealth',
    24:'Oregon',
    25:'Oklahoma State',
    26:'Ohio State',
    27:'Mississippi',
    28:'Wofford',
    29:'Harvard',
    30:'Georgia State',
    31:'Texas Southern',
    32:'Coastal Carolina',
    33:'Villanova',
    34:'Virginia',
    35:'Oklahoma',
    36:'Louisville',
    37:'Northern Iowa',
    38:'Providence',
    39:'Michigan State',
    40:'North Carolina State',
    41:'Louisiana State',
    42:'Georgia',
    43:'Boise State',
    44:'Wyoming',
    45:'California-Irvine',
    46:'Albany (NY)',
    47:'Belmont',
    48:'Lafayette',
    49:'Duke',
    50:'Gonzaga',
    51:'Iowa State',
    52:'Georgetown',
    53:'Utah',
    54:'Southern Methodist',
    55:'Iowa',
    56:'San Diego State',
    57:'St. John\'s (NY)',
    58:'Davidson',
    59:'UCLA',
    60:'Stephen F. Austin',
    61:'Eastern Washington',
    62:'Alabama-Birmingham',
    63:'North Dakota State',
    64:'North Florida'
}

for team in teams:
    print team_stats[teams[team]]
    
def simulateGame(team1, team2):
    team_name1 = teams[team1]
    team_name2 = teams[team2]
    srs1 = int(abs(round(team_stats[team_name1])))
    srs2 = int(abs(round(team_stats[team_name2])))
    names = []
    #srs scores    
    for i in range(srs1):
        names.append(team1)
    for j in range(srs2):
        names.append(team2)
    return random.choice(names)

    #underdog coefficient
    #seed %16 * rand.range(5,10) (16 if 16 seed)
    t1_underdog = team1 % 16 if team1 < 16 else 16
    t2_underdog = team2 % 16 if team2 < 16 else 16
    
#    for k in range(t1_underdog * int(round(random.range(5,10)))):
#        names.append(team_name1)
#
#    for m in range(t2_underdog * int(round(random.range(5,10)))):
#        names.append(team_name2)
    
    for k in range(t1_underdog):
        names.append(team_name1)

    for m in range(t2_underdog):
        names.append(team_name2)


winner = {1:0,17:0}
for z in range(1000):    
    winner[simulateGame(1,17)] +=1
print winner


