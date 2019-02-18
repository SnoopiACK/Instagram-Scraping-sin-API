Scraper de Instagram que utiliza "Selenium" que permite automatizar navegadores web, en este caso Google Chrome.

**Para el funcionamiento se requiere una cuenta de Instagram.**

El script	 inicia sesión y luego comienza a “ver” las imágenes subidas en Bahía Blanca (puede cambiarse a cualquier otra localización), recoge información de cada imagen (Cantidad de Me Gusta, Usuario que publico, Fecha de posteo, etc.) y utilizando una red que se entrenó previamente se estima si la foto es o no COMIDA.

**WINDOWS**  <br />
**Instalar Selenium**

```
conda install -c conda-forge selenium
```
- Se debe tener *chromedriver.exe* en el mismo directorio.  <br />
- Google Chrome instalado.



Antes de correr el programa se debe descargar la red 
Link de la red: https://mega.nz/#!K1JR0Q4T!8H0vYEOtoujKjatW45cQ7fbXts1HgV99XUttJeLI8-4
