Email Slicing Python Script
This repository contains a Python script that slices email addresses into their respective usernames and domains. The script accepts a list of email addresses from the user, separates each email into a username and a domain, and then displays the results in a formatted table.

How It Works
The script defines three main functions:

separate(email): This function takes an email address as input, slices it into the username and domain, and appends them to the respective lists.
accept(n): This function accepts n email addresses from the user, stores them in a list, and uses the separate function to process each email.
display(n): This function displays the collected email addresses along with their respective usernames and domains in a formatted table.
Code Overview
python
Copy code
# Initialize empty lists to store emails, usernames, and domains
myemail = list()
username = list()
domain = list()

def separate(email):
    """Function to separate username and domain from an email address."""
    username.append(email[:email.index('@')])
    domain.append(email[email.index('@')+1:])

def accept(n):
    """Function to accept email addresses from the user and store them in a list."""
    for i in range(n):
        myemail.append(input("email: ").strip())
        separate(myemail[i])

def display(n):
    """Function to display email addresses along with their usernames and domains."""
    print()
    print("email                         username                      domain")
    for j in range(n):
        print(myemail[j], end="")
        l1 = len(myemail[j])
        for k in range(30 - l1):
            print(" ", end="")
        print(username[j], end="")
        l2 = len(username[j])
        for l in range(30 - l2):
            print(" ", end="")
        print(domain[j])

# Main execution
n = int(input("Enter number of emails to be entered: "))
accept(n)
display(n)
Usage
Clone the repository or download the script.
Run the script using a Python interpreter.
Enter the number of email addresses you want to input.
Input the email addresses when prompted.
The script will display the email addresses along with their corresponding usernames and domains.
Example
typescript
Copy code
Enter number of emails to be entered: 2
email: example1@gmail.com
email: example2@yahoo.com

email                         username                      domain
example1@gmail.com            example1                      gmail.com
example2@yahoo.com            example2                      yahoo.com
Contributing
Feel free to fork this repository, create a new branch, and submit a pull request if you have any improvements or additional features you would like to add.
