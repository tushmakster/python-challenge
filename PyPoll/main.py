# modules
import os
import pandas as pd

# change working dir to the folder this script is stored in
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# csv file object
csvfile = os.path.join("Resources","election_data.csv")


# read as data frame
df = pd.read_csv(csvfile)


# valus that are needed
total_votes_cast = df.shape[0]
candidadtes_l = df["Candidate"].value_counts()
candidates_pct = candidadtes_l/total_votes_cast
winner = candidadtes_l.idxmax()



# print to console in nice format
i = 0
print("Election Results")
print("--------------------------------")
for each in candidadtes_l:
    print(candidadtes_l.index[i]+": {:.2%}".format(candidates_pct[i])+" ("+ str(each)+")" )
    i = i+1
print("--------------------------------")
print("Winner: "+winner)
print("--------------------------------")




# export to text file
text_file = open("Output_Pypoll.txt", "w") 
i = 0
text_file.write("Election Results\n")
text_file.write("--------------------------------\n")
for each in candidadtes_l:
    text_file.write(candidadtes_l.index[i]+": {:.2%}".format(candidates_pct[i])+" ("+ str(each)+")\n" )
    i = i+1
text_file.write("--------------------------------\n")
text_file.write("Winner: "+winner+"\n")
text_file.write("--------------------------------\n")

text_file.close()