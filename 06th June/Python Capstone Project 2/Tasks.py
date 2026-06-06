import csv
import numpy as np
import pandas as pd
import os

# Part 1 – File Handling
cnt = 0
with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    print(next(reader))
    for row in reader:
        print(row)
        cnt += 1
print("Total Players:", cnt)

# Part 2 – Player Analytics
total_runs = 0
highest_runs = 0
highest_run_scorer = ""
lowest_runs = float("inf")
lowest_run_scorer = ""
players_more_600 = []
players_less_500 = []

with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs = int(row[4])
        total_runs += runs
        if runs < lowest_runs:
            lowest_runs = runs
            lowest_run_scorer = row[1]
        if runs > highest_runs:
            highest_runs = runs
            highest_run_scorer = row[1]
        if runs > 600:
            players_more_600.append(row[1])
        if runs < 500:
            players_less_500.append(row[1])

print("Highest run scorer:", highest_run_scorer)
print("Lowest run scorer:", lowest_run_scorer)
print("Average runs:", total_runs / cnt)
print("Players scored more than 600 runs:\n", players_more_600)
print("Players scored less than 500 runs:\n", players_less_500)

# Part 3 – Team Analytics
team_players = {}
team_runs = {}
with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        team_players[team] = team_players.get(team, 0) + 1
        team_runs[team] = team_runs.get(team, 0) + runs
print("Number of Players by Team:\n", team_players)
print("Total Runs by Team:\n", team_runs)
print("Team with highest runs:", max(team_runs, key=team_runs.get))
print("Team with lowest runs:", min(team_runs, key=team_runs.get))

# Part 4 – Boundary Analysis
max_fours = 0
total_fours = 0
total_sixes = 0
max_sixes = 0
max_fours_player = 0
max_sixes_player = 0

with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        fours = int(row[5])
        sixes = int(row[6])
        total_fours += fours
        total_sixes += sixes
        if fours > max_fours:
            max_fours = fours
            max_fours_player = row[1]
        if sixes > max_sixes:
            max_sixes = sixes
            max_sixes_player = row[1]

print("Player with most fours is", max_fours_player, "with", max_fours, "fours.")
print("Player with most sixes is", max_sixes_player, "with", max_sixes, "sixes.")
print("Total Fours:", total_fours)
print("Total Sixes:", total_sixes)

# Part 5 – Lists, Sets and Dictionaries
players_name = []
team_name = set()
team_runs = {}
player_runs = {}
with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        name = row[1]
        players_name.append(name)
        team_name.add(team)
        team_runs[team] = team_runs.get(team, 0) + runs
        player_runs[name] = player_runs.get(name, 0) + runs

players_name.sort()
print("Sorted player names:")
print(players_name)
print("Unique teams:", team_name)
print("Dictionary, team : total_runs")
print(team_runs)
print("Dictionary, player_name : runs")
print(player_runs)

