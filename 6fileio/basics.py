import os
import sys
import csv

#print(os.__file__)
'''
file = open("test.txt","a")
file.write(f"Jai\n")
file.close()
'''
'''
names = ["Jai","Sindhu","Mohan"]
with open("test.txt","a") as file:
    for name in names:
        file.write(f"{name}\n")

with open("test.txt",) as file:

    for line in sorted(file,reverse=True):
        print(line.rstrip())
        #print(line,end='')
'''

'''
students = []
with open('test.txt') as file:
    for line in file:
        name,colour = line.rstrip().split(',')
        students.append({'name':name,'colour':colour})

for student in sorted(students,key=lambda student: student['name']):
    print(f"{student['name']} colour is {student['colour']}")
'''

"""
students = []

file = open("test.txt")

for line in file:
    print(f"{line}",end='')
    #name,address = csv.reader(file)
    #print(name,address)
file.close()
"""

students = []

'''
with open("test.txt") as file:
    reader = csv.reader(file,skipinitialspace=True)
    for name,address in reader:
        students.append({"name":name,'address':address.strip()})

for student in sorted(students,key=lambda student: student['name']):
    print(f"{student['name']} is from {student['address']}")
'''

'''
students = []
with open("test.txt") as file:
    reader = csv.DictReader(file,fieldnames=['name','address'])
    for line in reader:
        students.append({'address':line['address'],'name':line['name']})

print(students)

for student in sorted(students,key=lambda student: student['name']):
    print(f"{student['name']} is from {student['address']}")
'''

name = input("What is your name? ")
address = input("What is your address? ")

with open("file.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=['name','address'])
    writer.writerow({'address':address,'name':name})
    #writer = csv.writer(file)
    #writer.writerow([name,address])