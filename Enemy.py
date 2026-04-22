import turtle
import random
import grid_turtle_code
import time
import player_controller


class enemy_class:
    def __init__(self, terrain):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.selector = random.randint(1,4)
        if self.selector == 1 or self.selector == 2:
            self.t.shape("circle")
            self.t.color("red")
            self.health = 10
            self.speed = 3
            self.damage = 5
            self.type = 1
        elif self.selector == 3:
            self.t.shape("triangle")
            self.t.color("red")
            self.health = 6
            self.speed = 5
            self.damage = 5
            self.type = 2
        elif self.selector == 4:
            self.t.shape("square")
            self.t.color("red")
            self.health = 15
            self.speed = 3
            self.damage = 10
            self.type = 3
        self.terrain = terrain
        self.last_move = [-1,-1]
        self.spawn()
        self.display_health()
    def spawn(self):
        self.location = grid_turtle_code.goto_grid(self.t,random.randint(2,32),random.randint(2,15),id=[0,0])
        while self.location in self.terrain:
            self.location = grid_turtle_code.goto_grid(self.t,random.randint(2,32),random.randint(2,15),id=[0,0])
    
    def display_health(self):
        if self.health <= 0:
            self.t.clear
        else:
            self.t.clear()
            self.t.penup()
            self.t.color("purple")
            self.t.sety(self.t.ycor() + 10)
            self.t.write(self.health,align="center")
            self.t.sety(self.t.ycor() - 10)
            self.t.color("Red")
        turtle.update()
        
    def take_damage(self, attack_list, take_damage):
        for i in attack_list:
            if self.location[0] == i[0] and self.location[1] == i[1]:
                print("hit")
                self.health -= take_damage
                if self.health <= 0:
                    self.die()
        self.display_health()
        
    def activate(self,player_location):
        self.t.clear()
        if self.health > 0:
            for _ in range(self.speed):
                time.sleep(.2)
                if self.last_move == self.location:
                    while self.last_move == self.location:
                        movement_choice = random.randint(1,4)
                        if movement_choice == 1:
                            self.location = grid_turtle_code.move_grid(self.t,1,0,self.location,self.terrain)
                        elif movement_choice == 2:
                            self.location = grid_turtle_code.move_grid(self.t,-1,0,self.location,self.terrain)
                        elif movement_choice == 3:
                            self.location = grid_turtle_code.move_grid(self.t,0,-1,self.location,self.terrain)
                        elif movement_choice == 4:
                            self.location = grid_turtle_code.move_grid(self.t,0,1,self.location,self.terrain)
                else:
                    self.last_move = self.location[:]
                    movement_choice = random.randint(0,1)
                    if movement_choice == 0:
                        if self.location[0] < player_location[0]:
                            self.location = grid_turtle_code.move_grid(self.t,1,0,self.location,self.terrain)
                        elif self.location[0] > player_location[0]:
                            self.location = grid_turtle_code.move_grid(self.t,-1,0,self.location,self.terrain)
                        elif self.location[1] > player_location[1]:
                            self.location = grid_turtle_code.move_grid(self.t,0,-1,self.location,self.terrain)
                        elif self.location[1] < player_location[1]:
                            self.location = grid_turtle_code.move_grid(self.t,0,1,self.location,self.terrain)
                    elif movement_choice == 1:
                        if self.location[1] > player_location[1]:
                            self.location = grid_turtle_code.move_grid(self.t,0,-1,self.location,self.terrain)
                        elif self.location[1] < player_location[1]:
                            self.location = grid_turtle_code.move_grid(self.t,0,1,self.location,self.terrain)
                        elif self.location[0] < player_location[0]:
                            self.location = grid_turtle_code.move_grid(self.t,1,0,self.location,self.terrain)
                        elif self.location[0] > player_location[0]:
                            self.location = grid_turtle_code.move_grid(self.t,-1,0,self.location,self.terrain)
                if self.location[0] == player_location[0] and self.location[1] == player_location[1] and self.health > 0:
                    player_controller.player_health(self.damage)
                    self.die()
            self.display_health()
    def die(self):
        self.health = 0
        self.t.hideturtle()
        self.display_health()