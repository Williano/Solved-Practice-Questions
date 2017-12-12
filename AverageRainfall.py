# Script: AverageRainfall.py
# Description: This program averages rainfall per month.  It asks the user for the number
#              of years.  It will then display the number of months, the total inches of
#              rainfaill, and the average rainfall per month for the entire period.
# Programmer: William Kpabitey Kwabla
# Date: 19.07.16


# Declares variables to hold the total rainfall,
# monthly rainfall, average rainfall, the number
# of years, and the total number of months.
total_rainfall = 0.0
month_rainfall = 0.0
average_rainfall = 0.0
years = 0
total_months = 0

# Gets number of years
number_years = int(input('Enter the number of years: '))

# Gets rainfall by month
for year in range(number_years + 1):
    print ('For year ', year + 1, ':')
    for month in range(12):
        month_rainfall = float(input('Enter the rainfall amount for the month: '))
        
        # Add to total number of months
        total_months += 1
        # Add to total rainfall amount
        total_rainfall += month_rainfall
			
# Calculates the average rainfall
average_rainfall = total_rainfall / total_months

# Prints the total months,total rainfall and average rainfall.
print()
print('For ', total_months, 'months')
print('Total rainfall: ', format(total_rainfall, '.2f'),'inches')
print('Average monthly rainfall: ',format(average_rainfall, '.2f'),'inches')

        



        

