#import csv
import os 
import csv

#read file
csvpath=os.path.join('Resources', 'budget_data.csv')

#initialize variables
Total_Months=0
Total=0
Change=0
previous_profit_loss= None
Changes=[]
Average_change= Change

#read csv
with open('Resources//budget_data.csv','r') as file:
    csvreader=csv.reader(file,delimiter=",")
    next(csvreader)
    for row in csvreader:
        date=row[0]  
        profit_loss= row[1]
        #print(profit_loss, "profit_loss")
        
        #Calculate Total Months
        Total_Months = Total_Months +1
        #print(Total_Months)
        
        #Calculate Total 
        Total= int(profit_loss) + Total
        #print(Total, "total")
        
       #Calculate Change per row
        current_profit_loss= int(row[1])
        if previous_profit_loss is not None:
            Change= current_profit_loss-previous_profit_loss
            Changes.append(Change)
        previous_profit_loss=current_profit_loss
        #print(Change,"change")

 #Calculate Average Change           
denominator = len(Changes)
average_change = sum(Changes)/ denominator
#print(average_change, "average_change")
        
#Calculate Greatest Increase
Greatest_Increase = max(Changes)
#print(Greatest_Increase)

#Calculate Greatest Decrease``
Greatest_Decrease = min(Changes)
#print(Greatest_Decrease)

# Print Financial Analysis Summary
print(f"Financial Analysis --------------------- Total_Months: {Total_Months},Total: {Total}, average_change: {average_change},Greatest_Increase: {Greatest_Increase}, Greatest_Decrease: {Greatest_Decrease}")

#Print Summart to Word Document    
newfilepath = os.path.join("..\\Analysis\\Pybank.txt")
with open("Analysis\\Pybank.txt", "w") as file:
    print("Financial Analyis", file=file)
    print("---------------------", file=file)
    print(f"Total Months:{Total_Months}", file=file)
    print(f"Total:{Total}", file=file)
    print(f"Average Change:{average_change}", file=file)
    print(f"Greatest Increase:{Greatest_Increase}", file=file)
    print(f"Greatest Decrease:{Greatest_Decrease}", file=file)