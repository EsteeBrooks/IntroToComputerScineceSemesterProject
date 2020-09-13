#"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity poicy of the CS department.”

import random
import Draw

#Create the canvas
Draw.setCanvasSize(1200,780) 

# FUNCTIONS

#Function to draw the tool bar 
def toolBox():
    
    #Draw Gray Background  
    Draw.setColor(Draw.LIGHT_GRAY)  
    Draw.filledRect(0, 700, 1200, 78)
    Draw.setColor(Draw.GRAY)      
    
    #Draw different buttons in Tool Bar using a list and loop.
    Draw.setFontFamily("Times") 
    Draw.setFontSize(50)      
    positions = [55, 710, 200, 60]
    options = ["New Box","Delete Box", "Shuffle", "Bring Foward", "Send Backward"]
    size = 50
    
    for i in range(len(options)):
        Draw.setColor(Draw.GRAY)      
        Draw.filledRect(positions[0], positions[1], positions[2], positions[3]) 
        Draw.setColor(Draw.DARK_GRAY)
        #Changing the size of the font for certain tools in order to fit the background
        if options[i] == "Bring Foward":
            Draw.setFontSize(size-16)
        elif options[i] == "Send Backward":
            Draw.setFontSize(size-20)  
        elif options[i] == "Delete Box":
            Draw.setFontSize(size-8)   
        else:
            Draw.setFontSize(size)
        
        #Drawing the words for each the tool in the right position  
        if options[i] == "Delete":
            Draw.string(options[i], positions[0]+33 , positions[1]+5)
        elif options[i] == "Shuffle":
            Draw.string(options[i], positions[0]+27 , positions[1]+5)
        elif options[i] == "Bring Foward" or options[i] == "Send Backward":
            Draw.string(options[i], positions[0]+5 , positions[1]+13)        
        else:
            Draw.string(options[i], positions[0]+5 , positions[1]+5)
        
        #updating the position to draw in the next tool title in the next box
        positions[0] += 220    

#Instructions function: Draw a box above the tools with the the instructions in it
def instructions(str):
    Draw.setColor(Draw.GRAY)
    Draw.filledRect(0, 650, 1200, 50)    
    Draw.setColor(Draw.DARK_GRAY)
    if str == "Click cattycorner corner. This must be BELOW and to the RIGHT of the first corner.":
        Draw.setFontSize(35)        
    else:
        Draw.setFontSize(40)
    Draw.string(str, 0, 650)

#Checking if a person pressed on the canvas and updating newX and newY to those spots
def mousePressed():
    mousePress = False
    while not mousePress:                
        if Draw.mousePressed():
            mousePress = True 
            newX = Draw.mouseX()
            newY = Draw.mouseY()
    return newX, newY

#Finding the intersection between a horizontal line at spot clicked and the orthogonals 
def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    return [px, py] 

