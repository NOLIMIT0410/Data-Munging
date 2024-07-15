# Place code below to do the munging part of this assignment.
import csv
output_file_path = "data/clean_data.csv"
out_file=open(output_file_path,'w', newline='')
csvwriter=csv.writer(out_file)
f = open("data/GLB.Ts+dSST.txt", "r")
print(f)
isHeadFound=False
#filter lines as we only want to work on lines that we need.
for line in f:
    #get rid of lines that are empty
    if not line.strip():
        continue
    #keep only the first title
    if line.startswith("Year") and isHeadFound==True:
        continue
    if line.startswith("Year"):
        isHeadFound=True       
    if not line.startswith("Year") and not line[0].isdigit():
        continue 
    line_split = line.split()
    #print (line_split)
    #set all missing value as 0.0
    for idx in range(len(line_split)):
        if "*" in line_split[idx]:
            line_split[idx]="0.0"
    #change unit of our values
    if not line_split[0]=="Year":
        for idx in range(1,len(line_split)-1):
            line_split[idx]=float(line_split[idx])
            line_split[idx]=line_split[idx]/100*1.8
            line_split[idx]=format(line_split[idx],".1f")
            print(line_split[idx])
    csvwriter.writerow(line_split)