
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#setting the inital total months to zero to begin with
total_months = 0
# list for total months
totalmonths = []
#setting the initial profit/loss count to zero
total_profitloss = 0
# list for appending the profit/loss 
monthly_change = []
#list for the appending the difference in each month(profit/loss)
monthly_profit_change = []
#variable for average change
Average_change = 0 
#variable for greatest increase
greatest_increase =0
#variable for greatest decrease
greatest_decrease = 0
#variable to find the month of greatest increase 
monthofgreatestincrease = 0 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
   # To skip the header
    next(csvreader)
    
    #iterate through the csvfile
    #incrementing the total months by 1 everytime to find the total months in the file
    #appending the pofit/loss to the total_months list
    #appending the total months list to find the month of greatest increase
    #appending the monthly change in profit/loss to the monthly_profit_change list
    for row in csvreader:
        total_months += 1
        total_profitloss += int(row[1])
        totalmonths.append(row[0])
        monthly_change.append(int(row[1]))
        
    #iterate through the monthly_change list
    #append the difference in profit/losses(current month -previous month)to a new list called monthly_profit_change list
    #calculate the average monthly change
    #find the maximum in monthly_profit_change and assign it to greatest increase
    #find the minimum in monthly_profit_change adn assign it to greatest decrease
    #once we know these two values, find its index in the monthly profit change list and add 1 to it as the length of monthly_change is up       by one index value
    for i in range(len(monthly_change)-1):
        monthly_profit_change.append(monthly_change[i+1]-monthly_change[i])
        Average_change = round(sum(monthly_profit_change)/len(monthly_profit_change),2)
        greatest_increase = max(monthly_profit_change)
        greatest_decrease = min(monthly_profit_change)
        monthofgreatestincrease = monthly_profit_change.index(greatest_increase)+1
        monthofgreatestdecrease = monthly_profit_change.index(greatest_decrease)+1
        
    #Printing the results  
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profitloss}")
    print(f"Average Change: ${Average_change}")
    print(f"Greatest Increase in Profits: {totalmonths[monthofgreatestincrease]} ($ {greatest_increase})")
    print(f"Greatest Decrease in Profits: {totalmonths[monthofgreatestdecrease]} ($ {greatest_decrease})")
    
    #extracting an output text file with the results 
    outfile = open ("output.txt", "w")
    outfile.write("Financial Analysis")
    outfile.write ("                  \n")
    outfile.write ("------------------------\n")
    outfile.write(f"Total Months: {total_months} \n")
    outfile.write(f"Total : ${total_profitloss} \n")
    outfile.write(f"Average Change: ${Average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {totalmonths[monthofgreatestincrease]} ($ {greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {totalmonths[monthofgreatestdecrease]} ($ {greatest_decrease})\n")
    outfile.close()
    
  