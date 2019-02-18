# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:53:36 2019

@author: LENOVO
"""


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
import time 
from skimage import io
import matplotlib
import urllib
import matplotlib.pyplot as plt

import funciones
from funciones import analisar,plotear
from funciones import getInformacion



#Igw0E   rBNOH        eGOV_         _4EzTm
def estaSTR(texto,palabra):
    try:
      resultado= texto.index(palabra)
    except ValueError:
      resultado=-1
    return resultado   



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
while(i<80):
    
    ht=driver.find_element_by_tag_name("html")
    html = driver.page_source
    soup = BeautifulSoup(html)  
                
    if "coreSpriteRightChevron\"" in html:
        rigth=ht=driver.find_element_by_class_name("coreSpriteRightChevron")
        rigth.click()
    else:
        ht.send_keys(Keys.RIGHT)
        
    if('Igw0E   rBNOH        eGOV_         _4EzTm' in html):
        ht.send_keys(Keys.LEFT)
        contadorErrores = contadorErrores + 1
        print('Error cargando')
        time.sleep(2)
        if(contadorErrores == 10):
            ht.send_keys(Keys.RIGHT)
            contadorErrores = 0 
        continue
    
    datos = getInformacion(html)
    if datos['clase'] == 'comida':
        fotosConComida.append(datos)
    

    plt.pause(2)    



# MEGUSTEADOR
# for cx in range(0,5):
#     meGusta=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/span[1]/button')
#     meGusta.click()
#     time.sleep(0.5)
#     ht=driver.find_element_by_tag_name("html")
#     ht.send_keys(Keys.RIGHT)
#     time.sleep(0.5)
    
#solar mongo
    
