from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#########################################################################################
def initWorld():
    mc.setBlocks(-150,0,-150   ,150,150,150 ,0)  #air
    mc.setBlocks(-150,-1,-150  ,150,0,150   ,2)  #gras - all.
#########################################################################################

######################################################################################### 
def makeStairs(x,z,y,numstairs,width): 
    for s in range(0, numstairs):
        for w in range(0,width):
             mc.setBlock(x+w,z+s,y+s,17)#stone y-koordinate
#########################################################################################
def makeTree(x,z,y):
        mc.setBlocks(x,z,y       ,x+1,z+6,y+1,  17)
        mc.setBlocks(x-3,z+6,y-4 ,x+4,z+26,y+5, 18)
#########################################################################################
def printCoordinateSystem():
    for x in range(0, 10):
         mc.setBlock(x,1,0,2)#gras x-coordinate
    for z in range(0, 10):
        mc.setBlock(0,z,0,24)#sandstone z-coordinate
    for y in range(0, 10):
         mc.setBlock(0,1,y,1)#stone y-koordinate
#########################################################################################
def makeFluntern():

    mc.setBlocks(-150,-1,-150, 150,0,150 ,1 )          #stone=street
    makeTree(110,0,5)  

#########################################################################################
def makeHort():
    mc.setBlocks(0,0,0  ,18,10,-28 ,1)

def makeUebergang():
    mc.setBlocks(18,3,-4  ,53,5,-12 ,1)
    for x in range(0, 4):
        mc.setBlocks(25+x*7,0, -4 ,25+x*7,2, -4 ,1 )
        mc.setBlocks(25+x*7,0,-12 ,25+x*7,2,-12 ,1 ) 
    
def makeSchulhaus():
    mc.setBlocks(54,0,0  ,72,18,-60 ,1)

#########################################################################################

initWorld()
makeFluntern()
makeHort()
makeUebergang()
makeSchulhaus()
printCoordinateSystem()
mc.player.setTilePos(-5, 1, -5) #Spieler vor den Hort stellen

