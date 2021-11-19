from breezypythongui import EasyFrame
import csv



class HighScore:
    """High score functionality class"""
    def __init__(self):
        self.scores = []

    def read_high_scores(self):
        """reads high scores from the specified csv file
        returns high scores as list sorted by score"""
        lines = []
        try:
            csv_file = open("HighScores.csv", newline="")
            score_reader = csv.reader(csv_file)
        except FileNotFoundError:
            csv_file = open("HighScores.csv","w+", newline="")
            score_reader = csv.reader(csv_file)
        try:
            for row in score_reader:
                lines.append({'name': row[0], "score": int(row[1])})
        except IndexError:
            pass
        lines = sorted(lines,
                       key=lambda i: i['score'],
                       reverse=False)
        csv_file.close()
        return lines

    def write_high_scores(self, score, name):
        """write the high score to the csv file if it is a valid score
        returns True or False depending on whether it was a valid high score also"""
        if self.is_high_score(score):
            if len(self.scores) == 8:
                if score == self.scores[7]['score']:
                    self.scores[7] = {'name': name, 'score': score}
                else:
                    self.scores.append({'name': name, 'score': score})
            else:
                self.scores.append({'name': name, 'score': score})
            self.scores = sorted(self.scores,
                                 key=lambda i: i['score'],
                                 reverse=False)
            with open("HighScores.csv", 'w', newline="\n") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=['name', 'score'])
                for score in self.scores[0:8]:
                    writer.writerow(score)
            return True
        return False

    def is_high_score(self, score):
        """returns whether it is a valid highscore"""
        self.scores = self.read_high_scores()
        n = len(self.scores)
        if n < 8:
            return True
        else:
            if score <= self.scores[7]['score']:
                return True
        return False


class HighScoreTable(EasyFrame):
    """High Score UI class"""

    def __init__(self):
        self.scores = []
        self.hs_func = HighScore()
        EasyFrame.__init__(self, title="High Scores",
                           width=300,
                           height=350,
                           resizable=False)
        self.show_high_scores()

    def show_high_scores(self):
        """method creates the ui for the high score class
        also sorts the scores it received"""
        self.scores = self.hs_func.read_high_scores()
        high_score_labels = []
        self.addLabel(font="Verdana",
                      text="BEST SCORES",
                      row=4,
                      column=0,
                      columnspan=3,
                      sticky='ew',
                      foreground='#03a003')
        for counter in range(0,8):
            bg_colour = '#ffffff'
            try:
                user_score = self.scores[counter]
                if counter % 2 == 0:
                    bg_colour = '#cccccc'
                temp_panel = self.addPanel(row=6 + counter,
                                           column=0,
                                           background=bg_colour)
                temp_panel.addLabel(font='trebuchet',
                                    text=f'{user_score["name"]:<5}',
                                    row=counter,
                                    column=0,
                                    sticky='w',
                                    foreground='#333333',
                                    background=bg_colour)
                temp_panel.addLabel(font='trebuchet',
                                    text=f'{user_score["score"]:>5}',
                                    row=counter,
                                    column=1,
                                    sticky='e',
                                    foreground='#090909',
                                    background=bg_colour)
                high_score_labels.append(temp_panel)
            except IndexError:
                pass


if __name__ == '__main__':
    HighScoreTable().mainloop()
