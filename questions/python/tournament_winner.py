class Solution:
    def winner(self, competitions, results):
        scores = {}
        for index, competition in enumerate(competitions):
            if results[index] == 1:
                winning_team = competition[0]
            else:
                winning_team = competition[1]

            if winning_team in scores:
                scores[winning_team] += 3
            else:
                scores[winning_team] = 3

            if index == 0:
                current_best_team = winning_team
            elif scores[winning_team] > scores[current_best_team]:
                current_best_team = winning_team

        return current_best_team