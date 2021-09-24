import time

FILENAME = "mlb-player-stats-Batters.csv"


def teamRosterBattingAverage(teamName):
    playerNames = []
    respectiveAverages = []
    header = None
    print()
    print("Batting average for each player on " + '\033[1m' + str(teamName) + '\033[m')
    with open(FILENAME, "r") as dataFile:
        for currentLine in dataFile:

            if header is None:
                header = currentLine
                continue

            currentLine = currentLine.rstrip()
            currentLine = currentLine.split(',')
            if currentLine[1] == teamName:
                playerNames.append(currentLine[0])
                respectiveAverages.append(currentLine[19])

        playerNameAndAverages = merge(respectiveAverages, playerNames)
        playerNameAndAverages.sort(reverse=True)

        for average, player in playerNameAndAverages:
            print('\033[1m' + player + ": " + '\033[m', end="")
            print(average)
    print()


def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


def possibleTeamNames():
    teamNames = set()
    header = None
    with open(FILENAME, "r") as dataFile:
        for currentLine in dataFile:

            if header is None:
                header = currentLine
                continue

            currentLine = currentLine.rstrip()
            currentLine = currentLine.split(',')
            if currentLine[1] not in teamNames:
                teamNames.add(currentLine[1])

    print("Team Names:")
    for eachTeam in teamNames:
        print('\033[1m' + eachTeam + '\033[m', end=" ")

    print()
    return teamNames


while True:
    teamList = possibleTeamNames()
    userTeamChoice = input(
        "Choose a team from the list to display the teams batting average. Type 'esc' to end: \n>>> ").upper()
    while userTeamChoice not in teamList:
        if userTeamChoice == "ESC":
            break
        print()
        print("No data on " + '\033[1m' + userTeamChoice + '\033[m')
        print()
        possibleTeamNames()
        userTeamChoice = input(
            "Choose a team from the list to display the teams batting average. Type 'esc' to end: \n>>> ").upper()

    if userTeamChoice == "ESC":
        # time.sleep(1)
        print("Program terminating", end="")
        for i in range(4):
            print(".", end="")
            time.sleep(1)
        break
    teamRosterBattingAverage(userTeamChoice)
