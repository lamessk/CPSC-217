#Lamess Kharfan, Student Number: 10150607. CPSC 217.
#Draw a climograph displaying temperature and precipitation data for all
#12 months of the year using 24 input statements, 12 for temperature and 12 for
#precipitation. Line graph will be repersenative of temperature data and Bar
#graph is representative of the precipitation data.

from SimpleGraphics import*

background("white") 

#draw outer lines of graph
line(50, 500, 720, 500)
line(50, 100, 50, 500)
line(720, 100, 720, 500)

#Labels on axises
text(20, 270, "Temp.")
text(20, 285, "(Â°C)")
text(775, 280, "Precip.")
text(775, 295, "(mm)")

#ticks and numbers along the left side
x = 0
numT = 30
for x in range (5):
    x = (x * 100)
    numT = numT - 10
    line(40, x + 100, 50, x + 100)
    text(30, x + 100, numT)

#ticks and numbers along the right side
x = 0
precY = 220
for x in range (11):
    x = (x * 40)
    precY = precY - 20
    line(720, x + 100, 730, x + 100)
    text(740, x + 100, precY)
    

#list months along the bottom
wordsX = 40
months = ['Jan', 'Feb' , 'March' , 'April' , 'May' , 'June' , 'July' , 'Aug' , 'Sept' , 'Oct' , 'Nov' , 'Dec']
for i in range(0, 12):
    wordsX = (i * 55)
    text(80 + wordsX, 520, (months[i]))

#recieve input from the user for precipitation, draw a bar on the graph
#according to month and precipitation value
mon = 1
xPos = 0
yPos = 500
scale = -2

while mon <= 12:
    prec = float(input("Enter a precipitation value for month number " + str(mon) + ": "))
    mon = mon + 1
    xPos = (xPos + 55)
    setFill("light blue")
    rect(xPos, 500, 50, prec * scale)

#recieve input from user for temperature and draw a dot where the the user
#specifies, according to month and temperature value
mon = 1
xPos = 20
yPos = 295
scalingF = -10
while mon <= 12:
    temp = float(input("Enter a temperature value for month number " + str(mon) + ": "))
    mon = mon + 1
    xPos = (xPos + 55)
    setOutline("red")
    setFill("red")
    ellipse(xPos - 4, temp * scalingF + yPos - 4 , 10, 10)

#connect dots with a line
    
    if mon > 2:
        line(xPos - 55, prevY * scalingF + yPos , xPos, temp * scalingF + yPos)
    prevY = temp
    
