import random
def makeTheTeam(players,size):
    playerTeams = []
    index = 0
    while(index < len(players)):
        playerTeams.append(players[index:index+size])
        index = index+size
    
    return playerTeams


someList = ["Cristiano","Messi","Lampard","Araguniz","Drogba","Chettri","Gurpreet Singh","Livingston"]
random.shuffle(someList)

print(someList)
print(makeTheTeam(someList,3))