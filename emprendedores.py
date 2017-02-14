#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ing. en Sistemas 2017 UMG
# Proyecto: tarea para Emprendedores de negocios
# Autores:  Mauricio Garcia, Luis Fajardo, Kevin chitay, edson, jorge, y muchos mas.
# Fecha:    13/2/2017
# Version:  0.2
# Contacto: 6luiscarret@gmail.com

import time                     #Este modulo es para crear el retardo en segundos para realizar el ping.
import os                       #Este modulo nos permite ejecutar comandos del sistema, en este caso para el ping.
import smtplib                  #Este modulo nos ayuda a enviar el correo.

username = 'monitorinnova@gmail.com'
password = 'la clave:*********'

print("[*] Conectando al Servidor, porfavor espere . . .")
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()						#Iniciamos la comunicacion hacia el servidor smtp "security is not my problem jajaja"
server.login(username,password)					#se le pasa el parametro de usuario  y contrasenia




hostname = raw_input("Ingrese el host a monitorear: ")          #Aqui solicitamos la ip del host, se utiliza el raw, que se si se utiliza
                                                                #unicamente el input no deja ingresar todos los caracteres.

email = raw_input("Ingrese el correo a notificar una caida del enlace: ")       #ingresamos el mail al cual se enviara el correo

correo = 'monitor@innova.net.gt'


#mensaje que se enviara por correo
mensaje = """From: MONITORINNOVA <monitor@innova.net.gt>
MIME-Version: 1.0

Content-type: text/html
Subject: ALERTA !!!  ENLACE DOWN

<b>Se ha generado una Alerta sobre el host por favor verifique la posible falla !!

"""
mensaje = mensaje + hostname

while True:                     #iniciamos el while en True para que se ejecute siempre

    ping = os.system("ping -c 1  "+ hostname +" | grep icmp")   #Realizamos un ping con filtros y el valor se lo asignamos a la variable ping
    if ping == 0:
        print "[+] Comunicacion Exitosa"
        time.sleep(5)
    else:
        print "[!] Se ha perdido la  conexion!"
        time.sleep(5)
        server.sendmail(correo, email, mensaje)
        print("[-] Se ha enviado un correo de Alerta.")
        server.quit()

        time.sleep(200)



