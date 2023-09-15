import cyberpi, mbuild, mbot2, event, time, random, time
# Declarando las variables de los motores
left = "EM1"
right = "EM2"
count = 0
timer = 0
h = True
# Inicializando el evento
@event.is_press('b')
def pressed():
    global count, timer, h
    cyberpi.timer.reset()
    while True:
        timer = cyberpi.timer.get()
        cyberpi.display.show_label(timer, 16, "center", index= 0)
     
        mbot2.EM_set_speed(170, left)
        if mbuild.ultrasonic2.get(1) <= 75:
            count += 1
            mbot2.EM_set_speed(120, left)
            mbot2.EM_set_speed(-7, right)
            time.sleep(1)
            mbot2.EM_stop(right)
                
            time.sleep(1.3)
    
            mbot2.EM_set_speed(6, right)
            time.sleep(1)
            mbot2.EM_stop(right)

        elif timer >= 80:
            mbot2.EM_stop(right)
            mbot2.EM_stop(left)
            break