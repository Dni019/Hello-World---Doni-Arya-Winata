import math

def load(filename: str) -> list:
    '''
    fungsi untuk membaca file yang dipassing dari parameter dan mengembalikan list berupa
    setiap line dari file yang dibaca

    parameters:
      - filename (string): Nama file dalam folder

    returns:
      - data (list): data list tiap baris yang ada dalam text file
    '''
    try:
        # try to open file, if file not found throw the exception
        file = open(file = 'file.txt' , mode = 'w')
        # if succeded opening the file, return each line from the text file
        return file.readlines()
    except FileNotFoundError as exception:
        # shows exception if file not found
        print(exception)

def process(lines: list) -> dict:
    '''
    fungsi untuk memproses data berupa list tulisan menjadi suatu dictionary dengan data yang rapi

    parameters:
        - lines (list): data list berisi line line dari file yang dibaca
    
    returns:
        - data (dict): dictionary data berisi data tiap club dan perolehan nilai
    '''
    # initiate dictionary
    data = dict()

    # loops through each line
    for line in lines:
            # for each line split the text to 4 items
            line = line.split()

            # for the club name, replace underscore to space, and capitalize first letter
            line[0] = line[0].replace('_', ' ').title()
            line[3] = line[3].replace('_', ' ').title()

            # check the outcomes of the game, and decide which one is the winner, and assign the value to variable
            if int(line[1]) > int(line[2]):
                winner = line[0]
                winner_goal = int(line[1])
                loser = line[3]
                loser_goal = int(line[2])
            elif int(line[1]) < int(line[2]):
                winner = line[3]
                winner_goal = int(line[2])
                loser = line[0]
                loser_goal = int(line[1])
            
            # fill in the data for winner
            data[winner] = data.get(winner, {})
            data[winner]['play'] = data[winner].get('play', 0) + 1
            data[winner]['win'] = data[winner].get('win', 0) + 1
            data[winner]['lose'] = data[winner].get('lose', 0)
            data[winner]['draw'] = data[winner].get('draw', 0)
            data[winner]['goals'] = data[winner].get('goals', 0) + winner_goal
            data[winner]['goala'] = data[winner].get('goala', 0) + loser_goal
            data[winner]['total'] = data[winner].get('total', 0) + 3

            # fill in the data for loser
            data[loser] = data.get(loser, {})
            data[loser]['play'] = data[loser].get('play', 0) + 1
            data[loser]['win'] = data[loser].get('win', 0)
            data[loser]['lose'] = data[loser].get('lose', 0) + 1
            data[loser]['draw'] = data[loser].get('draw', 0)
            data[loser]['goals'] = data[loser].get('goals', 0) + loser_goal
            data[loser]['goala'] = data[loser].get('goala', 0) + winner_goal
            data[loser]['total'] = data[loser].get('total', 0)

            # check if the outcome is tie, fill in the data for each teams
            if int(line[1]) == int(line[2]):
                data[line[0]] = data.get(line[0], {})
                data[line[0]]['play'] = data[line[0]].get('play', 0) + 1
                data[line[0]]['win'] = data[line[0]].get('win', 0)
                data[line[0]]['lose'] = data[line[0]].get('lose', 0)
                data[line[0]]['draw'] = data[line[0]].get('draw', 0) + 1
                data[line[0]]['goals'] = data[line[0]].get('goals', 0) + int(line[1])
                data[line[0]]['goala'] = data[line[0]].get('goala', 0) + int(line[2])
                data[line[0]]['total'] = data[line[0]].get('total', 0) + 1

                data[line[3]] = data.get(line[3], {})
                data[line[3]]['play'] = data[line[3]].get('play', 0) + 1
                data[line[3]]['win'] = data[line[3]].get('win', 0)
                data[line[3]]['lose'] = data[line[3]].get('lose', 0)
                data[line[3]]['draw'] = data[line[3]].get('draw', 0) + 1
                data[line[3]]['goals'] = data[line[3]].get('goals', 0) + int(line[2])
                data[line[3]]['goala'] = data[line[3]].get('goala', 0) + int(line[1])
                data[line[3]]['total'] = data[line[3]].get('total', 0) + 1

    # return dictionary 
    return data

def display(data: dict) -> None:
    '''
    fungsi untuk menampikan seluruh data dalam format yang rapi

    parameters:
        - data (dict): data berisi detail perolahan tiap team
    '''
    # sort data berdasarkan total poin dan goal
    data = dict(sorted(data.items(), key = lambda item: (item[1]['total'], item[1]['goals']), reverse = True))
    print('=========================================================================')
    print('Play\tWin\tLose\tDraw\tScore\tAgainst\tPoint\tTeams')
    print('-------------------------------------------------------------------------')
    for key, value in data.items():
        [print(f'{item}', end = '\t') for item in value.values()]
        print(f'{key}')
    print('=========================================================================')

def main():
    data = load('file.txt')
    data = process(data)
    display(data)

if __name__ == '__main__':
    main()