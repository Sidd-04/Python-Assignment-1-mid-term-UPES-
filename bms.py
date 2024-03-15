'''..................................BANK MANAGEMENT SYSTEM ..........................................'''
print("WELCOME TO BANK PORTAL\n")
while True:
 print("1.CREATE ACCOUNT")
 print("2.LOGIN TO AN EXISTING ACCOUNT")
 print("3.EXIT")
 i=int(input("CHOOSE ANY OPTION = "))
 if i==1:
    acc_no=int(input('\nEnter your ACCOUNT NUMBER='))
    acc_name=input('Enter your ACCOUNT NAME=')
    ph_no=int(input('Enter your PHONE NUMBER='))
    add=(input('Enter your place='))
    cr_amt=int(input('Enter your credit  amount='))
    L={"account no":acc_no,"account name":acc_name,"Phone number":ph_no,"Address":add,"Account Balance":cr_amt}
    print("Your Account is created")
    print("Your Account details are as follows:-\n")
    print(L,"\n")

 if i==2:

  id=int(input("\nENTER YOUR ACCOUNT NO= "))
  nm=input("ENTER YOUR NAME= ")
  try:
   if (id==acc_no and nm==acc_name):
    while True:
     print('1.TRANSACTION')
     print('2.CUSTOMER DETAILS')
     print('3.TRANSACTION DETAILS')
     print('4.DELETE ACCOUNT')
     print('5.CHANGE ACCOUNT DETAILS')
     print('6.QUIT')

     n=int(input("Enter your CHOICE = "))
 
     amt11=0;amt22=0
     if n == 1:
      print('\n1.WITHDRAW AMOUNT')
      print('2.ADD AMOUNT\n')
      x=int(input("Enter your CHOICE = "))
 
      if x == 1:
   
       acct_no=int(input("\nEnter your Account Number = "))
       acct_name=input("Enter Your Name = ")
       if (acct_no==acc_no and acct_name==acc_name):
         amt1=int(input('\nEnter Withdrawl Amount = '))
         amt11=amt1
         cr_amt=cr_amt-amt1
         print(amt1,"rupees is deducted from Your Account ")
         print("\nRemaining Account balance is : ",cr_amt)
      
       else:
         print("\nInvalid Account details")
 
      if x== 2:
       acct_no=int(input("\nEnter your Account Number = "))
       acct_name=input("Enter Your Name = ")
       if (acct_no==acc_no and acct_name==acc_name):
        amt2=int(input('\nAmount to be Recieved is = '))
        amt22=amt2
        cr_amt=cr_amt+amt2
        print('Account Updated Succesfully!!!!!')
        print("\n Updated Account Balance is : ",cr_amt)
    
       else:
        print("\nInvalid Account details")
     
     if n == 2:
       acct_no=int(input('\nEnter your Account Number = '))
       name=input("Enter Your Name = ")
       if (acct_no==acc_no):
        print('ACCOUNT NO=',acc_no)
        print('ACCOUNT NAME=',acc_name)
        print('PHONE NUMBER=',ph_no)
        print('ADDRESS OF USER=',add)
        print('Account balance=',cr_amt) 
       else:
        print("\nInvalid Account Number")
 
     if n== 3:
      acct_no=int(input('Enter your Account Number =' ))
      if (acct_no==acc_no):
       print(' TRANSACTION DETAILS FOR ACCOUNT NUMBER=',acct_no ,'\nWITHDRAWAL AMOUNT FROM YOUR ACCOUNT ',acc_no,"is : ",amt11,'\nAMOUNT ADDED TO YOUR ACCOUNT ',acc_no,"is : ",amt22)
      else:
       print("Invalid Account Number")

     if n == 4:
      print('DELETE YOUR ACCOUNT')
      acct_no=int(input('Enter your account number='))
      if acct_no==acc_no:
       L.clear()
       print('ACCOUNT DELETED SUCCESSFULLY')
  
      else:
       print("Invalid Account Number")

     if n == 5:
      print("1.Account Name","\n2.Phone Number","\n3.Address")
      j=int(input("\nChoose any Option which you want to Update \n"))
      if j==1:
       acc_name=input("Enter new name for your Account= ")
       print("\nNew account name is : ",acc_name)
      if j==2:
       ph_no=input("Enter new Phone Number for your Account= ") 
       print("\nNew Phone Number is : ",ph_no)
      if j==3:
       add=input("Enter new Address= ")
       print("\nUpdated Address is : ",add)


     if n == 6:
      quit()

     else: 
      print("\nPLEASE CHOOSE A OPTION\n")
  except NameError:
    print("Account not exist")

 if i==3:
  quit()
 





'''.............................................END..............................'''