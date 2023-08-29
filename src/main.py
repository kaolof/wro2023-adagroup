# Importando las librerias
import cyberpi, mbuild, mbot2, event, time, random, time
# Declarando las variables de los motores
left = "EM1"
right = "EM2"
# Definiendo activadores
number = True
color_1 = 0
color_2 = 0
turnR = True
turnL = True
# Inicializando el evento
@event.is_press('b')
def pressed():
    global color_1, color_2, turnR, turnL
    mbuild.smart_camera.open_light(1)
    while True:
        # Mostrar el contador de lineas
        cyberpi.display.show_label(color_1, 16, "center", index= 0)
        cyberpi.display.show_label(color_2, 16, "bottom_mid", index= 1)
        
        # El carro gira sentido horario
        if mbuild.quad_rgb_sensor.is_color("red","any",1) and color_1 >= 0 and color_2 == 0 and turnR:
            color_1 += 1
            mbot2.EM_stop(left)
            mbot2.EM_set_speed(9,right)
            time.sleep(1)
            mbot2.EM_stop(right)
            turnR = False
            cyberpi.display.show_label(color_1, 16, "center", index= 0)
            cyberpi.display.show_label(color_2, 16, "bottom_mid", index= 1)

        elif mbuild.quad_rgb_sensor.is_color("white","any",1) and color_1 >= 1 and color_2 == 0 :
            color_1 += 1

        else:
            mbot2.EM_stop(right)
            mbot2.EM_set_speed(200, left)
            if color_1 >= 12:
                mbot2.EM_set_speed(200,left)
                time.sleep(3)
                mbot2.EM_stop(left)
                break
