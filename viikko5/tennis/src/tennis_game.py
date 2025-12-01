class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0:
                score = "Love-All"
            elif self.m_score1 == 1:
                score = "Fifteen-All"
            elif self.m_score1 == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self.m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score += "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score += "Love"
                elif temp_score == 1:
                    score += "Fifteen"
                elif temp_score == 2:
                    score += "Thirty"
                elif temp_score == 3:
                    score += "Forty"

        return score

    def is_tied(self):
        return self.m_score1 == self.m_score2

    def get_tied_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 < len(self.SCORE_NAMES):
            return f"{self.SCORE_NAMES[self.m_score1]}-All"
        return "Deuce"

    def is_winner(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def get_winner_score(self):
        minus_result = self.m_score1 - self.m_score2
        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def get_ongoing_score(self):
        score = ""
        for i in range(1, 3):
            temp_score = self.m_score1 if i == 1 else self.m_score2
            if i == 2:
                score += "-"
            score += self.SCORE_NAMES[temp_score] if temp_score < len(
                self.SCORE_NAMES) else ""
        return score
