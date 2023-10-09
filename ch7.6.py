# Larger Than n
def main():
    n=25
    list_n=[23,12,45,67,25,30,35,12,15,80,16]
    number=lis_number(list_n,n)
    for i in number:
        print(i)
def lis_number(list_n,n):
    number=[z for z in list_n if z>n]
    return number
main()