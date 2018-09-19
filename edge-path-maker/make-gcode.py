import Edge_Detection

scale_factor = 10

def makeGCode(edges, width, height):
    commands = []
    oldpoint = (0,0)
    commands += ["G21 (set to mm units)\n"]
    #commands += ["$22=1 $23=2(home)\n"] # this probably needs to be fixed
    for edge in edges:
        #commands += ["G1 X0 Y0 Z5"]
        i = 0
        for i in range(0, len(edge) - 2, 2):
            point = edge[i]
            x = point[0]# - oldpoint[0]
            y = point[1]# - oldpoint[1]
            commands += ["G91 G0 " + "X" + str((x - oldpoint[0])/scale_factor) + " " + "Y" + str((y - oldpoint[1])/scale_factor)]
            oldpoint = point
        #commands += ["G1 X0 Y0 Z5"]
        for i in range(len(edge)-2, len(edge)):
            point = edge[i]
            x = point[0]# - oldpoint[0]
            y = point[1]# - oldpoint[1]
            commands += ["G91 G0 " + "X" + str((x - oldpoint[0])/scale_factor) + " " + "Y" + str((y - oldpoint[1])/scale_factor)]
            oldpoint = point

    return commands

def writeToFile(fileName, gcode):
    fin = open(fileName, "w+")
    for line in gcode:
        fin.write("%s\n" % line)
    fin.close()

if __name__ == '__main__':
    imgName = input("Image name: ")
    fileName = input("GCode file name: ")
    raw_drawing, width, height = Edge_Detection.prepEdgePainter(imgName)
    gcode = makeGCode(raw_drawing, width, height)
    writeToFile(fileName, gcode)
