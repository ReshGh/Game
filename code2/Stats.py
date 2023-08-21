class Stats():

    def __init__(self):
        """stats"""
        self.reset_stats()
        self.run_game = True
        with open('HighScore.txt', 'r',) as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """stats dynamic"""
        self.guns_left = 2
        self.score = 0