#Step 1 of New Box Tool: Creating the vanishing point on the horizon line and the corners of the front of the box
def boxSkeleton():    
    
    #Draw the vanishing point and horzon line:
    instructions("Click vanishing point location.")
    newX, newY = mousePressed()
    if newY >= 0 and newY <= 650:
        
        #Drawing the vanishing point and horizon line
        Draw.filledOval(newX, newY,5,5)
        Draw.line(0, newY+2, 1200, newY+2)
        
        #Saving the vanishing points in varibles
        vpX = newX+2 
        vpY = newY+2
        
        #Updating the instructions
        instructions("Click first corner of box.")
    
    else:
        #Leave the function to show error message 
        return 2, 2
    
    #Draw the first corner and saving the point
    newX, newY = mousePressed()
    if newY >= 0 and newY <= 650:
        
        #Creating an empty list to store the front corners of the box
        corners = []  
        
        #Saving the first corner 
        cornerOneY = newY
        cornerOneX = newX
        
        #Drawing the first corner
        Draw.filledRect(cornerOneX ,cornerOneY,3,3)
        
        #Update the instructions
        instructions("Click cattycorner corner. This must be BELOW and to the RIGHT of the first corner.")
    else:
        #Leave the function to show the error message
        return 1,1
    #Draw the second corner, the front of the box, and the orthogonals to the vanishing point  
    newX, newY = mousePressed()
    if newY >= 0 and newY <= 650:
        
        #If the user doesn't draw the second corner to the right and below the first corner, create an error message
        if cornerOneY > newY or cornerOneX > newX:
            
            #Leave the function
            return 0, 0           
        
        #Saving the second corner         
        cornerTwoY = newY
        cornerTwoX = newX 
        
        #Drawing the second point of the box 
        Draw.filledRect(cornerTwoX,cornerTwoY,3,3)        
        
        #Saving the third corner, which has the x coord of the second corner
        #and the y coord of the first corner        
        cornerThreeY = cornerOneY 
        cornerThreeX = cornerTwoX
        
        #Saving the fourth corner, which has the x coord of the first corner
        #and the y coord of the second corner          
        cornerFourY = cornerTwoY
        cornerFourX = cornerOneX
        
        #Saving the width and height of the box into a variable    
        widthFrontBox = (cornerTwoX-cornerOneX) + 3
        heightFrontBox = (cornerTwoY-cornerOneY) + 3
        
        #Drawing the front of the box 
        Draw.rect(cornerOneX, cornerOneY, widthFrontBox, heightFrontBox)
              

        #Saving all the new varibles in two lists so it is easy to pass into other functions:
        #The first has the front box corners, height and width:  
        corners += [[cornerOneX, cornerOneY],
                    [cornerTwoX, cornerTwoY],
                    [cornerThreeX, cornerThreeY],
                    [cornerFourX, cornerFourY],
                    [widthFrontBox, heightFrontBox]]
        
        #The second has the front box corners and the vanishing point:
        orth =        [[cornerOneX, cornerOneY, vpX, vpY],
                       [cornerTwoX, cornerTwoY, vpX, vpY],
                       [cornerThreeX, cornerThreeY, vpX, vpY],
                       [cornerFourX, cornerFourY, vpX, vpY]]
        
        #Drawing the orthogonals from the front of the box to the vanishing point
        for i in range(len(orth)):
            Draw.line(orth[0],orth[1],orth[2],orth[3])            
        
        #Update the instruction
        instructions("Click on box to decide how long the box is.") 
    return orth, corners

#Step 2 of New Box Tool: Deciding how long the box
def lengthBox(orth, corners):
    
    #Creating the varible that will keep track of the orthgonal closest to the click 
    closestLine = 0
    
    newX, newY = mousePressed()
    clickXY = [newX, newY]
    
    #Find the intersection point between the orthogonals and the new click:
    #if the box is closests to orthogonal [cornerOneX, cornerOneY, vpX, vpY] update the varibles: 
    intersection = findIntersection (orth[0][0], orth[0][1], orth[0][2], orth[0][3], 0, newY, 1200, newY)
    #Create the a varible that stores the distance from the closest orthogonal to the click:   
    closestOrthToClick = abs(intersection[0]-newX)
    
    #Loop through the rest of the orthogonals to check if the click is closter to those orthogonals: 
    for i in range(2, len(orth), 1):
        intersection = findIntersection ( orth[i][0], orth[i][1], orth[i][2], orth[i][3], 0, newY, 1200, newY)
        if abs(intersection[0]-newX) < closestOrthToClick:
            #Update the shortest distance for the closest orthogonal and the click 
            closestOrthToClick = abs(intersection[0]-newX)
            #Update the closest orthogonal  
            closestLine = i

    #Setting newX and newY to a different variable and returning it for the next function to use 
    endOfBoxX = newX
    endOfBoxY = newY
    
    return clickXY, closestLine, endOfBoxX, endOfBoxY

