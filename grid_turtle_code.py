import turtle
import grid_turtle_code
import random
import copy

"""
this code handles drawing the main game grid, moving objects on the game grid, and highligtning squares
"""

t = turtle.Turtle(visible=False)
t.shape("square")
t.turtlesize(.9)
t.color("red")
t.speed(0)

def goto_grid(t,x,y, id=[0,0],terrain=None):
    block_terrain = copy.deepcopy(terrain)
    if block_terrain != None:
        for i in block_terrain:
            if id[0] + x == i[0] and id[1] + y == i[1]:
                return id
    t.teleport(-395 + (30 * x),(30 * y) - 135)
    id[0] = x
    id[1] = y
    turtle.update()
    return id

def move_grid(t,x,y,id=[0,0],terrain=None):
    block_terrain = copy.deepcopy(terrain)
    if block_terrain != None:
        for i in block_terrain:
            if id[0] + x == i[0] and id[1] + y == i[1]:
                return id
    t.teleport(t.xcor()+(30*x),t.ycor()+(30*y))
    id[0] += x
    id[1] += y
    turtle.update()
    return id

def highlight_squares(type="raw",squares=[], size=1,start_posistion=(0,0),include_keys=False,blocked_terrian=[]):
    
    t.penup()
    t.setheading(0)
    t.left(90)
    goto_grid(t,start_posistion[0],start_posistion[1])
    if type == "cross":
        for j in range(4):
            for i in range(size):
                t.forward(30)
                t.stamp()
            if include_keys == True and i == size-1:
                t.color("black")
                if j == 0:
                    t.write("W",font=("arial", 8, "bold"))
                if j == 1:
                    t.write("D",font=("arial", 8, "bold"))
                if j == 2:
                    t.write("S",font=("arial", 8, "bold"))
                if j == 3:
                    t.write("A",font=("arial", 8, "bold"))
                t.color("red")
            goto_grid(t,start_posistion[0],start_posistion[1])
            t.right(90)
    if type == "star":
        for j in range(4):
            for i in range(size):
                t.forward(30)
                t.right(90)
                t.forward(30)
                t.left(90)
                t.stamp()
            if include_keys == True and i == size-1:
                t.color("black")
                if j == 0:
                    t.write("W",font=("arial", 8, "bold"))
                if j == 1:
                    t.write("A",font=("arial", 8, "bold"))
                if j == 2:
                    t.write("S",font=("arial", 8, "bold"))
                if j == 3:
                    t.write("D",font=("arial", 8, "bold"))
                t.color("red")
            goto_grid(t,start_posistion[0],start_posistion[1])
            t.right(90)
    if type == "raw":
        for i in squares:
            goto_grid(t,i[0],i[1])
            t.stamp()
    turtle.update()
            
def clear_highlingting():
    t.clear()
    

def draw_grid(t,grid_size,num_rows,num_collums,start_x,start_y,num_obstruction):
    t.hideturtle()
    t.speed(0)
    t.shape("square")
    t.shapesize(1.8,1.8)
    t.teleport(start_x,start_y)
    
    for i in range(num_rows):
        t.teleport(start_x, start_y - (i*grid_size))
        t.forward(num_collums*grid_size)
    t.right(90)
    for i in range(num_collums + 1):
        t.teleport(start_x + (i*grid_size), start_y)
        t.forward(num_rows*grid_size-grid_size)
    t.left(90)
    t.teleport(start_x-grid_size/2, start_y+grid_size/2)
    turtle.update()
    obstruction_location = []
    t.shapesize(1.6,1.6)
    for i in range(num_obstruction):
        obstruction_location.append(goto_grid(t,random.randint(1,32),random.randint(1,15),id=[0,0]))
        t.pendown()
        t.stamp()
        t.penup()
    return obstruction_location