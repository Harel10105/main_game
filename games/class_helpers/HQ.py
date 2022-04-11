class QH():
    def get_questions(self):
        listQ = []
        with open("games/game_files/questions1", "r") as f:
            lines = f.readlines()
            temp = []
            for i in range(len(lines) + 1):
                if i % 6 != 0 or i == 0:
                    temp.append(lines[i][:-1])
                else:
                    listQ.append(temp)
                    temp = []
                    if i + 1 < len(lines):
                        temp.append(lines[i][:-1])
        return listQ

    def get_questions_level_return(self, listQ, level):
        listq2 = []
        currentLevel = str(level)
        for i in range(len(listQ)):
            if listQ[i][0] == currentLevel:
                listQ[i].append(i)
                listq2.append(listQ[i])
        return listq2