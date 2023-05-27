# pim
Repositorio proyecto final PIM Univerisdad Javeriana 2023-10

# Análisis de Imágenes Médicas - Segmentación de Características en Imágenes de Fondo de Ojo

Este proyecto tiene como objetivo desarrollar un pipeline para la segmentación de características en imágenes de fondo de ojo, basado en el desafío propuesto en [AIROGS](https://airogs.grand-challenge.org/data-and-challenge/). El propósito es extraer y segmentar estructuras de interés en estas imágenes.

# Descripción del Proyecto

El reto consiste en segmentar cilindros (venas) que rodean una estructura esférica (Globo Ocular), lo cual representa un desafío interesante desde el punto de vista geométrico. Inicialmente, nos enfocamos en las estructuras de las venas y el círculo óptico.

Otro desafío importante fue establecer parámetros que se adapten al conjunto de imágenes seleccionadas (30) para tratarlas de manera razonable. Esto es relevante, considerando las implicaciones del uso de imágenes de diferentes fuentes y morfológicamente distintas en un entorno real.

# Generalidades del pipeline.

Dentro de las conclusiones a priori que se puede obtener del desarrollo del presente proyecto está el hecho de que el orden afecta el resultado. Con esto en mente establecemos para este caso de uso particular, la siguiente cronología como la más efectiva para la obtención del resultado esperado.

<img width="284" alt="pipeline" src="https://github.com/IaManBel/pim/assets/124216691/aa955d5b-6f92-44eb-b8f0-11da5e2c66c4">

# Detalle y justificación

1.	Dadas las características ya expuestas de las imágenes, en primer lugar, convertimos las imágenes a escala de grises, en búsqueda de simplicidad y reducción de esfuerzo de cómputo, así como una reducción en la dimensionalidad, para el tratamiento de estas.

2.	Dentro del pipeline el siguiente ajuste está enfocado a la reducción del ruido, por medio de la aplicación de un    filtro de mediana, eliminando los outliers (pixeles que exceden por mucho el valor de la media, para este filtro se utilizó el parámetro r=1!.

3.	Con el objetivo de preservar los bordes, de las estructuras que queremos destacar, dentro del pipeline se hace uso de un filtro gausiano, el cual de acuerdo con las especificaciones facilita trabajar la imagen para resaltar las venas y el circulo óptico. Con este acercamiento logramos observar claramente las estructuras existentes en dentro del círculo óptico, las cuales representan en general dificultad por su particular luminosidad, y las que hasta el momento para nosotros con el uso de otros pipelines habían sido difícilmente identificables.

4.	Dentro del pipeline hacemos uso del filtro mean buscando reducir el ruido en la imagen (variaciones de alta frecuencia) para el desarrollo del ejercicio se utilizó el valor de r = 2, con el objetivo específico de conservar y resaltar las áreas de especifico interés (Roi).

5.	Para este caso específico en donde nos enfrentamos geométricamente a una esfera (globo ocular), envuelta por entidades cilíndricas (cavidades venosas), hacemos uso del filtro de difusión basado en curvatura, buscando aprovechar a ventaja que ofrece el registro del cambio de gradiente. Como parte de la generalización del proceso para tratar las 30 imágenes, se definieron los parámetros Iteraciones = 1 y unidades de tiempo = 2, ya que como combinatoria nos presentó un mejor resultado de cara al resultado esperado.

6.	Por último, en el pipeline, se aplica un kernel de dimensión 3 x 3, asignando el valor máximo a cada pixel, buscando mejorar la representación de la imagen como resultado final.



# Ejecución 

Los programas utilizados para el desarrollo del proyecto se encuentran en este repositorio en el directorio [Code_python](https://github.com/IaManBel/pim/tree/main/Code_python) ,la sintaxis de ejecución y el orden especifico es el siguiente.

#### python3  grayscale.py TRAIN01.jpg gTRAIN01.jpg 
#### python3  median.py gTRAIN01.jpg medi1gTRAIN01.jpg 1  
#### python3  Gaus2.py medi1gTRAIN01.jpg Gausmedi1gTRAIN01.jpg    
#### python3  mean.py Gausmedi1gTRAIN01.jpg mean2Gausmedi1gTRAIN01.jpg 2  
#### python3  Ccurv.py mean2Gausmedi1gTRAIN01.jpg Ccur12mean2Gausmedi1gTRAIN01.jpg 1 2  
#### python3  KrnelMax.py Ccur12mean2Gausmedi1gTRAIN01.jpg KrneCcur12mean2Gausmedi1gTRAIN01.jpg   

# Resultados
Los resultados obtenidos en cada uno de los 30 casos se encuentran en el directorio [6-Kernel](https://github.com/IaManBel/pim/tree/main/6-Kernel)
![KrnCcur12mean2Gausmedi1gTRAIN01](https://github.com/IaManBel/pim/assets/124216691/1a1f823f-cb90-4b1c-9432-82c2112c7770)





