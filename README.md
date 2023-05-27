# pim
Repositorio proyecto final PIM Univerisdad Javeriana 2023-10

# Análisis de Imágenes Médicas - Segmentación de Características en Imágenes de Fondo de Ojo

Este proyecto tiene como objetivo desarrollar un pipeline para la segmentación de características en imágenes de fondo de ojo, basado en el desafío propuesto en [AIROGS](https://airogs.grand-challenge.org/data-and-challenge/). El propósito es extraer y segmentar estructuras de interés en estas imágenes.

# Descripción del Proyecto

El reto consiste en segmentar cilindros (venas) que rodean una estructura esférica (Globo Ocular), lo cual representa un desafío interesante desde el punto de vista geométrico. Inicialmente, nos enfocamos en las estructuras de las venas y el círculo óptico.

Otro desafío importante fue establecer parámetros que se adapten al conjunto de imágenes seleccionadas (30) para tratarlas de manera razonable. Esto es relevante, considerando las implicaciones del uso de imágenes de diferentes fuentes y morfológicamente distintas en un entorno real.

# Generalidades del pipeline.

Dentro de las conclusiones a priori que se puede obtener del desarrollo del presente proyecto está el hecho de que el orden afecta el resultado. Con esto en mente establecemos para este caso de uso particular la siguiente cronología como la más efectiva para la obtención del resultado esperado.

<img width="284" alt="pipeline" src="https://github.com/IaManBel/pim/assets/124216691/aa955d5b-6f92-44eb-b8f0-11da5e2c66c4">

# Ejecución 

Los programas utilizados para el desarrollo del proyecto se encuentran en este repositorio en el directorio /Code_python
la sintaxis de ejecución y el orden especifico es el siguiente.

#### python3  grayscale.py TRAIN01.jpg gTRAIN01.jpg 
#### python3  median.py gTRAIN01.jpg medi1gTRAIN01.jpg 1  
#### python3  Gaus2.py medi1gTRAIN01.jpg Gausmedi1gTRAIN01.jpg    
#### python3  mean.py Gausmedi1gTRAIN01.jpg mean2Gausmedi1gTRAIN01.jpg 2  
#### python3  Ccurv.py mean2Gausmedi1gTRAIN01.jpg Ccur12mean2Gausmedi1gTRAIN01.jpg 1 2  
#### python3  KrnelMax.py Ccur12mean2Gausmedi1gTRAIN01.jpg KrneCcur12mean2Gausmedi1gTRAIN01.jpg   

# Resultados
![KrnCcur12mean2Gausmedi1gTRAIN01](https://github.com/IaManBel/pim/assets/124216691/1a1f823f-cb90-4b1c-9432-82c2112c7770)





