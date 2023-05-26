# pim
Repositorio proyecto final PIM Univerisdad Javeriana 2023

# Análisis de Imágenes Médicas - Segmentación de Características en Imágenes de Fondo de Ojo

Este proyecto tiene como objetivo desarrollar un pipeline para la segmentación de características en imágenes de fondo de ojo, basado en el desafío propuesto en [AIROGS](https://airogs.grand-challenge.org/data-and-challenge/). El propósito es extraer y segmentar estructuras de interés en estas imágenes.

## Descripción del Proyecto

El reto consiste en segmentar cilindros (venas) que rodean una estructura esférica (Globo Ocular), lo cual representa un desafío interesante desde el punto de vista geométrico. Inicialmente, nos enfocamos en las estructuras de las venas y el círculo óptico.

Otro desafío importante fue establecer parámetros que se adapten al conjunto de imágenes seleccionadas (30) para tratarlas de manera razonable. Esto es relevante, considerando las implicaciones del uso de imágenes de diferentes fuentes y morfológicamente distintas en un entorno real.

GENERALIDADES DEL PIPELINE.

Dentro de las conclusiones a priori que se puede obtener del desarrollo del presente proyecto está el hecho de que el orden afecta el resultado. Con esto en mente establecemos para este caso de uso particular la siguiente cronología como la más efectiva para la obtención del resultado esperado.

<img width="377" alt="pipeline" src="https://github.com/IaManBel/pim/assets/124216691/11e6e3ce-d195-4369-ac91-4ca288f1b9fe">




