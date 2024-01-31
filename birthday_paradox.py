# Birthday Paradox

def findTheProbability(n):
    probabilityNot = 1

    for i in range(n):
        probabilityNot = probabilityNot * (365-i)/365

    probability = 1 - probabilityNot
    percentage = probability*100
    return percentage

n = int(input("Enter the number of people present in the group: "))
percentage = findTheProbability(n)
print(f"Chance that two people share the same birthday in a group of {n} people is: {percentage}")