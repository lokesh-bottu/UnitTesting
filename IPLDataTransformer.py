import csv

class IPLDataTransformer:
    def __init__(self, csv_file):
        self.data = self.load_data(csv_file)

    def load_data(self, csv_file):
        with open(csv_file, mode='r') as file:
            data = list(csv.DictReader(file))
        return data

    def matches_per_year(self):
        matches_count = {}
        for row in self.data:
            year = row['season']
            if year in matches_count:
                matches_count[year] += 1
            else:
                matches_count[year] = 1
        return matches_count
    

    def matches_won_per_year(self):
        matches_won = {}
        for row in self.data:
            year = row["season"]
            if year not in (matches_won.keys()):
                matches_won[year] = {}
            matches_won[year][row["winner"]] = matches_won[year].get(row["winner"],0) +1
        return matches_won
    

    def matches_conceded(self):
        conceded_count = {}
        for row in self.data:
            year = row["season"]
            if str(year) == "2016":
                winner = row["winner"]
                conceded_count[winner] = conceded_count.get(winner,0) + row["win_by_runs"]
        return conceded_count