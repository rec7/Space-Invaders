import turtle
import os
import math


#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


#Border
class Border:
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)

    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)

    border_pen.hideturtle()


#Player
class Player:
    player = turtle.Turtle()
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    playerSpeed = 15

class PlayerWeapon:
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    bulletSpeed = 20

#Ready state
bulletState = "ready"



#Player Control
class PlayerControl:
    x = Player.player.xcor()

    def move_left():
        PlayerControl.x -= Player.playerSpeed
        if PlayerControl.x < -280:
            PlayerControl.x = -280
        Player.player.setx(PlayerControl.x)

    def move_right():
        PlayerControl.x += Player.playerSpeed
        if PlayerControl.x > 280:
            PlayerControl.x = 280
        Player.player.setx(PlayerControl.x)

    def fire_bullet():
        #Bullet declaired as global
        global bulletState
        if bulletState == "ready":
            bulletState = "fire"
            #Move bullet to above player
            x = Player.player.xcor()
            y = Player.player.ycor() + 10
            PlayerWeapon.bullet.setposition(x, y)
            PlayerWeapon.bullet.showturtle()

    def isColliding(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

        if distance < 15:
            return True
        else:
            return False

    def move_binds():
        turtle.listen()
        turtle.onkey(PlayerControl.move_left, "Left")
        turtle.onkey(PlayerControl.move_right, "Right")
        turtle.onkey(PlayerControl.fire_bullet, "space")

    
PlayerControl.move_binds()


#Enemy
class Enemy:
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200, 250)

    enemySpeed = 2


#Main Loop
class Main:
    isRunning = True

    while isRunning:
        
        #Move enemy
        x = Enemy.enemy.xcor()
        x += Enemy.enemySpeed
        Enemy.enemy.setx(x)

        #Move Bullet
        if bulletState == "fire":
            y = PlayerWeapon.bullet.ycor()
            y += PlayerWeapon.bulletSpeed
            PlayerWeapon.bullet.sety(y)

        #Boundary check
        def BounaryCheck():
            global bulletState

            if Enemy.enemy.xcor() > 280:
                y = Enemy.enemy.ycor()
                y -= 40

                Enemy.enemySpeed *= -1
                Enemy.enemy.sety(y)
                

            if Enemy.enemy.xcor() < -280:
                y = Enemy.enemy.ycor()
                y -= 40

                Enemy.enemySpeed *= -1
                Enemy.enemy.sety(y)

            if PlayerWeapon.bullet.ycor() > 275:
                PlayerWeapon.bullet.hideturtle()
                bulletState = "ready"

            #Bullet and enemy collision
            if PlayerControl.isColliding(PlayerWeapon.bullet, Enemy.enemy):
                #Reset bullet
                PlayerWeapon.bullet.hideturtle()
                bulletState = "ready"
                PlayerWeapon.bullet.setposition(0, -400)

                #Reset enemy
                Enemy.enemy.setposition(200, -200)

        BounaryCheck()

    delay = input("Press enter to finish.")

