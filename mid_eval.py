import csv
import os
import sys

class PlayerInfo():
    def __init__(self, playerId, hp, xp, classType):
        self.playerId = playerId
        self.hp = hp
        self.xp = xp
        self.classType = classType

    def changeHP(self):
        amount = input("Enter amount by which you want to change HP: ")
        newHP = self.hp+int(amount)
        if newHP > 100:
            newHP = 100
        if newHP < 0:
            newHP = 0
        self.hp = newHP

    def changeXP(self):
        amount = input("Enter amount by which you want to change XP: ")
        newXP = self.xp+int(amount)
        if newXP > 100000:
            newXP = 100000
        if newXP < 0:
            newXP = 0
        self.xp = newXP

    def printStats(self):
        print("Id: " + self.playerId)
        print("HP: " + str(self.hp))
        print("XP: " + str(self.xp))
        print("Class: " + self.classType)

details = {}
filepath = os.path.join(sys.path[0], "details.csv")
if os.path.exists(filepath):
    with open(filepath,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            details[line[0]] = PlayerInfo(line[0], int(line[1]), int(line[2]), line[3])

playerId = input("Enter player id: ")
playerInfo = None
if playerId in details:
    playerInfo = details[playerId]
else:
    playerClass = None
    while True:
        c = input("Please choose a class:\n1.Warrior\n2.Archer\n3.Mage\n")
        if c == "1": 
            classType = "Warrior"
            break
        elif c == "2":
            classType = "Archer"
            break
        elif c == "3":
            classType = "Mage"
            break
    playerInfo = PlayerInfo(playerId, 100, 0, classType)
    details[playerId] = playerInfo

while True:
    action = input("1.Change HP\n2.Change XP\n3.Get current stats\n4.Exit\n")
    if action == "1": 
        playerInfo.changeHP()
    elif action == "2":
        playerInfo.changeXP()
    elif action == "3":
        playerInfo.printStats()
    elif action == "4":
        break

with open(filepath, 'w') as csv_file:
    for playerId, playerInfo in details.items():
        csv_file.write(playerId + "," + str(playerInfo.hp) + "," + str(playerInfo.xp) + "," + playerInfo.classType + "\n")

