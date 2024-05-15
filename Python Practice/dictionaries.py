"""
dic={"ali":3236688762, "hassan" : 3258195012, "hasnain": 3017262047}
print(dic)
print(dic["hassan"])
dic["sam"]=16356524
print(dic)
del dic["hasnain"]
print(dic)
for item in dic:
    print(f"Key: {item} Number is : {dic[item]}")
for id,value in dic.items():
    print(f"Key: {id} Number is : {value}")
print("hassan" in dic)
print(dic.clear())
print(dic)
roll_no=(5,100)
print(roll_no[1])
# roll_no[1]=5000      # tuples canot be updated
print(roll_no)

#Using above create a dictionary of countries and its population
#1,1
countries = {
    'China': 143,
    "india": 136,
    "Usa": 32,
    "Pakistan": 21
}
def main():
    while True:
        options = input(f" 1) Print : \n 2) Add : \n 3) Remove : \n 4) Query :\n 5) Exit : \n Select Option: ")
        options = int(options)
        if options == 5:
            break

        if options == 1:
            printAll()
        elif options == 2:
            add()
        elif options == 3:
            remove()
        elif options == 4:
            query()
        else:
            print("Invalid option. Please try again.")

def printAll():
    for item in countries:
        print(f"Countrie {item} Population {countries[item]}")
    print("\n")
def add():
    cName = input("Write Country Name to Add")
    if cName in countries:
        print("Country Already Exist")
    else:
        pop = input("Enter Population")
        countries[cName] = pop
def remove():
    cName = input("Enter Country Name U Want To Remove: ")
    cName = cName.lower()
    if cName in countries:
        del countries[cName]
        print(f"Remaainig Dictionary: \n")
        printAll()
    else:
        print("Country doesn't Exist: ")
def query():
    cName = input("Enter Country Name U Want To Remove: ")
    if cName not in countries:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {cName} is: {countries[cName]} crore")

if __name__ == '__main__':
    main()
  #Q2//////////////////////////////////////////////////////////////////////////////////////////
import statistics
stocks={
    "info": [600,630,620],
    "ril": [1430,1490,1567],
    "mtl": [234,180,160],
}

def main():
    op=input(f" 1) Print \n 2) Add \n Enter Ur Choise")
    op=int(op)
    if op == 1:
        printAll()
    elif op == 2:
        add()
    else:
        print("You Enter Wrong Choice")
def printAll():
    for stock, price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ", round(avg, 2))
def add():
    s = input("Enter a stock ticker to add:")
    p = input("Enter price of this stock:")
    p = float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    printAll()
if __name__ == '__main__':
    main()
"""
import math

# Q3///////////////////////////////////////////////////////////////////////////////

import math
def cir_Cal(radius):
    area=math.pi*(radius**2)
    c=2*math.pi*radius
    d=2*radius
    return area, c, d
"""""
if __name__ == '__main__':
    r = input("Enter radius Of Circle")
    r = float(r)
    area, c, d = cir_Cal(r)
    print(f"Area :{area} \n Circumference :{c} \n Diameter :{d}")
////////////////////////////////////////////////DICTIONARY POPULATION//////////////////////////////////
population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country,population[country] in population.items():
        print(f"{country}==>{population[country]}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()
"""

import statistics

stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all():
    for stock,price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ",round(avg,2))


def add():
    s = input("Enter a stock ticker to add:")
    p = input("Enter price of this stock:")
    p=float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()


def main():
    op=input("Enter operation (print, add or add):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

if __name__ == '__main__':
    main()

population={
    "pakistan" : 21,
    "india" : 136,
    "china" : 143,
    "USA" : 32,
}
def print_all():
    for countries , population[countries] in population.items():
        print(f"{countries} ==> {population[countries]}")
def add():
    countries=input("Enter Country Name")
    countries=countries.lower()
    if countries in population:
        print(f"{countries} Already exist in Dictionary")
        return
    p=input("Enter Population of Country:")
    p=float(p)
    population[countries]=p
    print_all()
def remove():
    countries=input("Enter Country Name:")
    countries=countries.lower()
    if countries not in population:
        print(f"{countries} does'nt exist in Dictionary")
        return
    del population[countries]
    print_all()
def query():
    countries=input("Enter Country Name U want to Query:")
    countries=countries.lower()
    if countries not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {countries} is: {population[countries]} crore")
def main():
    Choice=input(f"Enter Ur Choice [Print , Add , Remove, Query]")
    if Choice.lower() == "print":
        print_all()
    elif Choice.lower() == "add":
        add()
    elif Choice.lower() == "remove":
        remove()
    elif Choice.lower() == "query":
        query()
if __name__ == '__main__':
    main()
