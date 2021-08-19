"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
"""

def tickets(people):
    cash = []
    for person in people:
        if person == 25:
            cash.append(25)
        elif person == 50:
            if 25 in cash:
                cash.append(50)
                cash.remove(25)
            else:
                return "NO"
        else:
            if 25 in cash and 50 in cash:
                cash.append(100)
                cash.remove(25)
                cash.remove(50)
            else:
                return "NO"
    return "YES"
