#Rainfall Statistics
def main():
    try:
        num=12
        month=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        rain=[0]*num
        ##################
        total=calculate_rain(month,rain,num)
        ####################
        average_rain=total/num
        ######################
        mon_max,mon_min=min_max_rain(month,rain)
        ##################
    except Exception as j:
        print(j)
    else:
        print(f'The total rainfall for the year={total:,.2f}')
        print(f"the average monthly rainfall={average_rain:,.2f}")
        print(f'The months with the highest amounts is {mon_max}.')
        print(f'The months with the lowest amounts is {mon_min}.')
def calculate_rain(mon,rain,num):
    try:
        total=0.0
        for n in range(num):
            rain[n]=float(input(f"Enter the total rainfall for {mon[n]}:"))
            total+=rain[n]
        return total
    except Exception as k:
        print(k)
def min_max_rain(mon,rain):
    try:
        maxs=rain.index(max(rain))
        mins=rain.index(min(rain))
        month_max=mon[maxs]
        month_min=mon[mins]
        return month_max,month_min
    except Exception as l:
        print(l)
        

main()
