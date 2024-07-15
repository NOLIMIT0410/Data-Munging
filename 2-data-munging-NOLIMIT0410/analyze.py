# Place code below to do the analysis part of the assignment.
import csv
row=0
decadeSum=0
year=0
with open('data/clean_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        if line[0]=="Year":
            continue
        Temp=line[1:13]
        sum=0
        for cell in Temp:
            sum=sum+float(cell)
        if row==0:
            year=int(line[0])
        decadeSum=decadeSum+sum 
        row+=1
        if row==10:
            decadeSum=decadeSum/120
            decadeSum=format(decadeSum,".1f")
            endYear =year+9
            print(f"{year} to {endYear}: {decadeSum}")
            decadeSum=0
            row=0



   


        

    
