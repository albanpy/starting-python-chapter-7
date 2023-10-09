#Number Analysis Program
def main():
    try:
        num=20
        numbers=[0]*num
        ##################
        total,average_number=calculate_number(numbers,num)
        max_number,min_number=max_min(numbers)
        #################################
        print()
        print(f'The lowest number in the list is {min_number:,.2f}')
        print(f'The highest number in the list is {max_number:,.2f}')
        print(f'The total of the numbers in the list is {total:,.2f}')
        print(f'The average of the numbers in the list is {average_number:,.2f}')
    except Exception as d:
        print(d)
def calculate_number(number,num):
    try:
        total=0.0
        print(f'Enter a series of {num} numbers')
        print()
        for n in range(num):
            number[n]=float(input("Enter Number#:"))
            total+=number[n]
        avg=total/num
        return total,avg
    except Exception as h:
        print(h)
def max_min(nums):
    try:
        maxs=max(nums)
        mins=min(nums)
        return maxs,mins
    except Exception as j:
        print(j)
main()
