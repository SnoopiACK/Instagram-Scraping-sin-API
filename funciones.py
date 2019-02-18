import os
import tensorflow as tf
import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import datetime
import cv2
import numpy as np
from skimage import io
import os


RETRAINED_LABELS_TXT_FILE_LOC = os.getcwd() + "/" + "retrained_labels.txt"
RETRAINED_GRAPH_PB_FILE_LOC = os.getcwd() + "/" + "retrained_graph.pb"

TEST_IMAGES_DIR = "./data/validacion"

SCALAR_GREE = (0.0, 255.0, 0.0)
SCALAR_RED = (255.0, 0.0, 0.0)

classifications = ['comida','nocomida']


def plotear(openCVImage,strClassification,scoreAsAPercent):

#    print("the object appears to be a " + strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence")
#    cv2.imshow("foto", cv2.cvtColor(openCVImage, cv2.COLOR_BGR2RGB))
    writeResultOnImage(openCVImage, strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% ",strClassification)
    plt.axis('off')
    plt.imshow(openCVImage)  
    

def analisar(link):

    with tf.Session() as sess:


#        openCVImage = cv2.imread(imageFileWithPath)
        openCVImage = io.imread(link)
        

        finalTensor = sess.graph.get_tensor_by_name('final_result:0')

        tfImage = np.array(openCVImage)[:, :, 0:3]
            
        predictions = sess.run(finalTensor, {'DecodeJpeg:0': tfImage})

        sortedPredictions = predictions[0].argsort()[-len(predictions[0]):][::-1]

        onMostLikelyPrediction = True
        for prediction in sortedPredictions:
            strClassification = classifications[prediction]
            if strClassification.endswith("s"):
                strClassification = strClassification[:-1]

            confidence = predictions[0][prediction]
      
            
            if onMostLikelyPrediction:            
                scoreAsAPercent = confidence * 100.0
                categoria = strClassification
                print("the object appears to be a " + strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence")
#                writeResultOnImage(openCVImage, strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence",strClassification)
##                cv2.imshow("foto", cv2.cvtColor(openCVImage, cv2.COLOR_BGR2RGB))
#                plt.axis('off')
#                plt.imshow(openCVImage)
#                plotear(openCVImage,strClassification,scoreAsAPercent)
                onMostLikelyPrediction = False
#                
                
##                cv2.waitKey()
#                cv2.destroyAllWindows()
#
#        tfFileWriter = tf.summary.FileWriter(os.getcwd())
#        tfFileWriter.add_graph(sess.graph)
#        tfFileWriter.close()
          
        return (categoria,scoreAsAPercent) 
#    
def writeResultOnImage(openCVImage, resultText,categoria ):
    
    color = SCALAR_RED
    imageHeight, imageWidth, sceneNumChannels = openCVImage.shape

 
    fontFace = cv2.FONT_HERSHEY_TRIPLEX

    fontScale = 1.0 
    fontThickness = 2

    fontThickness = int(fontThickness)

    upperLeftTextOriginX = int(imageWidth * 0.05)
    upperLeftTextOriginY = int(imageHeight * 0.05)
 
    textSize, baseline = cv2.getTextSize(resultText, fontFace, fontScale, fontThickness)
    textSizeWidth, textSizeHeight = textSize

    lowerLeftTextOriginX = upperLeftTextOriginX
    lowerLeftTextOriginY = upperLeftTextOriginY + textSizeHeight
    
    if categoria=="comida":
        color = SCALAR_GREE
    
    cv2.putText(openCVImage, resultText, (lowerLeftTextOriginX, lowerLeftTextOriginY), fontFace, fontScale, color, fontThickness)
   
def getInformacion(html):
    soup = BeautifulSoup(html) 
    
    
    meGusta = soup.findAll("div", class_="Nm9Fw")
    
    
    if str(meGusta) in 'Sé el primero en':
        megusta=0
    else:
        if str(meGusta) in 'Sé el primero en':
            megusta=1
        else:
            if(len(meGusta) != 0):
                meGusta = BeautifulSoup(str(meGusta))
                meGusta = meGusta.findAll('span')
                meGusta = str(meGusta)
                meGusta = meGusta.replace('[<span>','')
                meGusta = meGusta.replace('</span>]','')
                if str(meGusta) == '[]':
                    meGusta = '1'
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
    
    clase,porcentaje=analisar(link)
    plotear(foto,clase,porcentaje)
    datos = {'foto': foto,
             'link': link,
             'usuario': usuario,
             'megusta': meGusta,
             'clase': clase,
             'porcentaje': porcentaje,
             'fechaSubida': fechaSubida,
             'fechaRegistrada': fechaRegistrada}
 
        
    return datos
    




with tf.gfile.FastGFile(RETRAINED_GRAPH_PB_FILE_LOC, 'rb') as retrainedGraphFile:
    graphDef = tf.GraphDef()
    graphDef.ParseFromString(retrainedGraphFile.read())
    _ = tf.import_graph_def(graphDef, name='')













    