#Step 3 of New Box Tool: Drawing the sides as shapes 
def boxAsShapes(boxes, colorsForBoxes, clickXY, closestLine, orth, corners, endOfBoxX, endOfBoxY):
    #If the closest line to the click is the second line (meaning cornerTwoX/cornerTwoY), create the sides like this:
    if closestLine == 2:
    
        #Finding the points to draw the polygon based on the intersection between the user click and the orth 
        #When closestLine == 2, the end of the side of the box is in line with the click. The top of the box is based of the sides 
        intersectionLine0AndClick = findIntersection (orth[0][0], orth[0][1], orth[0][2], orth[0][3], 0, clickXY[1], 1200, clickXY[1])        
        intersectionLine2AndClick = findIntersection (orth[2][0], orth[2][1], orth[0][2], orth[0][3], 0, clickXY[1], 1200, clickXY[1])       
        intersectionLine3AndClick = findIntersection (orth[3][0], orth[3][1], orth[0][2], orth[0][3], 0, clickXY[1], 1200, clickXY[1])            
        intersectionLine3AndintersectionLine0AndClick = findIntersection (orth[3][0], orth[3][1], orth[0][2], orth[0][3], intersectionLine0AndClick[0], 0, intersectionLine0AndClick[0], 650)
        
        #Creating lists to store the sides, top, and bottom of the box:
        #Top of box coordinates 
        coordsTop = [orth[2][0], orth[2][1], orth[0][0], orth[0][1], intersectionLine0AndClick[0], intersectionLine0AndClick[1], intersectionLine2AndClick[0],intersectionLine2AndClick[1]]
        
        #Bottom of box coordinates 
        coordsBottom = [corners[1][0], corners[1][1], corners[3][0], corners[3][1],  intersectionLine3AndintersectionLine0AndClick[0], intersectionLine3AndintersectionLine0AndClick[1], intersectionLine2AndClick[0], intersectionLine3AndintersectionLine0AndClick[1]]        
        
        #Side Left of box coordinates
        coordsSideLeft = [orth[0][0], orth[0][1], orth[3][0], orth[3][1], intersectionLine3AndintersectionLine0AndClick[0], intersectionLine3AndintersectionLine0AndClick[1], intersectionLine0AndClick[0],intersectionLine0AndClick[1]]
        
        #Side right of box coordinates
        coordsSideRight = [corners[1][0], corners[1][1], corners[2][0], corners[2][1],  intersectionLine2AndClick[0], intersectionLine0AndClick[1], intersectionLine2AndClick[0], intersectionLine3AndintersectionLine0AndClick[1]]

    #If the closest line to the click is any other side create the sides like this:
    else: 
        #Finding the points to draw the polygon based on the intersection between the user click and the orth: 
        #When closestLine != 2, the end of the top of the box is in line with the click. The sides of the box is based of the top 
        intersectionLine0AndClick = findIntersection (orth[0][0], orth[0][1], orth[0][2], orth[0][3], clickXY[0], 0, clickXY[0], 780)
        intersectionLine3AndClick = findIntersection (orth[3][0], orth[3][1], orth[0][2], orth[0][3], clickXY[0], 0, clickXY[0], 780)            
        intersectionLine2AndintersectionLine0AndClick = findIntersection (orth[2][0], orth[2][1], orth[0][2], orth[0][3], 0, intersectionLine0AndClick[1], 1200, intersectionLine0AndClick[1])
        
        #Creating lists to store the sides, top, and bottom of the box:        
        #Top of box coordinates 
        coordsTop = [corners[2][0], corners[2][1], corners[0][0], corners[0][1], intersectionLine0AndClick[0], intersectionLine0AndClick[1], intersectionLine2AndintersectionLine0AndClick[0],intersectionLine2AndintersectionLine0AndClick[1]]
        
        #Bottom of box coordinates 
        coordsBottom = [corners[1][0], corners[1][1], corners[3][0], corners[3][1], intersectionLine3AndClick[0], intersectionLine3AndClick[1], intersectionLine2AndintersectionLine0AndClick[0], intersectionLine3AndClick[1]]
            
        #Side  left of box coordinates
        coordsSideLeft = [corners[0][0], corners[0][1], corners[3][0], corners[3][1], intersectionLine3AndClick[0], intersectionLine3AndClick[1], intersectionLine0AndClick[0],intersectionLine0AndClick[1]]
        
        #Side right of box coordinates
        coordsSideRight = [corners[1][0], corners[1][1], corners[2][0], corners[2][1], intersectionLine2AndintersectionLine0AndClick[0], intersectionLine2AndintersectionLine0AndClick[1], intersectionLine2AndintersectionLine0AndClick[0], intersectionLine3AndClick[1]]
        
    #Front box coordinates 
    coordsFront = [corners[0][0], corners[0][1], corners[2][0], corners[2][1], corners[1][0], corners[1][1], corners[3][0], corners[3][1]]
    
    #Adding the sides, top, and bottom of the box as an element to the boxes boxes 
    #If the end of the box  is to the right Vanishing point and...
    if endOfBoxX > orth[0][2]:
        #above the vanishing point:
        if endOfBoxY > orth[0][3]:
            boxes += [[coordsSideLeft, coordsTop, coordsFront]]
        #below the vanishing point:
        elif endOfBoxY < orth[0][3]:
            boxes += [[coordsSideLeft, coordsBottom, coordsFront]]
    #if the end of the box is to the left of the vanishing point and ...
    elif endOfBoxX <= orth[0][2]:
        #above the vanishing point:
        if endOfBoxY > orth[0][3]:
            boxes += [[coordsSideRight, coordsTop, coordsFront]]
        #below the vanishing point:
        elif endOfBoxY < orth[0][3]:
            boxes += [[coordsSideRight, coordsBottom, coordsFront]]

    #Choosing random colors for the box 
    for i in range(len(boxes[-1])):
        colorsForBoxes += [[randomColor()]]
    
    #Redrawing the screen with just the boxes 
    redrawScreen(boxes, colorsForBoxes) 
    return boxes, colorsForBoxes

