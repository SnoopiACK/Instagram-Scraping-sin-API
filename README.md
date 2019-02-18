Scraper de Instagram que utiliza "Selenium" que permite automatizar navegadores web, en este caso Google Chrome.

**Para el funcionamiento se requiere una cuenta de Instagram.**

El script	 inicia sesión y luego comienza a “ver” las imágenes subidas en Bahía Blanca (puede cambiarse a cualquier otra localización), recoge información de cada imagen (Cantidad de Me Gusta, Usuario que publico, Fecha de posteo, etc.) y utilizando una red Tensorflow que se entrenó previamente se estima si la foto es o no COMIDA.

**WINDOWS**  <br />
**Instalar Selenium**

```
conda install -c conda-forge selenium
```
- Se debe tener *chromedriver.exe* en el mismo directorio.  <br />
- Google Chrome instalado. <br />

**Clasificador Comida/noComida**

Antes de correr el programa se debe descargar la red y colocar en el mismo directorio donde se ejecuta el script. <br />
Link de la red: https://mega.nz/#!K1JR0Q4T!8H0vYEOtoujKjatW45cQ7fbXts1HgV99XUttJeLI8-4

**Ejecutar**

Correr el script *scraper.py*.



**Advertencia**

- Todavía no está protegido ante posibles errores, por ejemplo: Que falle la conexión a internet.<br /> 

- Solo se probó en la versión en español de Instagram, talvez otra versión podrían surgir errores. <br /> 

- Por el momento analiza un numero arbitrario de imagenes, 


![20190218012711](https://user-images.githubusercontent.com/40048927/52928328-e163e800-331d-11e9-9258-fa2c46086d94.gif)

