#Total Sales
def main():
    try:
        num=7
        day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        num_day=[0]*num
        total=sales(day,num_day,num)
    except Exception as k:
        print(k)
    else:
        print()
        print(f'The total sales for the week are {total:,.2f}/= sh')
def sales(day,num_day,num):
    try:
        total=0.0
        for n in range(num):
             num_day[n]=float(input(f"Enter a store’s sales for {day[n]}#:"))
             total+=num_day[n]
        return total
    except Exception as l:
        print(l)
main()
