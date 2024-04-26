from machine import Pin
from time import sleep, sleep_ms
import time

#Pines del semaforo 1

semaforoverde1= Pin (22,Pin.OUT)
semaforoamarillo1= Pin (23,Pin.OUT)
semafororojo1= Pin (21,Pin.OUT)

#Pines del semaforo 2

semaforoverde2= Pin (19,Pin.OUT)
semaforoamarillo2= Pin (18,Pin.OUT)
semafororojo2= Pin (17,Pin.OUT)

#Pines del semaforo 3

semaforoverde3= Pin (5,Pin.OUT)
semaforoamarillo3= Pin (16,Pin.OUT)
emafororojo3= Pin (4,Pin.OUT)

#Pines del semaforo 4

semaforoverde4= Pin (12,Pin.OUT)
semaforoamarillo4= Pin (14,Pin.OUT)
semafororojo4= Pin (27,Pin.OUT)

# Inicio del semaforo 1

def semaforo1():
    semafororojo1.value(1)
    semafororojo2.value(1)
    semaforoamarillo1.value(0)
    semaforoverde1.value(0)
    time.sleep(2) # Tiempo  que tarda de cambiar de un color a otro
    
    semafororojo1.value(0)
    semaforoverde1.value(1)
    time.sleeo(2) # Tiempo  que tarda de cambiar de un color a otro
    
    semaforoverde1.value(0)
    semaforoamarillo1.value(1)
    time.sleep(2) # Tiempo  que tarda de cambiar de un color a otro
    semaforoamarillo1.value(0)
    semafororojo1.value(1)
    
# Inicio del semaforo 2

def semaforo2():
    semafororojo2.value(1)
    semaforoamarillo2.value(0)
    semaforoverde2.value(0)
    time.sleep(2) # Tiempo  que tarda de cambiar de un color a otro
    
    semafororojo2.value(0)
    semaforoverde2.value(1)
    time.sleep(2) # Tiempo  que tarda de cambiar de un color a otro
    semaforoverde2.value(0)
    semaforoamarillo2.value(1)
    time.sleep(2) # Tiempo  que tarda de cambiar de un color a otro
    semaforoamarillo2.value(0)
    semafororojo2.value(1)
    
# Pin de nuestro led que dara la señal del cruze peatonal
    
def boton_peatonal_interrupt(pin):
    cruzeled1 = Pin (2,Pin.OUT) # Led que dara la señal para el cruze de los peantones
    sleep(.2)
    cruzeled1.value(1)
    sleep(.2)
    cruzeled1.value(0)
    sleep(.2)
    cruzeled1.value(1)
    sleep(.2)
    cruzeled1.value(0)
    sleep(.2)
    semafororojo1.value(1) # El semaforo rojo se detiene
    semaforoamarillo1.value(0)
    semaforoverde1.value(0)
    
# Boton del cruze peatonal estetendra una secuencia infinita

Pin(35,Pin.IN).irq(trigger=Pin.IRQ_FALLING, handler = boton_peatonal_interrupt)
while True:
    semaforo1()
    sleep(.5)
    semaforo2()
    sleep(.5)
    