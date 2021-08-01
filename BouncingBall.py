import turtle;
import random;
import keyboard;

wn = turtle.Screen();
wn.bgcolor("black");
wn.title("Bouncing Ball Sim");
n = 30;
wn.tracer(n);

balls = [];
x = 50;

for _ in range(x):
    balls.append(turtle.Turtle());

colors = ["red","blue","yellow","orange","green","white","purple"];
shapes = ["circle","triangle","square"];

for ball in balls:
    ball.shape(random.choice(shapes));
    ball.color(random.choice(colors));
    ball.penup();
    ball.speed(30);
    x = random.randint(-290,290);
    y = random.randint(200,250);
    ball.goto(x,y);
    ball.dy = 0.00000000000000000000001;
    ball.dx = random.randint(-2,2);
    ball.da= random.randint(-5,5);

gravity = 0.1;


while True:

    wn.update();
    
    for ball in balls:
        ball.rt(ball.da);
        ball.dy -=gravity;
        ball.sety(ball.ycor()+ball.dy);

        ball.setx(ball.xcor()+ball.dx);

        #check for a wall collision
        if ball.xcor() > 280:
            ball.dx *= -1;
            ball.da*=-1;

        if ball.xcor() < -280:
            ball.dx *= -1;
            ball.da*=-1;

        #Check for a bounce
        if ball.ycor()<-250:
            ball.dy*=-1;
            ball.da*=-1;
            ball.sety(-200);

        if ball.ycor()>250:
            ball.dy*=-1;
            ball.da*=-1;
            ball.sety(240);

        if keyboard.is_pressed('ESC'):
            exit(0);

        if keyboard.is_pressed('SPACE'):
            ball.color(random.choice(colors));
        else:
            continue;
   

    #Check for collisions between balls
    for i in range(0,len(balls)):
        for j in range(i+1,len(balls)):
                #check for a collision
                if balls[i].distance(balls[j]) < 20:
                       balls[i].color(random.choice(colors));
                       balls[j].color(random.choice(colors));
                       balls[j].shape(random.choice(shapes));
                       balls[j].shape(random.choice(shapes));
                       tempDx = balls[i].dx;
                       tempDy = balls[i].dy;

                       balls[i].dx = balls[j].dx;
                       balls[i].dy = balls[j].dy;

                       balls[j].dx = tempDx;
                       balls[j].dy = tempDy;
                       


    

wn.mainloop();
raw_input("promt: ");

