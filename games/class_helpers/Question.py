import random
from games.class_helpers.HQ import QH


class Question:
    """
    __init__  - create a new question by choosing randomly from an already existing storage
    @:param level - level of the question
    """

    def __init__(self, level):
        self.new_question = True
        self.two_option = True
        self.level = level
        hq = QH()
        qList = QH.get_questions(hq)
        self.level_question = QH.get_questions_level_return(hq, qList, self.level)
        self.question_index = random.randint(0, len(self.level_question) - 1)
        self.question = self.level_question[self.question_index]

    """
    return only the question string
    @:param self
    @:return str question
    """

    def get_question(self):
        str1 = self.question[1]
        return str1

    """
    50 50 helper  - 2 answers one right and one not right
    @:param self
    @:return 2 answers
    """

    def get_50_50(self):
        if self.two_option:
            self.two_option = False
            half = []
            temp = []
            posAnswers = []
            ans = self.question[2:-1]
            for answer in ans:
                if '$' in answer:
                    half.append(answer)
                else:
                    temp.append(answer)
            second = random.randint(0, len(temp) - 1)
            half.append(temp.pop(second))
            for i in range(len(ans)):
                if ans[i] in half:
                    if '$' in ans[i]:
                        ans[i] = ans[i][:-1]
                    posAnswers.append(ans[i])
                else:
                    posAnswers.append(" ")
            return posAnswers
        return None

    """
        other question helper  - give the player other question to try to get answer
        @:param self
        @:return other question list
        """

    def get_other_question(self):
        if self.new_question:
            self.new_question = False
            new_question_index = random.randint(0, len(self.level_question) - 1)
            while new_question_index == self.question_index:
                new_question_index = random.randint(0, len(self.level_question) - 1)
            self.question = self.level_question[new_question_index]
    """
        get the correct answer
        @:param self
        @:return the right answer
    """

    def get_answer(self):
        ans = self.question[2:-1]
        for answer in ans:
            if '$' in answer:
                return answer[:-1]

    """
           get the possible answers
           @:param self
           @:return possible answers in list
    """

    def get_possible_answers(self):
        ans = self.question[2:-1]
        for i in range(len(ans)):
            if '$' in ans[i]:
                ans[i] = ans[i][:-1]
        return ans

    def get_right_answer_number(self):
        ans = self.question[2:-1]
        for i in range(len(ans)):
            if '$' in ans[i]:
                return i + 1

    """
        get the max time for a certain question
        @:param self
        @:return time (20 or 60 seconds)
    """

    def get_max_time(self):
        if self.level == 1:
            return 24
        if int(self.level) <= 5:
            return 21
        return 61

    def get_max_show(self):
        return float(5.0+self.level)
