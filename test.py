from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time 
import random
from PIL import Image
import PIL
from skimage import io
import matplotlib
import urllib
import os
import datetime

import cv2
import numpy as np
from keras.preprocessing.image import load_img, img_to_array, array_to_img
from keras.models import load_model
from skimage import io

import matplotlib.pyplot as plt




#Igw0E   rBNOH        eGOV_         _4EzTm
def estaSTR(texto,palabra):
    try:
      resultado= texto.index(palabra)
    except ValueError:
      resultado=-1
    return resultado   


def predict(file):
  x = array_to_img(file)
  x = x.resize((longitud,altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  o=cnn.predict_proba(x)
  result = array[0]
  answer = np.argmax(result)
  return answer

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)


fotosConComida = []



chrome_path = "chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.set_window_position(0, 0)
driver.set_window_size(1,1000)


driver.get("https://www.instagram.com/accounts/login/");

email="snoopi.ht@gmail.com"
contra="instagram123snoopi"


caja = driver.find_element_by_name("username")
caja.send_keys(email)
time.sleep(0.2)
caja = driver.find_element_by_name("password")
caja.send_keys(contra, Keys.ENTER)
time.sleep(2)    



driver.get("https://www.instagram.com/explore/locations/230064926/bahia-blanca-buenos-aires/")


time.sleep(4)
ht=driver.find_element_by_class_name("_9AhH0")   
ht.click()
time.sleep(2)


i=0
contadorErrores = 0
while(i<800):
    
    ht=driver.find_element_by_tag_name("html")
    html = driver.page_source
    soup = BeautifulSoup(html)  
                
    ht.send_keys(Keys.RIGHT)
    if(estaSTR(html,'Igw0E   rBNOH        eGOV_         _4EzTm') != -1):
        ht.send_keys(Keys.LEFT)
        contadorErrores = contadorErrores + 1
        print('salala')
        time.sleep(2)
        if(contadorErrores == 10):
            ht.send_keys(Keys.RIGHT)
            contadorErrores = 0 
        continue
    
    
    meGusta = soup.findAll("div", class_="Nm9Fw")
    
    
    if estaSTR(str(meGusta),'Sé el primero en'):
        megusta=0
    else:
        if estaSTR(str(meGusta),'Sé el primero en'):
            megusta=1
        else:
            if(len(meGusta) != 0):
                meGusta = BeautifulSoup(str(meGusta))
                meGusta = meGusta.findAll('span')
                meGusta = str(meGusta)
                meGusta = meGusta.replace('[<span>','')
                meGusta = meGusta.replace('</span>]','')
                meGusta = int(meGusta.replace('.',''))
            else:
                    meGusta = -1
            
    usuario = soup.findAll("div", class_="o-MQd")
    usuario = BeautifulSoup(str(usuario))
    usuario = usuario.findAll('a')
    usuario = usuario[0]['title']
        

    
    fechaSubida = soup.findAll(class_="c-Yi7")
    fechaSubida = BeautifulSoup(str(fechaSubida))
    fechaSubida = fechaSubida.findAll('time')
    fechaSubida = fechaSubida[0]['datetime']
    año=int(fechaSubida[:fechaSubida.index('-')])
    fechaSubida = fechaSubida[fechaSubida.index('-')+1:]
    mes=int(fechaSubida[:fechaSubida.index('-')])
    fechaSubida = fechaSubida[fechaSubida.index('-')+1:]
    dia=int(fechaSubida[:fechaSubida.index('T')])
    fechaSubida = fechaSubida[fechaSubida.index('T')+1:]
    hora=int(fechaSubida[:fechaSubida.index(':')])
    fechaSubida = fechaSubida[fechaSubida.index(':')+1:]
    minuto=int(fechaSubida[:fechaSubida.index(':')])
    fechaSubida = fechaSubida[fechaSubida.index(':')+1:]
    segundo=int(fechaSubida[:fechaSubida.index('.')])
    
    fechaSubida =  datetime.datetime(año,mes,dia,hora,minuto,segundo,0)
    fechaRegistrada = datetime.datetime.now()
    
    
    foto = soup.findAll(class_="_97aPb")
    foto = BeautifulSoup(str(foto))
    foto = foto.findAll('img')
    foto = foto[0]['src']
    link = foto
    foto = io.imread(foto)
    


    texto = 'NO ES COMIDA'
    color =  (0, 0, 255)
    if(predict(foto)==0):
        fotosConComida.append(foto)
        texto = 'COMIDA'
        color =  (0, 255, 0)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    plotear = foto +foto*0
    cv2.putText(plotear, texto, (20, 80), font, 3, color, 3)
   
    plt.axis('off')
    plt.imshow(plotear)
    plt.pause(2)    
    i=i+1
    print(i)
