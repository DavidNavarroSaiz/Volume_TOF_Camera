
<h1 align="center">Camara: TOF</h1>
<p>

 <div alingn ="center">
<p align="center">Demo medicion de volumen</p>
 </div>
 </p>
 Acontinuacion se presenta un demo para el calculo del volumen que se encuentra en el interior de un recipiente en el laboratorio, ver figura (1). Para esta ocasión, se uso una mezcla de agua con una arcilla simulando  un lodo con el fin de tener de manera general  las condiciones del material a inspeccionar en mineros y calcular el volumen.
 <p>
<p align="center">
<img src="tarro.jpeg" >
</p>
<p align="center">Figura 1.</p>
<p align="left">Requerimientos:</p>
Este demo se realizo en Python 3.10.7, ademas, es necesario contar con las librerias que se encuentra en el archivo solucion Leer_archivo_h5 de este repocitorio.
<p></p>

En el laboratorio se obtuvieron imagenes del tarro con diferentes volumenes de la mezcla, la cual se fué adicionando en el tarro a alturas aproximadas de 2,4,6 y 8 centrimetros usando el archivo "capturas_h5.py".

<p align="left">PROCEDIMIENTO PARA EL CALCULO DEL VOLUMEN</p>

El procedimiento para realizar la medicion esta dada por:
<p></p>
*Cargar datos de las imagenes (nube de puntos)
<p></p>
*Guardar la informacion de la imagen de referencia. Figura 2.
<p></p>
*A las imagenes del recipiente con cada volumen segmentar la superficie del volumen. Figura 3
<p></p> *Unir la superfice segmentada en la imagen de referencia. Figura 4. 
<p></p>
*Segmentar la region que contiene el volumen en la imagen unida para extraer el volumen del recipiente contenido. Figura 5.
<p></p>
*Realizar un mesh por medio de delaunay 3D para rellenar la seccion segmentada.
<p></p>
*Optener el valor del Volumen.
<p></p>
<p align="center">
<img src="procedimiento.png" >
</p>
Imagen del volumen solido.
 <p align="center">
<img src="llenado_volumen.png" >
</p>
