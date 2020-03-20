
#LOGIC FOR MAZE GENERATOR

# let c be a list of cells, initially empty 
# add a random cell to c  
#
   #repeat until list c is empty

	# 1) choose a cell from c at random.
	#	2) if cell has unvisited neigbours.
	#	   carve a path to it from cell to neighbour
	#	   add neighbour to list c
	#
	#	3) if cell doesnt have neigbours.
	#	   remove cell from list c
#
#
#

from PIL import Image,ImageDraw	
import random 

cellRowCount = 500
cellColCount = 500
canvas_width  =  cellColCount * 5
canvas_height =  cellRowCount * 5
img = Image.new(mode = 'RGB',size = (canvas_width,canvas_height))


#draw grid
img1 = ImageDraw.Draw(img)
img1.line(((canvas_width-1,0),(canvas_width-1,canvas_height)),fill = 'white',width = 0)           #execption cases 
img1.line(((0,canvas_height-1),(canvas_width,canvas_height-1)),fill = 'white',width = 0 )
for i in range(cellRowCount):
	shape = [(0,i*(canvas_height/cellRowCount)),(canvas_width,i*(canvas_height/cellRowCount))]
	img1.line(shape,fill = 'white',width = 0)
for i in range(cellColCount):
	shape = [(i*(canvas_width/cellColCount),0),(i*(canvas_width/cellColCount),canvas_height)]
	img1.line(shape,fill = 'white',width = 0)			
			
	
grid = [[False for i in range(cellColCount)]for j in range(cellRowCount)] #False = not visited, True = visited


#START OF MAZE MAKER ALGORITHM 
def carvePath(start,end):
	if start[1] > end[1]:
		#draw path above start cell 
		shape = [(((canvas_width/cellColCount)*start[0])+1,(canvas_height/cellRowCount)*start[1]),(((canvas_width/cellColCount)*(start[0]+1)),(canvas_height/cellRowCount)*start[1])]
		img1.line(shape,fill = 'black',width = 0)

	elif start[1] < end[1]:
		#draw path below start cell 
		shape = [(((canvas_width/cellColCount)*start[0]),(canvas_height/cellRowCount)*(start[1]+1)),(((canvas_width/cellColCount)*(start[0]+1)),(canvas_height/cellRowCount)*(start[1]+1))]
		img1.line(shape,fill = 'black',width = 0)

	elif start[0] > end[0]:
		#draw path left of start cell 
		shape = [(((canvas_width/cellColCount)*start[0]),(canvas_height/cellRowCount)*start[1]),(((canvas_width/cellColCount)*start[0]),(canvas_height/cellRowCount)*(start[1]-1))]
		img1.line(shape,fill = 'black',width = 0)
	
	else:
		#draw path right of start cell 
		shape = [(((canvas_width/cellColCount)*(start[0]+1)),(canvas_height/cellRowCount)*(start[1]+1)),(((canvas_width/cellColCount)*(start[0]+1)),(canvas_height/cellRowCount)*(start[1]))]
		img1.line(shape,fill = 'black',width = 0)



#checks neighbouring cells if visited or not then returns random cell 
def checkNear(cell):
	x = cell[0]
	y = cell[1]
	nearCells = []
	if y>0:
		if grid[y-1][x] == False:
			nearCells.append([x,y-1])
	if y<cellRowCount-1:
		if grid[y+1][x] == False:
			nearCells.append([x,y+1])
	if x<cellColCount-1:
		if grid[y][x+1] == False:
			nearCells.append([x+1,y])
	if x>0:	
		if grid[y][x-1] == False:
			nearCells.append([x-1,y])
	
	if nearCells == []:
		return None
	randomcell  = random.choice(nearCells)
	return randomcell 
	
#main code 
c = []
x = random.randrange(0,cellColCount)
y = random.randrange(0,cellRowCount)
cell = [x,y]
grid[y][x] = True
c.append(cell)


while len(c)>0:
	randomCell = random.choice(c)
	Near = checkNear(randomCell)
	if Near == None:
		c.remove(randomCell)
	else:
		grid[Near[1]][Near[0]] = True  #sets variable to true means cell has been visited
		c.append(Near)	
		carvePath(randomCell,Near)
		
img.show()

img.save('maze.png')