#Function to clear screen and redraw the boxes
def redrawScreen(boxes, colorsForBoxes):
    Draw.clear()
    toolBox()
    for i in range (len(boxes)):
        for j in range(len(boxes[i])):
            Draw.setColor(colorsForBoxes[j])
            Draw.filledPolygon(boxes[i][j])          

#Picking a random color 
def randomColor():
    options=[Draw.BLACK,
             Draw.GRAY,
             Draw.RED,
             Draw.GREEN,
             Draw.BLUE,
             Draw.CYAN,
             Draw.MAGENTA,
             Draw.YELLOW,
             Draw.DARK_RED,
             Draw.DARK_GREEN,
             Draw.DARK_BLUE,
             Draw.DARK_GRAY,
             Draw.LIGHT_GRAY,
             Draw.ORANGE,
             Draw.VIOLET,
             Draw.PINK]
    color = random.choice(options)
    return color        

#New Box Tool Function
def newBox(boxes, colorsForBoxes):
    #Redrawing the screen in case there was an error message before:
    redrawScreen(boxes, colorsForBoxes)
    
    #Doing part 1 of this function:
    orth, corners = boxSkeleton()
    
    #if the user clicked in the tool box:
    if orth == 2 and corners == 2:
        redrawScreen(boxes, colorsForBoxes)
        return
    
    #if the user created points on the tool box show an error message:    
    if orth == 1 and corners == 1:
        
        Draw.setColor(Draw.LIGHT_GRAY)
        Draw.filledRect(300, 200, 610, 150)
        Draw.setColor(Draw.BLACK)            
        
        Draw.string("Whoops! Draw only on the canvas.", 320, 220)
        
        Draw.setColor(Draw.RED)            
        Draw.string("Press New Box to try again", 320, 270)
        return
        
    #if the user created points incorrectly, show an error message:    
    if orth == 0 and corners == 0:

        Draw.setColor(Draw.LIGHT_GRAY)
        Draw.filledRect(300, 200, 610, 260)
        Draw.setColor(Draw.BLACK)            
        
        Draw.string("Whoops! The second corner must", 320, 220)
        Draw.string("be drawn to the RIGHT and", 320, 270)
        Draw.string("BELOW the first corner.", 320, 320)
        
        Draw.setColor(Draw.RED)            
        Draw.string("Press New Box to try again", 320, 390)
        return
                
    else:
        #If drawn correctly, go on to the next two parts of this function:
        clickXY, closestLine, endOfBoxX, endOfBoxY = lengthBox(orth, corners)
        boxAsShapes(boxes, colorsForBoxes, clickXY, closestLine, orth, corners, endOfBoxX, endOfBoxY)

#Delete Box Tool Function
def deleteBox(boxes, colorsForBoxes):
    instructions("Click on the front of a box to delete the box.")
    newX, newY = mousePressed()
    
    #Check which box was clicked on starting from the last box drawn:
    for i in range(len(boxes)-1, -1, -1):
        if newX >= boxes[i][2][0] and newX <= boxes[i][2][2] and newY >= boxes[i][2][1] and newY <= boxes[i][2][5]:
            del boxes[i]
            break
    redrawScreen(boxes, colorsForBoxes)
            
