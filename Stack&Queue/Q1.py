"""
I am a user of your web browser. I can click back button to go back to the last site or 
click the next button to move to a next site. Create a system where I can do so.

1st line of input will have the number of operations:
2nd line will enter back to go back or will enter new to enter a new website
or will enter now to get the current website

print the current website when user types now
print the history left when number of operations are over

Input:
10
new
abc@yahoo.com
new 
abc1@google.com
new
abc3@google.com
new 
ami@tumi.com
back
back
now
new
ami@tumi.com
now
back

Ans:
abc1@google.com
ami@tumi.com

abc1@google.com
abc@yahoo.com

1,2,3,10

10

1
2
3
10
"""

from Stack_Class import Stack

n = int(input("Enter the number: "))
browser = Stack(n)
for i in range(n):
    ch = input("choice: ")
    if ch == "now":
        print(browser.peep())
    elif ch == "new":
        web = input("Enter the website: ")
        browser.push(web)
    elif ch == "back":
        browser.pop()

browser.display()

    






