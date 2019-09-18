import os
import csv


# change working dir to the dir where this script is stored
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# relative path to file
csvpath = os.path.join("resources","budget_data.csv")

# read in as list
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    header = next(csvreader)
    budget_data_l = list(csvreader)

# get the values needed
total_months = len(budget_data_l)

# get the values needed
total_prof = 0
change_l = list()
for i in range(len(budget_data_l)):
    total_prof = total_prof + float(budget_data_l[i][1])
    if i >0:
        change_l.append(float(budget_data_l[i][1]) - float(budget_data_l[i-1][1]))

# get the values needed
avg_change = sum(change_l)/len(change_l)

# get the values needed
index_max_change = change_l.index(max(change_l)) + 1 
max_change = max(change_l)

index_min_change = change_l.index(min(change_l)) + 1 
min_change = min(change_l)


# print to console
print("\nFinancial Analysis")
print("---------------------------")
print("Total Months: "+str(total_months))
print("Total: ${:0.0f}".format(total_prof))
print("Average change: ${:0.2f}".format(avg_change))
print("Greatest increase in profits: {} (${:0.0f})".format(budget_data_l[index_max_change][0],max_change))
print("Greatest decrease in profits: {} (${:0.0f})".format(budget_data_l[index_min_change][0],min_change))

# write to text file
text_file = open("Output_Pybank.txt", "w")

text_file.write("Financial Analysis\n")
text_file.write("---------------------------\n")
text_file.write("Total Months: "+str(total_months)+"\n")
text_file.write("Total: ${:0.0f}\n".format(total_prof))
text_file.write("Average change: ${:0.2f}\n".format(avg_change))
text_file.write("Greatest increase in profits: {} (${:0.0f})\n".format(budget_data_l[index_max_change][0],max_change))
text_file.write("Greatest decrease in profits: {} (${:0.0f})\n".format(budget_data_l[index_min_change][0],min_change))

text_file.close()