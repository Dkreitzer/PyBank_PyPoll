#import addins
import os
import csv
import pandas as pd
import numpy


#Save path to a data set in a variable
csvpath = ("election_data.csv")

#use Pandas to read the data
Election_pd = pd.read_csv(csvpath)

#Create a list of the unique names in the Candidate Column
Candidate_Names = Election_pd["Candidate"].unique()

#Identify the total number of unique votes in the Candidate Column.
Vote_Total = Election_pd["Candidate"].value_counts()


#Total number of votes casted
Total_Votes = Election_pd["Candidate"].count()

#kahn's Votes
KahnVote = Vote_Total[0]
KahnPerc = ("{0:.3%}".format(KahnVote/Total_Votes))

#Correy's Votes
CorreyVote = Vote_Total[1]
CorreyPerc = ("{0:.3%}".format(CorreyVote/Total_Votes))

#li's Votes
LiVote = Vote_Total[2]
LiPerc = ("{0:.3%}".format(LiVote/Total_Votes))

#O'Tooley' Votes
OTooleyVote = Vote_Total[3]
OTooleyPerc = ("{0:.3%}".format(OTooleyVote/Total_Votes))

#PRINTING BELOW

print("Election Results")                                #Election Results

print("-"*25)                                            #dashed line

print(f"Total Votes:  {Total_Votes}")                    #Print total number of votes

print("-"*25)                                            #dashed line

print(f"Kahn: {KahnPerc} ({KahnVote})")                  # print Kahn
print(f"Correy: {CorreyPerc} ({CorreyVote})")            # print Correy
print(f"Li: {LiPerc}  ({LiVote})")                       #print li
print(f"O'Tooley: {OTooleyPerc} ({OTooleyVote})")        #print O'Tooley

print("-"*25)                                            #dashed line

print("Winner: Kahn")                                   #print the winner is

print("-"*25)                                           #dashed line

