# import modules
import os
import csv

# set path for file
csvpath = os.path.join("..","**PyBank**", "budget_data.csv")

# read csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        print(row)
        total_months = 0

 # open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # for loop including header
    total_months = 0
    for row in csvreader:
        total_months= total_months+1
    total_months = total_months-1
print(total_months)

 # open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

      
    # for loop net profit loss
    net_profit_loss = 0
    # need to write code to skip header
    next(csvreader, None)
    for row in csvreader:
        col=row[1]
        #print(col) # troubleshooting
        #int(col)
        net_profit_loss +=int(col)
    
    
    print(net_profit_loss)

 # open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # need to write code to skip header
    next(csvreader, None)
    
    # set rev_change to first row with data
    first_line =next(csvreader)
    previous_number = first_line[1]
    rev_change=0
    print(previous_number)

    
    # average revenue change - want to find difference between row and row before to find difference between each month then divide by total_months
    
    for col in csvreader:
        rev_change += int(col[1])-int(previous_number)
        
        # set new value to previous_number
        previous_number = col[1]
        
    print(rev_change)    
    avg_rev_change = (rev_change)/(total_months)
    print(avg_rev_change)
    
    # greatest and smallest change in revenue
    #max_rev_change = max(rev_change))
    #print(max_rev_change)
    #min_rev_change = min(rev_change)
    #print(min_rev_change)
    
    
  # open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # need to write code to skip header
    next(csvreader, None)
# set rev_change to first row with data
    first_line =next(csvreader)
    previous_number = first_line[1]
# greatest and smallest change in revenue

    #max_change and min_change
    biggest_change = 0
    smallest_change = 0
    biggest_month = ""
    smallest_month = ""
    for col in csvreader:
        change = int(col[1])-int(previous_number)
        # set new value to previous_number
        previous_number = col[1]
        change_list=[change]
        #print(change_list)
        # if statement for greatest increase #broken
        #print(col[1])
        
        if change > biggest_change:
            biggest_change = change
            biggest_month = col[0]
            
    
        if change < smallest_change:
            smallest_change = change
            smallest_month = col[0]
    print("biggest_change:" +str(biggest_change))
    print("smallest_change:" +str(smallest_change))
    print(biggest_month)
    print(smallest_month)
            
            
        
        # if statement for greatest decrease
        #if change < previous_number
        
        #min_rev_change = min(rev_change)
        #print(min_rev_change)
        
# ** Option: write for loop that compares each row to previous and if statement that if next row is greater than previous, replace with function
   
# financial summary
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months {str(total_months)}\n"
    f"Average Change $ {str(avg_rev_change)}\n"
    f"Greatest Increase in Profits: {biggest_month} {str(biggest_change)}\n"
    f"Greatest Decrease in Profits: {smallest_month} {str(smallest_change)}\n"
)

#set text path

with open("./analysis/analysis.txt","w") as textfile:
    textfile.write(output)
