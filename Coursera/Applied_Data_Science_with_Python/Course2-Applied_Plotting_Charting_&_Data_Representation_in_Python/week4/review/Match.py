import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

# create a function for labeling #
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%d' % int(height),
                ha='center', va='bottom')

matches=pd.read_csv("Match.csv")
teams=pd.read_csv("Team.csv")
player=pd.read_csv("Player.csv")
season=pd.read_csv("Season.csv")
#player_match=pd.read_csv("Player_Match.csv")
print(matches.head())
#print(player_match.head())

matches["Team_Name"] = pd.merge(matches, teams[["Team_Id","Team_Short_Code"]], how='left', left_on='Team_Name_Id',right_on='Team_Id')["Team_Short_Code"]
matches["Opponent_Team"] = pd.merge(matches, teams[["Team_Id","Team_Short_Code"]], how='left', left_on='Opponent_Team_Id',right_on='Team_Id')["Team_Short_Code"]
matches["Toss_Winner"] = pd.merge(matches, teams[["Team_Id","Team_Short_Code"]], how='left', left_on='Toss_Winner_Id',right_on='Team_Id')["Team_Short_Code"]
matches["Match_Winner"] = pd.merge(matches, teams[["Team_Id","Team_Short_Code"]], how='left', left_on='Match_Winner_Id',right_on='Team_Id')["Team_Short_Code"]
matches["Man_Of_The_Match"] = pd.merge(matches, player[["Player_Id","Player_Name"]], how='left', left_on='Man_Of_The_Match_Id',right_on='Player_Id')["Player_Name"]
matches.drop(["Opponent_Team_Id","Toss_Winner_Id","Man_Of_The_Match_Id","Second_Umpire_Id","First_Umpire_Id"], axis=1, inplace=True)
print(matches.head())


# Plot for Matches count at  every stadium
plt.figure(figsize=(12,6))
fig=sns.boxplot(y='Venue_Name',x='Match_Winner_Id',data=matches)
plt.xlabel('Winner')
plt.ylabel('Venue')
plt.show(fig)


plt.figure(figsize=(12,6))
sns.countplot(y='Match_Winner', data=matches)
plt.yticks(rotation='horizontal')
plt.show()


plt.figure(figsize=(12,6))
figa=sns.boxplot(x='Match_Winner',y='Team_Name_Id', data=matches)
plt.xlabel('Team Name')
plt.ylabel('Count')
plt.show(figa)
