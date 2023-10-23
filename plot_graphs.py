import matplotlib.pyplot as plt
from IPLDataTransformer import IPLDataTransformer

def plot_matches_per_year(data_transformer):
    matches_per_year = data_transformer.matches_per_year()
    years = list(matches_per_year.keys())
    no_of_matches = list(matches_per_year.values())

    plt.bar(years, no_of_matches)
    plt.xlabel('Year')
    plt.ylabel('No of matched Played ')
    plt.title('No of matches played per year for all years')
    plt.show()


def plot_matches_won_per_year(data_transformer):
    matches = data_transformer.matches_won_per_year()
    matches = dict(sorted(matches.items()))
    
    years = list(matches.keys())

    teams_of_years = {}
    # for game in matches:
    #     for group in matches[game]:
    #         if group in teams_of_years.keys():
    #             teams_of_years[group].append(game[group])
    #         else:
    #             teams_of_years[group]=[0]


    teams_of_years={}   # will be organized as : team --> no. of matches won from 2008 to 2017


    for team in matches:
        for i in years:      
            year = str(i)
            
            if team not in teams_of_years:
                teams_of_years[team]=[]
            
            if year not in matches[team]:
                teams_of_years[team].append(0)
            else:           
                teams_of_years[team].append(matches[team][year])


    x = years
    j = [0] * len(years)
    for i in teams_of_years:
        plt.bar(x,teams_of_years[i],bottom=j,label=i)
        for indx in range(len(x)):             
            j[indx] += teams_of_years[i][indx]


def plot_conceded_count(data_transformer):
    conceded_count = data_transformer.matches_conceded()
    teams = list(conceded_count.keys())
    runs = list(conceded_count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(teams, runs)
    plt.xlabel('Team')
    plt.ylabel('Runs Conceded in 2016')
    plt.title('Runs Conceded by Each Team in 2016')
    plt.show()

if __name__ == '__main__':
    data_transformer = IPLDataTransformer("mock_matches.csv")
    plot_matches_per_year(data_transformer)
    plot_matches_won_per_year(data_transformer)
    plot_conceded_count(data_transformer)
