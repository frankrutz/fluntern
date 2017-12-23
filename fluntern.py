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
    mc.setBlocks(0,0,0  ,15,9,-28 ,1)

def makeUebergang():
    mc.setBlocks(16,3,-4  ,50,5,-12 ,1)
    for x in range(0, 4):
        mc.setBlocks(22+x*7,0, -4 ,22+x*7,2, -4 ,1 )
        mc.setBlocks(22+x*7,0,-12 ,22+x*7,2,-12 ,1 ) 
    
def makeSchulhaus():
    mc.setBlocks(51,0,0   ,69,12,-60 ,1)#Gebäudekörper Schulhaus, massiv, stone
    mc.setBlocks(59,1,0   ,61,2,2    ,0)#Haupteingang
    mc.setBlocks(52,1,-1  ,68,3,-59  ,0)#Erdgeschoss mit Luft füllen
    mc.setBlocks(52,5,-1  ,68,7,-59  ,0)#1.OG mit Luft füllen
    mc.setBlocks(52,9,-1  ,68,11,-59 ,0)#2.OG mit Luft füllen


    mc.setBlocks(70,0,-5  ,77,12,-15 ,1)#Treppenhaus massiv, stone
    mc.setBlocks(69,1,-6  ,76,11,-14 ,0)#Treppenhaus mit Luft füllen
    mc.setBlocks(70,1,-6  ,77,1,-8   ,1)#Treppe EG zum 1.OG
    mc.setBlocks(76,2,-9  ,74,2,-14  ,1)
    mc.setBlocks(69,3,-14 ,73,3,-11  ,1)


def makeFussballplatz():
    mc.setBlocks(15,0,9  ,65,1,9  ,1)#Mauer zur Schule hin, stone
    mc.setBlocks(15,0,10 ,65,1,11 ,3)#Mauer zur Schule hin, dirt
    
    mc.setBlocks(15,0,12 ,65,2,12 ,1)#Mauer zum Fussballplatz hin, stone
    mc.setBlocks(34,3,12 ,61,7,12,85)#Gitter auf Mauer
    
    mc.setBlocks(61,0,13 ,61,2,28 ,1)#Mauer Fussballplatz-Parkplatz stone
    mc.setBlocks(61,3,13 ,61,7,28,85)#Gitter auf Mauer


    mc.setBlocks(34,0,13 ,34,2,55 ,1)#Mauer Fussballplatz Richtung Tram
    mc.setBlocks(34,3,13 ,34,7,55,85)#Gitter auf Mauer
    
    mc.setBlocks(60,0,55 ,34,2,55 ,1)#Mauer Fussballplatz Richtung Berg
    mc.setBlocks(60,3,55 ,34,7,55,85)#Gitter auf Mauer
    
    mc.setBlocks(60,1,13 ,35,1,55 ,2)#Grund Fussballplatz, gras
    makeTree(40,1,65)


def makeTurnhalle():
    mc.setBlocks(65,0,32  ,100,9,55 ,1)#Turnhalle Hauptteil
    mc.setBlocks(68,0,31  ,103,4,27 ,1)#Turnhalle Vorbau

     

#########################################################################################

initWorld()
makeFluntern()
makeHort()
makeUebergang()
makeSchulhaus()
makeFussballplatz()
makeTurnhalle()
printCoordinateSystem()
mc.player.setTilePos(60, 1, 3) #Spieler vor den Haupteingang stellen

