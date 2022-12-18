#Pegando os dados climáticos ----------------------------------

#importando os módulos
from requests import get
import json
from pprint import pprint

#Pegando parte do link
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

#Definindo a longitude e latitude de São Carlos
my_lat = -22.00962768278184
my_lon = -47.89382570189137

#Pegando o ID fornecido pelo docente 
ID = 966583

#Concatenando a parte do link com o ID
weather = weather + str(ID)

#Pegando e printando os dados fornecidos pela API
my_weather = get(weather).json()['items']
pprint(my_weather)

#Uso de camera --------------------------------------------------------

#Importando os módulos
from time import sleep
import time
from picamera import PiCamera

#Definindo um objeto camera
camera = PiCamera()
#Atribuição a resolução desejado a camera
camera.resolution = (1024, 768)
#Anotando na câmera os nome dos integrantes da dupla
camera.annotate_text = "Leonardo Zaniboni 11801049 \n Guilherme Yukio 11800796"
#Vendo a camera
camera.start_preview(alpha=250)
#Capturando a imagem
camera.capture("/home/sel/img.jpg")
time.sleep(5)
camera.stop_preview()
#Gravando o video
camera.start_recording("video_leo_gui.h264")
time.sleep(5)
#Parando de gravar
camera.stop_recording()