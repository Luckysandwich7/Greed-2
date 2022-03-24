class Score:

    """
    This class pulls the score and updates it as you collect Gems and Stones.
    """

    def __init__(self):
        """
        Begins the score at 0
        """    
        self.myScore = 0


    def set_score_plus(self):
        """
        Adds 1 point to the score
        """
        self.myScore += 1

    def set_score_minus(self):
        """
        Subtracts 1 point from the score
        """
        self.myScore -= 1

    def get_score(self):
        """
        Updates the score and presents the new score
        """
        return self.myScore
