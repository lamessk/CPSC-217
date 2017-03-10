#Lamess Kharfan. CPSC 217. TUT11. 
#Assignment 3- Analyzing Food Webs. Read from a file containing Predator-Prey 
#relationships, create a dictionary that contains every predator as values and 
#their prey as a list of values. Using this dictionary, find Apex Predators, find 
#producers, identify most flexible eaters, identify "tastiest organism", and 
#determine the height of each organism in the food web. Print every identified item.

import sys

#whatPredatorsEat: Read every line in a given file and identify the preators and prey
#Add them to a dictionary containing predator-prey relationships.
# @param file - the file from which the function reads predator-prey relationships from

def whatPredatorsEat(file):
  print(" ")
  
  #Empty dictionary to be filled with predator-prey relationships
  relationship = {}
  
  #open file 
  try:
    inf = open(file, "r")
  
  except IOError: 
    print("Failed to open", file, ". Quitting...")
    quit()
    
   #for every line in the file, split the line into its elements by "eats"
   for line in inf:
    line = line.rstrip()
    element = line.split(" eats ")
    
    #if predator already in dictionary, add prey to list.
    #otherwise, add predator to list
    if(element[0] in relationship:
      relationship[element[0]].append(element[1])
    else:
      relationship[element[0]] = [element[1]]
     
  inf.close()
  return relationship
  
# printFriendlyString - takes dictionary containing pred-prey relationships, 
# prints in the correct format, "predator eats" followed by its list of prey.
# @param relationship- dictionary of pred-prey relationships

def printFriendlyString(relationship):
  print("Predators and Prey: ")
  
  for key, value in relationship.items():
    predEats = " " + str(key) + " eats"
    
    if len(value) == 1:
      predEats = str(predEats) + str(value[0])
    else:
      for i in range(0, len(value)):
        if i < len(value) - 2:
          predEats = str(predEats) + str(value[i]) + ", "
        else:
          if i != len(value) - 1:
            predEats = str(predEats) + str(value[i]) + " and "
          else:
            predEats = str(predEats) + str(value[i])
        
  print(str(predEats))
  
# printApex - Identifies which predators in the predator-prey relationship dictionary
# that are not eaten by other organisms, or which keys do not appear in the values.
# @param relationship- dictionary of pred-prey relationships
def printApex(relationship):
  print(" ")
  print("The Apex predators are: ")
  for key in relationships.keys():
    apexPred = True
    for keys in relationship.keys():
      if key in relationship[keys]:
        apexPred = False
      if apexPred == True:
        print(" " + str(key))
        
# printProducer - identifies which prey in the pred-prey relationship dictionary
# do not eat another organism, or which values do not appear in the keys.
# @param - relationship- dictionary of pred-prey relationships

def printProducer(relationship):
  print(" ")
  print("The producers are: ")
  preys = []
  for pred in relationship:
    for prey in relationship[pred]:
      if prey not in preys:
        preys.append(prey)
        
  for prey in preys:
    if prey not in relationship:
      print(" " + str(prey))

# printFlexible - Identifies which predators in the predator prey relationship
# dictionary eats the greatest number of organisms (which value has the longest list
# of values) and prints them. 
def printFlexible(relationship):
  print(" ")
  print("The most flexible eater is: ")
  max len = 0 
  max key = " " 
  
  for key in relationship: 
    flexible = len(relationship([key])
    if flexible > max len:
      max len = flexible
  for key in relationship.keys():
    if len(relationship[key]) == max len:
      print(" " + str(key))
      
# printTasty - Identifies which prey is eaten by the most different members of the foodchain
# or which value appears most often in the list of values and prints them
# @param - relationship- dictionary of pred-prey relationships
def printTasty(relationship):
  print(" ")
  print("The Tastiest Prey is: ")
  tastiest = {}
  for prey in relationship:
    for preys in relationship[prey]:
      if preys in tastiest.keys():
        tastiest[preys] = tasiest[preys] + 1
      else:
        tastiest[preys] = 1

  yum = []
  tasty = 0
  for i in tastiest:
    if tasty == tastiest[i]:
      tasty = tastiest[i]
      yum.append[i]
    elif tasty < tastiest[i]:
      tasty = tastiest[i]
      yum = [i]
      
  for i in yum:
    print(" " + str(i))

# printHeights - Identified the longest path from an organism to a producer.
# Lists height for every organism 
# @param - relationship- dictionary of pred-prey relationships
def printHeights(relationship)
  print(" ")
  print("Heights: ")
  heights = {}
  
  allAnimals = set()
  for pred in relationship:
    allAnimals.add(pred)
    for prey in relationship[pred]:
      allAnimals.add(prey)
    
  for i in allAnimals:
    heights[i] = 0
    
  eating = True
  while eating == True:
    eating = False
    for animal in relationship:
      for prey in relationship[animal]:
        if heights[animal] <= heights[prey]:
          heights[animal] = heights[prey] + 1
          eating = True
          
  for pred in heights:
    print(" " + str(pred) + ": " + str(heights[pred]))
    
#main() - used to call functions in order and display their results
def main():
  if len(sys.argv) == 2: 
    filesname = sys.argv[1]
  
  elif len(sys.argv) < 2:
    filename = input("Please enter the name of a file: ")
  
  else: 
    print(sys.argv[0], "must be started with exactly one parameter")
    quit()
    
  relationship = whatPredatorsEat(filename)
  printFriendlyString(relationship)
  printApex(relationship)
  printProducer(relationship)
  printTasty(relationship)
  printFlexible(relationship)
  printHeights(relationship)
  
main()