# Part 6 – Functions
def find_top_scorer():
    top_score = 0
    top_scorer = ""
    with open ("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            runs = int(row[4])
            if runs > top_score:
                top_score = runs
                top_scorer = row[1]
    return top_score, top_scorer
score, player = find_top_scorer()
print("Top scorer is", player, "with", score, "runs.")

def calculate_average_runs():
    total_runs = 0
    cnt = 0
    with open ("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            runs = int(row[4])
            total_runs += runs
            cnt += 1
    return total_runs / cnt
print("Average runs:", calculate_average_runs())

def find_best_team():
    team_runs = {}
    with open ("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            team = row[2]
            runs = int(row[4])
            team_runs[team] = team_runs.get(team, 0) + runs
    return max(team_runs, key=team_runs.get), max(team_runs.values())
best_team, runs = find_best_team()
print("Best team is", best_team, "with", runs, "total runs.")

def find_total_boundaries():
    total_boundaries = 0
    with open ("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            fours = int(row[5])
            sixes = int(row[6])
            total_boundaries += fours + sixes
    return total_boundaries
print("Total boundaries:", find_total_boundaries())

# Part 7 – Exception Handling
try:
    with open ("players.csv", "r") as file:
        reader = csv.reader(file)
        print(next(reader))
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV File not found")

runs = []
with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            runs.append(int(row[4]))
        except ValueError:
            print("Invalid runs value: ", row)
print("Runs:", runs)

matches = []
with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            matches.append(int(row[3]))
        except ValueError:
            print("Invalid matches value: ", row)
print("Matches:", matches)

# Part 8 – NumPy
runs_list = []
with open ("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs_list.append(int(row[4]))
arr = np.array(runs_list)
print("Total Runs", np.sum(arr))
print("Average Runs", np.mean(arr))
print("Maximum Runs", np.max(arr))
print("Minimum Runs", np.min(arr))
print("Standard Deviation", np.std(arr))
print("Median", np.median(arr))

# Part 9 – Pandas
df = pd.read_csv("players.csv")
print(df)

highest_runs = df.sort_values(by="runs", ascending=False)
print("Top 5 run scorers:\n", highest_runs.head())

print("Players sorted by runs descending:\n", highest_runs["player_name"])

team_runs = df.groupby("team")["runs"].sum()
print("Teams with its total runs:\n", team_runs)

avg_runs = df.groupby("team")["runs"].mean()
print("Average runs per team:\n", avg_runs)

runs_more_600 = df[df["runs"] > 600]
print("Players scored more than 600 runs:\n", runs_more_600)

top_team = team_runs.idxmax()
print("Top team:", top_team)

# Report Generation
# cricket_report.txt
total_players = len(df)
total_runs = df["runs"].sum()
average_runs = df["runs"].mean()
highest_scorer = df.loc[df["runs"].idxmax(), "player_name"]
lowest_scorer = df.loc[df["runs"].idxmin(), "player_name"]
most_fours = df.loc[df["fours"].idxmax(), "player_name"]
most_sixes = df.loc[df["sixes"].idxmax(), "player_name"]

def generate_report():
    with open("cricket_report.txt", "w") as file:
        file.write("--- CRICKET REPORT ---\n")
        file.write(f"Total Players: {total_players}\n")
        file.write(f"Total Runs: {total_runs}\n")
        file.write(f"Average Runs: {average_runs}\n")
        file.write(f"Highest Scorer: {highest_scorer}\n")
        file.write(f"Lowest Scorer: {lowest_scorer}\n\n")
        file.write(f"Team Wise Runs:\n {str(team_runs)}\n\n")
        file.write(f"Top 5 Players:\n {str(highest_runs.head())}\n\n")
        file.write(f"Most Fours: {most_fours}\n")
        file.write(f"Most Sixes: {most_sixes}")
generate_report()
print("cricket_report.txt file generated successfully.")

# Bonus Tasks
# top_players.csv
top_players = runs_more_600
top_players.to_csv("top_players.csv", index=False)
print("top_players.csv file generated successfully.")

# team_summary.csv
team_summary = df.groupby("team").agg({
    "runs": ["sum", "mean", "count"]
})
team_summary.columns = ["Total Runs", "Average Runs", "Player Count"]
team_summary = team_summary.reset_index()
team_summary.to_csv("team_summary.csv", index=False)
print("team_summary.csv file generated successfully.")

# Menu Driven Application
while True:
    print("\n--- MENU DRIVEN APPLICATION ---")
    print("1. Player Analysis\n2. Team Analysis\n3. Boundary Analysis\n4. Export Reports\n5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("\n--- PLAYER ANALYSIS ---")
        print("Total Players:", len(df))
        print("Average Runs:", np.mean(arr))
        print("Maximum Runs:", np.max(arr))
        print("Minimum Runs:", np.min(arr))
        print("Top scorer:", highest_scorer)
    elif choice == 2:
        print("\n--- TEAM ANALYSIS ---")
        print("Teams wise Runs:\n", team_runs)
    elif choice == 3:
        print("\n--- BOUNDARY ANALYSIS ---")
        print("Total Boundaries:", find_total_boundaries())
        print("Most Fours:", most_fours)
        print("Most Sixes:", most_sixes)
    elif choice == 4:
        print("\n--- EXPORT REPORTS ---")
        generate_report()
        print("Report exported. Report saved at:")
        print(os.path.abspath("cricket_report.txt"))
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
