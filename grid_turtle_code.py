import turtle
#-500,330,30,10,10
def goto_grid(t,x,y, id):
    t.teleport(-500 + 30 * x + -15,330 - 30 * y + -15)
    id = [x,y]
    return id

def move_grid(t,x,y,id):
    t.teleport(t.xcor()+(30*x),t.ycor()+(30*x))
    id[0] += x
    id[1] += y
    return id



def draw_boarder(t,grid_size,edge):
    for _ in range(edge+1):
        t.stamp()
        t.forward(grid_size)
    t.right(90)

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
'''
    draw_boarder(t,num_collums,grid_size)
    draw_boarder(t,num_rows,grid_size)
    draw_boarder(t,num_collums,grid_size)
    draw_boarder(t,num_rows,grid_size)
'''

