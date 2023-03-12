from clas import *
from tkinter import messagebox

points = 10
up = ' '
down = ' '
pause = True

speed = [[5, 7], [7, 20]]
coordinates = [[572, 295, 20], [15, 245], [1140, 245]]


def disable_active(active):
    if active:
        racket_red.swicth.config(state=ACTIVE)
        racket_blue.swicth.config(state=ACTIVE)
        single.config(state=ACTIVE)
        double.config(state=ACTIVE)

    else:
        racket_red.swicth.config(state=DISABLED)
        racket_blue.swicth.config(state=DISABLED)
        single.config(state=DISABLED)
        double.config(state=DISABLED)


def opening():
    welcome = Label(window, text='PONG',
                    font=("consolas", 200),
                    pady=150, padx=200, bg='blue',
                    fg='white', width=1400, height=700)
    welcome.pack()
    window.update()
    sleep(6)
    welcome.destroy()


def run():
    disable_active(False)
    while ball.goal(racket_red, racket_blue, start, points, red_win, blue_win) and pause:
        ball.move_ball(racket_red, racket_blue, start)
        racket_red.ai(ball)
        racket_blue.ai(ball)
        cort.tag_raise(racket_red.racket)
        cort.tag_raise(racket_blue.racket)
        cort.update()
        sleep(0.009)
        window.update()


def quite():
    if messagebox.askyesno(title='Exit', message='Do You Want To Quite?'):
        window.destroy()
    else:
        pass


def new_game():
    global pause, up, down
    disable_active(True)
    up = ' '
    down = ' '
    pause = False
    ball.resat(start, racket_red, racket_blue)
    pass


def start_paues():
    global up, down
    global pause
    if start['text'] == 'Start':
        start['text'] = 'Pause'
        up = 'up'
        down = 'down'
        pause = True
        run()
    else:
        start['text'] = 'Start'
        up = ' '
        down = ' '
        pause = False
    pass


def point():
    global points
    if y.get() == 0:
        points = 10
    elif y.get() == 1:
        points = 20
    pass


def vs(racket_text, rackets):
    if racket_text['text'] == ' Human ':
        racket_text['text'] = 'Computer'
        rackets.controller = 'c'
    else:
        racket_text['text'] = ' Human '
        rackets.controller = 'h'
    pass


window.title('Pong')
window.geometry('1360x650')
window.attributes('-fullscreen', True)
window.config(bg=bg)

window.bind('<Up>', lambda event: racket_blue.move(up, ball))
window.bind('<Down>', lambda event: racket_blue.move(down, ball))
window.bind('<w>', lambda event: racket_red.move(up, ball))
window.bind('<s>', lambda event: racket_red.move(down, ball))
window.bind('<space>', lambda event: start_paues())
window.bind('<Escape>', lambda event: quite())

racket1 = PhotoImage(file='/home/yeabsira/MyProjects/pythonProject/image/racket1.png')
racket2 = PhotoImage(file='/home/yeabsira/MyProjects/pythonProject/image/racket2.png')
red_win = PhotoImage(file='/home/yeabsira/MyProjects/pythonProject/image/red.png')
blue_win = PhotoImage(file='/home/yeabsira/MyProjects/pythonProject/image/blue.png')
cort_image = PhotoImage(file='/home/yeabsira/MyProjects/pythonProject/image/cor.png')
y = IntVar()


cort = Canvas(window, width=1150, height=600, bd=5, relief=SOLID)
cort.create_image(7, 7, image=cort_image, anchor=NW)
ball = Ball(cort, coordinates[0][0], coordinates[0][1], coordinates[0][2], speed[0][0], speed[0][1], 'yellow')
racket_red = Racket(cort, coordinates[1][0], coordinates[1][1], speed[1][0], speed[1][1], 'c', -speed[0][0], 0, ['red','red'], racket1)
racket_blue = Racket(cort, coordinates[2][0], coordinates[2][1], speed[1][0], speed[1][1], 'c', speed[0][0], 0, ['blue','#3792cb'], racket2)


start = Button(window, text="Start", font=("consolas", 15), padx=10, command=lambda: start_paues(), relief=RAISED)
new = Button(window, text="New Game", font=("consolas", 15), padx=10, command=lambda: new_game(), relief=RAISED)
getout = Button(window, text="Exit", font=("consolas", 15), padx=10, command=quite, relief=RAISED)

single = Radiobutton(window, text='Single',
                     font=("consolas", 15),
                     bg=bg, fg='green',
                     activebackground=bg,
                     activeforeground='green',
                     variable=y, value=0,
                     command=point)
double = Radiobutton(window, text='Double',
                     font=("consolas", 15),
                     bg=bg, fg='green',
                     activebackground=bg,
                     activeforeground='green',
                     variable=y, value=1,
                     command=point)


cort.place(x=20, y=20)
new.place(x=1200, y=170)
single.place(x=1200, y=230)
double.place(x=1200, y=270)
racket_red.swicth.place(x=1200, y=320)
racket_blue.swicth.place(x=1200, y=380)
racket_red.label.place(x=400, y=640)
start.place(x=575, y=650)
getout.place(x=580, y=700)
racket_blue.label.place(x=750, y=640)

window.mainloop()
