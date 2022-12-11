myemail=list()
username=list()
domain=list()
def separate(email):#function to separate username and domain and store in different list    
  username.append(email[:email.index('@')])
  domain.append(email[email.index('@')+1:])
def accept(n):#function to accept email from user and store it in alist
     for i in range(0,n):
        
        myemail.append(input("email : ").strip())
        separate(myemail[i])
def display(n): #function to diplay username and domain along with email
     print()
     print("email                         username                      domain"     )
     for j in range(0,n): #loop to print all tht email ,domain,username.
        print(myemail[j],end="")
        l1=len(myemail[j])
        for k in range(0,30-l1): #loop to print space
            print(" ",end="")
        print(username[j],end="") # print username
        l2=len(username[j])
        for l in range(0,30-l2): #loop to print space
            print(" ",end="")
        print(domain[j]) # to print domain
 
n = int(input("enter no of email to entered: "))
accept(n)
display(n)
