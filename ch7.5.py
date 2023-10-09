# Charge Account Validation
def main():
    try:
        infline=open('charge_accounts.txt','r')
        account=infline.readlines()
        for i in range(len(account)):
            account[i]=int(account[i])
        infline.close()
        #####################################################
        account_number=int(input("Enter a charge account number#:"))
        if account_number in account:
             print(f'{account_number} is a valid number')
        else:
            print(f'{account_number} is not a valid number')
    except Exception as k:
        print(k)
main()