#Bring Forward Box Tool Function
def bringFowardBox(boxes, colorsForBoxes):
    instructions("Click on front of box to bring it forward.")
    newX, newY = mousePressed()
    
    #Creating a varible to start which box should be brought foward
    boxToBringForward = []
    
    #Check which box was clicked on starting from the last box drawn:    
    for i in range(len(boxes)-1, -1, -1):
        if newX >= boxes[i][2][0] and newX <= boxes[i][2][2] and newY >= boxes[i][2][1] and newY <= boxes[i][2][5]:
            boxToBringForward = boxes[i]
            del boxes[i]
            break
        
    #Add the box back to the list boxes so that box will be drawn on top:
    if boxToBringForward != []:
        boxes += [boxToBringForward]
    redrawScreen(boxes, colorsForBoxes) 
    
#Send Backward Box Tool Function
def sendBackwardBox(boxes, colorsForBoxes):
    instructions("Click on FRONT of box to send it backward")
    newX, newY = mousePressed()
    #Check which box was clicked on and create varible to store the box:
    boxToSendBack = []    
    for i in range(len(boxes)-1, -1, -1):
        if newX >= boxes[i][2][0] and newX <= boxes[i][2][2] and newY >= boxes[i][2][1] and newY <= boxes[i][2][5]:
            boxToSendBack = boxes[i]
            del boxes[i]
            #Put this box in the front of list boxes so it will be drawn underneath:
            boxes = [boxToSendBack] + boxes
            break     
    redrawScreen(boxes, colorsForBoxes) 
    return boxes 
    
#Shuffle boxes
def shuffleBox(boxes, colorsForBoxes):
    for i in range(len(boxes)):
        #Choose a random number to shuffle the sides by:
        yShuffle = random.randint(-50, 50)
        xShuffle = random.randint(-50, 50)
        
        for j in range(len(boxes[i])):
            # The i represents the box, the j represents the side, the third index represents the x or y coordinates of the side 
            # For each x and y coordinate, move it by the amout set by xShuffle/yShuffle:
        
            boxes[i][j][0] = boxes[i][j][0] + xShuffle
            boxes[i][j][2] = boxes[i][j][2] + xShuffle
            boxes[i][j][4] = boxes[i][j][4] + xShuffle
            boxes[i][j][6] = boxes[i][j][6] + xShuffle
            
            boxes[i][j][1] = boxes[i][j][1] + yShuffle
            boxes[i][j][3] = boxes[i][j][3] + yShuffle            
            boxes[i][j][5] = boxes[i][j][5] + yShuffle        
            boxes[i][j][7] = boxes[i][j][7] + yShuffle 
              
    redrawScreen(boxes, colorsForBoxes)
   
# Main function
def main():
    boxes = []
    colorsForBoxes = [] 

    Draw.show()
    while True:
    
        toolBox()
                
        #Record where the user clicks in game 
        if Draw.mousePressed():
            newX = Draw.mouseX()
            newY = Draw.mouseY()
        
            #If the user clicked on "New Box":
            if newX >= 55 and newX <= 255 and newY >= 710 and newY <= 770:
                newBox(boxes, colorsForBoxes)              

            #If the user clicked on "Delete Box":                 
            elif newX >= 275 and newX <= 475 and newY >= 710 and newY <= 770:
                deleteBox(boxes, colorsForBoxes)
            
            #If the user clicked on "Shuffle":                                 
            elif newX >= 495 and newX <= 695 and newY >= 710 and newY <= 770:
                shuffleBox(boxes, colorsForBoxes)
                
            #If the user clicked on "Bring Forward":                 
            elif newX >= 715 and newX <= 915 and newY >= 710 and newY <= 770:
                bringFowardBox(boxes, colorsForBoxes)
            
            #If the user clicked on "Send Backward":    
            elif newX >= 935 and newX <= 1135 and newY >= 710 and newY <= 770:
                boxes = sendBackwardBox(boxes, colorsForBoxes)
                
        Draw.show()
              
main()
    
