import turtle
import grid_turtle_code

"""
this code handles drawing the main game grid, moving objects on the game grid, and highligtning squares
"""

t = turtle.Turtle(visible=False)
t.shape("square")
t.turtlesize(.9)
t.color("red")
t.speed(0)

def goto_grid(t,x,y, id=[0,0]):
    t.teleport(-500 + 30 * x + -15,330 - 30 * y + -15)
    id = [x,y]
    turtle.update()
    return id

def move_grid(t,x,y,id=[0,0]):
    t.teleport(t.xcor()+(30*x),t.ycor()+(30*y))
    id[0] += x
    id[1] -= y
    turtle.update()
    return id

def highlight_squares(type="raw",squares=[], size=1,start_posistion=(0,0),include_keys=False):
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
                        t.write("A",font=("arial", 8, "bold"))
                    if j == 2:
                        t.write("S",font=("arial", 8, "bold"))
                    if j == 3:
                        t.write("D",font=("arial", 8, "bold"))
                    t.color("red")
            t.backward(30*size)
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
            grid_turtle_code.goto_grid(t,start_posistion[0],start_posistion[1])
            t.right(90)
    turtle.update()
            
def clear_highlingting():
    t.clear()
    

def draw_grid(t,grid_size,num_rows,num_collums,start_x,start_y):
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
'''
    draw_boarder(t,num_collums,grid_size)
    draw_boarder(t,num_rows,grid_size)
    draw_boarder(t,num_collums,grid_size)
    draw_boarder(t,num_rows,grid_size)
'''

