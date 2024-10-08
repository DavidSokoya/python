# Finish the uefaEuro2016() function so it return string just like in the examples below:
# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."

def uefa_euro_2016(teams, scores):
    [team_a, team_b] = teams
    [score_a, score_b] = scores
    
    if score_a > score_b:
        return f"At match {team_a} - {team_b}, {team_a} won!"
    elif score_a < score_b:
        return f"At match {team_a} - {team_b}, {team_b} won!"
    else: 
          return f"At match {team_a} - {team_b}, teams played draw."