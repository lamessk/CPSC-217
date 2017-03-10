#Name:Lamess Kharfan
#The purpose of the program is to recieve x, y coordinates as input from the user and 
#draw the image of the fancy Android Logo center at the coordinates the user specified

xPos = int(input("Please Enter an X Value: "))
yPos = int(input("Please Enter a Y Value: "))

yPos = yPos - 150
xPos = xPos - 90

from SimpleGraphics import *

background("dark blue")

setFill("green1")
setOutline("green1")

#Draw Head
pieSlice(xPos, yPos, 180, 120, 0, 180)

#Draw body
rect(xPos, yPos + 65, 180, 190)

#Draw Arms
rect(xPos - 35, yPos + 65, 30, 180)
rect(xPos + 185, yPos + 65, 30, 180)

#Draw hands
ellipse(xPos - 36, yPos + 225, 31, 31)
ellipse(xPos + 185, yPos + 225, 31, 31)

#Draw legs
rect(xPos + 30, yPos + 250, 30, 90)
rect(xPos + 120, yPos + 250, 30, 90)

#Draw feet
ellipse(xPos + 29, yPos + 325, 31, 31)
ellipse(xPos + 121, yPos + 325, 31, 31)

#Draw eyes
setFill("white")
ellipse(xPos + 50, yPos + 20, 20, 20)
ellipse(xPos + 110, yPos + 20, 20, 20)

#Draw Antennae
line(xPos, yPos - 20, xPos + 50, yPos + 40)
line(xPos + 190, yPos - 20, xPos + 140, yPos + 40)

#Draw Bowtie
setWidth(1) 
setFill("pink")
setOutline("pink")
polygon(xPos + 30, yPos + 65, xPos + 30, yPos + 105, xPos + 90, yPos + 85)
polygon(xPos + 150, yPos + 65, xPos + 150, yPos + 105, xPos + 90, yPos + 85)

#Draw buttons
setFill("red")
ellipse(xPos + 80, yPos + 110, 20, 20)
setFill("blue")
ellipse(xPos + 80, yPos + 150, 20, 20)
setFill("yellow")
ellipse(xPos + 80, yPos + 190, 20, 20)
