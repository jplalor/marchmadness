#Quick and dirty predictor for NCAA Tournament
#John Lalor

import os
import random

def setup():
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
			continue
        
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
	
	
	round1 = { 1:[1,16,33],    2:[8,9,33],    3:[5,12,34],   4:[4,13,34],  5:[6,11,35],  6:[3,14,35],  7:[7,10,36],  8:[2,15,36],
			9:[17,32,37],  10:[24,25,37], 11:[21,28,38],12:[20,29,38],13:[22,27,39],14:[19,30,39],15:[23,26,40],16:[18,31,40],
			17:[33,48,41], 18:[40,41,41], 19:[37,44,42],20:[36,45,42],21:[38,43,43],22:[35,46,43],23:[39,42,44],24:[34,47,44],
			25:[49,64,45], 26:[56,57,45], 27:[53,60,46],28:[52,61,46],29:[54,59,47],30:[51,62,47],31:[55,58,48],32:[50,63,48] }

	round2 = {
	33:[0,0,49],34:[0,0,49],35:[0,0,50],36:[0,0,50],37:[0,0,51],38:[0,0,51],
	39:[0,0,52],40:[0,0,52],41:[0,0,53],42:[0,0,53],43:[0,0,54],44:[0,0,54],
	45:[0,0,55],46:[0,0,55],47:[0,0,56],48:[0,0,56]
	}

	round3 = {
		49:[0,0,57],50:[0,0,57],51:[0,0,58],52:[0,0,58],53:[0,0,59],54:[0,0,59],55:[0,0,60],56:[0,0,60]
	}

	round4 = {
		57:[0,0,61],58:[0,0,61],59:[0,0,62],60:[0,0,62]
	}

	round5 = {
		61:[0,0,63], 62:[0,0,63]
	}
	round6 = { 63:[0,0,64] }
	round7 = {64:[0,0,0]}

	rounds = [round1,round2,round3,round4,round5,round6,round7]
	return teams, rounds, team_stats

def makePick(seed1, seed2):
	population = []
	pick1 = seed1 % 16
	pick2 = seed2 % 16
	if pick1 == 0:
		pick1 = 16
	if pick2 == 0:
		pick2 = 16
	for i in range(17-pick1):
		population.append(seed1)
	for i in range(17-pick2):
		population.append(seed2)
	return random.choice(population)
	
def makePick2(team1, team2):
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
    
    #underdog coefficient
    #seed %16 * rand.range(5,10) (16 if 16 seed)
    t1_underdog = team1 % 16 if team1 < 16 else 16
    t2_underdog = team2 % 16 if team2 < 16 else 16
    
    for k in range(int(t1_underdog)): #  * round(random.randrange(5 * t1_underdog,10*t1_underdog)))):
        names.append(team1)

    for m in range(int(t2_underdog)):#   * round(random.randrange(5*t2_underdog,10*t2_underdog)))):
        names.append(team2)
	return random.choice(names)

def simulateGame(seed1, seed2):
	results = {seed1:0,seed2:0}
	for i in range(100):
		results[makePick2(seed1,seed2)] += 1
	return results[seed1] >= results[seed2]

def simulateRound(roundList, nextRoundList):
	for key in roundList:
		game = roundList[key]
		t1 = game[0]
		t2 = game[1]
		nextGame = game[2]
		isOdd = key%2 == 1
		nextPos = 0 if isOdd == 1 else 1
		if(simulateGame(t1,t2)):
			nextRoundList[nextGame][nextPos] = t1
		else:
			nextRoundList[nextGame][nextPos] = t2
	return nextRoundList


def runSim(rounds, teams, team_stats):
	for i in range(0,len(rounds)-1):
		r = rounds[i]
		nextR = rounds[i+1]
		simulateRound(r,nextR)
	for i in range(len(rounds)-1):
		round = rounds[i]
		for game in round:
			team1 = teams[round[game][0]]
			seed1 = round[game][0] % 16 if round[game][0] % 16 > 0 else 16
			team2 = teams[round[game][1]]
			seed2 = round[game][1] % 16 if round[game][0] % 16 > 0 else 16
			
			print str(game) + ': ' + team1 + ' (' + str(seed1) + ')' + ' vs. ' + team2 + ' (' + str(seed2) + ')'
			nextGame = round[game][2]
			nextPos = 1 if game % 2 == 0 else 0 
			winningTeam = teams[rounds[i+1][round[game][2]][nextPos]]
			winningSeed = rounds[i+1][round[game][2]][nextPos] % 16 if rounds[i+1][round[game][2]][nextPos] % 16 > 0 else 16
			print 'Winner: ' + winningTeam + ' (' + str(winningSeed) + ')'
			print 
	print 'NCAA Winner: ' + teams[rounds[6][64][0]]
	return teams[rounds[6][64][0]]

d = {}
#for z in range(100):
teams, rounds, team_stats = setup()
winner = runSim(rounds, teams, team_stats)
	#if winner in d:
	#	d[winner] += 1
	#else:
	#	d[winner] = 1
#print d