import os
import csv

# Had an issue with a "I/O Operation on Closed File" error, was able to source this for help: https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file"
filepath = os.path.join('.', 'Resources', 'election_data.csv')

with open(filepath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    candid_list = [candidate[2] for candidate in reader]

candid_descrip = [[candidate,candid_list.count(candidate)] for candidate in set(candid_list)]

total = len(candid_list)

#Lambda: https://www.w3schools.com/python/python_lambda.asp
candid_info = sorted(candid_descrip, key=lambda x: x[1], reverse=True)

#Percentage
for candidate in candid_info:
    percent_votes = (candidate[1] / total) * 100
    #Number Format
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

#Personal Note: f to format a string
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

print("-------------------------")
print(f"Winner: {candid_info[0][0]}")
print("-------------------------")

#For the text file.
filepath = os.path.join('.', 'Analysis', 'PyPollResults.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in candid_info:
        percent_votes = (candidate[1] / total) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {candid_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)
