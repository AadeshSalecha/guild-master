import turtle
import cv2
import Edge_Detection
import numpy as np


def makeTurtle(edges, width, height):
    turtle.setup(width = width, height = height)
    wn = turtle.Screen()
    turtle.tracer(0,0)
    turtle.penup()
    for edge in edges:
        for point in edge:
            turtle.goto(point[0] - width/2, -point[1] + height/2)
            turtle.pendown()
        turtle.penup()
    turtle.update()
    turtle.exitonclick()

# Not working yet
def testEdges(imageName):
    img = cv2.imread(imageName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    def changeThreshold(threshold):
        #threshold = cv2.getTrackbarPos("bar", "test")
        raw_drawing, width, height = Edge_Detection.prepEdgePainter(imageName, threshold)
        img = np.array(raw_drawing)
        cv2.imshow("test", img)
        cv2.waitKey(0)
    cv2.namedWindow("test")
    cv2.createTrackbar("bar", "test", 0, 500, changeThreshold)
    cv2.imshow("test", img)
    cv2.waitKey(0)




if __name__ == "__main__":
    imgName = input("Input name of image to be drawn: ")
    raw_drawing, width, height = Edge_Detection.prepEdgePainter(imgName, 100)
    makeTurtle(raw_drawing, width, height)