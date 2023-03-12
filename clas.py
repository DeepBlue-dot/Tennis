from tkinter import *
from time import *


def vs(racket_text, rackets):
    if racket_text['text'] == ' Human ':
        racket_text['text'] = 'Computer'
        rackets.controller = 'c'
    else:
        racket_text['text'] = ' Human '
        rackets.controller = 'h'
    pass


bg = 'black'
window = Tk()


class Ball:
    def __init__(self, canvas, x, y, d, x_velocity, y_velocity, color):
        self.canvas = canvas
        self.ball = canvas.create_oval(x, y, x+d, y+d, fill=color)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.x = x
        self.y = y
        self.d = d
        self.color = color

    def move_ball(self, red, blue, button):
        button['text'] = 'Pause'
        racket_red = self.canvas.coords(red.racket)
        racket_blue = self.canvas.coords(blue.racket)
        coordinate = self.canvas.coords(self.ball)
        center = (coordinate[1] + coordinate[3]) / 2

        if racket_red[1] < center < racket_red[3] and racket_red[0] < coordinate[0]-4 < racket_red[2] or \
                racket_blue[1] < center < racket_blue[3] and racket_blue[0] < coordinate[2]+4 < racket_blue[2]:
            self.x_velocity = -self.x_velocity

        if coordinate[3] >= self.canvas.winfo_height()-5 or coordinate[1] <= 5:
            self.y_velocity = -self.y_velocity

        self.canvas.move(self.ball, self.x_velocity, self.y_velocity)
        self.canvas.update()
        window.update()


    def delete(self):
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_oval(self.x, self.y, self.x + self.d, self.y + self.d, fill=self.color)
        self.canvas.update()

    def resat(self, button, red, blue):
        red.centre()
        blue.centre()
        button['text'] = 'Start'
        red.label.config(text=0)
        blue.label.config(text=0)
        blue.score = 0
        red.score = 0
        self.delete()
        self.canvas.update()
        window.update()

    def goal(self, red, blue, button, points, w_red, w_blue):
        coordinate = self.canvas.coords(self.ball)

        if coordinate[2] >= self.canvas.winfo_width() + 12:
            self.x_velocity = -self.x_velocity

            if red.score < points:
                button['text'] = 'Start'
                red.score += 1
                red.label['text'] = red.score
                red.centre()
                blue.centre()
                self.delete()
                window.update()
            else:
                self.resat(button, red, blue)
                red_winner = self.canvas.create_image(615, 300, image=w_red)
                window.update()
                sleep(6)
                self.canvas.delete(red_winner)
            return False

        elif coordinate[0] <= -12:
            self.x_velocity = -self.x_velocity
            if blue.score < points:
                button['text'] = 'Start'
                blue.score += 1
                blue.label['text'] = blue.score
                red.centre()
                blue.centre()
                self.delete()
                window.update()
            else:
                self.resat(button, red, blue)
                blue_winner = self.canvas.create_image(615, 300, image=w_blue)
                window.update()
                sleep(6)
                self.canvas.delete(blue_winner)
            return False

        return True


class Racket:
    def __init__(self, canvas, x, y, c_velocity, h_velocity, controller, direction, scores, color, racket1):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas
        self.racket = canvas.create_rectangle(self.x, self.y, self.x + 12, self.y + 120, fill=self.color[0])
        self.c_velocity = c_velocity
        self.h_velocity = h_velocity
        self.controller = controller
        self.direction = direction
        self.score = scores
        self.label = Label(window, text=self.score, font=("consolas", 80), bg=bg, fg=color[0])
        self.swicth = Button(window, text='Computer',
                             font=("consolas", 15),
                             image=racket1,
                             activeforeground='black',
                             activebackground=self.color[1],
                             compound='left', bg=self.color[1],
                             command=lambda: vs(self.swicth, self), relief=RAISED)

    def centre(self):
        self.canvas.delete(self.racket)
        self.racket = self.canvas.create_rectangle(self.x, self.y, self.x + 12, self.y + 120, fill=self.color[0])
        self.canvas.update()

    def move(self, direction, ball):
        coordinate = self.canvas.coords(self.racket)
        if self.controller == 'h' and self.direction == ball.x_velocity:
            if not (coordinate[1] <= 10) and direction == 'up':
                self.canvas.move(self.racket, 0, -self.h_velocity)
            if not (coordinate[3] >= self.canvas.winfo_height()) and direction == 'down':
                self.canvas.move(self.racket, 0, self.h_velocity)
            self.canvas.update()
            window.update()

    def ai(self, ball):
        coordinate = self.canvas.coords(self.racket)
        center = (coordinate[1] + coordinate[3]) / 2
        if self.controller == 'c' and self.direction == ball.x_velocity:
            coordinate_ball = self.canvas.coords(ball.ball)
            ball_center = (coordinate_ball[1] + coordinate_ball[3])/2
            if not (coordinate[3] >= self.canvas.winfo_height()) and center < ball_center:
                self.canvas.move(self.racket, 0, self.c_velocity)

            elif not (coordinate[1] <= 10) and center > ball_center:
                self.canvas.move(self.racket, 0, -self.c_velocity)
            self.canvas.update()
            window.update()
