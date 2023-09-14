# wro2023-adagroup


 <p style = "text-aling:center;">En gran mayoría de los casos siempre se llega a buscar formas de mejorar la manera de viajar de un sitio a otro, de buscar la automatización del transporte, sin embargo, los procesos que se pueden llegar a plantearse suelen ser tan contaminantes y bastante elevados al nivel económico, siempre con las presencias de modelos que no estén modulados o capacitados para entornos naturales, hace que no pueda identificar las cosas a su paso, generando más problemas a su aplicación en el campo. Los integrantes del equipo presentado llamado "adagroup", sugieren un modelo que pueda detectar obstáculos, utilizando una materia prima más ecológica, y con una estructura electromecánica, utilizando elementos electrónicos para su funcionamiento, conexión, y aumentar la efectividad de los procedimientos con programación. </p> 
      

![image](https://github.com/kaolof/wro2023-adagroup/assets/67702983/b2134ed8-f877-4dc1-98cd-a1e834340fa6)

## Proceso de diseño

### 1. Mecanica


#### 1.1 Dirreción del vehículo


   La dirección de la solución robótica a cual se le dio el nombre de Cybercooper es de tipo electrónica Ackermann. La dirección electrónica aporta la asistencia necesaria para mover las ruedas y efectuar el giro, esta es una gran alternativa a las direcciones mecánicas e hidráulicas porque no le causa mayor trabajo al motor y permite que tenga menos conexiones mecanicas haciendo que sea mucho más sencilla.


   Por dirección Ackermann se entiende a un sistema de direccionamiento automotriz que permite a las ruedas girar ángulos distintos con el fin de generar un solo centro de giro, otorgándole al carro un mejor desempeño en las curvas lo que hace que no se pierda velocidad mientras se gira.


   En el caso de la dirección del Cybercooper, se utilizaron estos dos sistemas para generar el direccionamiento del carro, componiéndose por 4 piezas (una mejoría ante sistema anterior), el servomotor que es el hace girar el sistema (este se encuentra ubicado en la parte superior del chasis) el cual esta conectado a una barra de madera (es quien soporta a las ruedas, esta mide 10cm de largo).
   

   ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/a5c072bf-58dd-42a7-a56e-582bbea6aa07)

![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/31ab27e4-263e-4ec8-95d0-6e37e6e0bd2b)


#### 1.2 Conducción


   El Cybercooper es propulsado por el eje trasero se compone por una transmisión de dos velocidades, donde el piñón de ataque fijado al servomotor con un tornillo acciona el engranaje coronario fijado con dos contra tuercas (dos adelante del engranaje y dos atrás) en una barra roscada (mismo diámetro que las anteriores) de 16cm de largo. 
   Al motor inducir velocidad y potencia en el engranaje coronario accionando la barra roscada y comenzando a mover las ruedas (las cuales están fijadas a cada lado de la barra), el eje de salida de la transmisión es sostenido por dos bases (impresas en 3D) donde la base más grande actúa de suspensión fija con el objetivo de reducir vibraciones en el robot. Esta se encuentra fijada con dos tornillos.


  La base más pequeña tiene una forma de "U" la cual se encarga de sujetar y mantener al engranaje coronario en la posición ideal, sin embargo al motor mover el sistema completo, aplicaba una cantidad de estrés considerable a la pieza por lo que se le colocó un resorte para darle una mayor rigidez a esta base. Además de eso, el motor esta elevado 0.5cm con una base de plástico para posicionar mejor el piñón con tal de formar un ángulo de 90° entre los dos engranajes.

  

  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/c189a656-0939-48ea-8804-4de5f8ac7182)

![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/5835d127-a4bb-48cb-a9b3-19ae07e2077a)
![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/33d9caad-8311-46d4-9b29-167f61af3b94)


  
#### 1.3 Diseño de chasis


  Ya con el sistema de conducción y dirección definidos y explicados pieza por pieza, se puede describir el diseño del chasis.
  Esta configuración que posee el Cybercooper es basada en el Cybertruck de Tesla y varios autos deportivos como por ejemplo el Bugatti, la cual consiste en una base con forma irregular hecha de PLA con un tamaño de 25cm x 10cm x 0.5cm. 

  
  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/0e9d6c2e-6a99-4a42-a0a9-262a7080143f)


  En la parte trasera se encuentra un rectángulo 7.5cm x 10cm donde se encuentra la tracción de la solución robótica la cual dispone de dos pilares de 1cm x 1cm x 6cm que le dan rigidez al motor para sostenerse, y a su vez, cuenta con una serie de perforaciones de 0.2cm, más 8 huecos de 0.4cm de diámetro (2 para la suspensión fija y 4 para la base del engranaje) lo que le proporciona menos peso al vehículo. 

  
  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/272011f7-1864-4df3-817f-e549e99733f8)

  
  La forma geométrica del tren trasero le proporciona mayor rigidez por lo que le permite mejorar estabilidad y evitar las vibraciones debido que se distribuye mejor el peso. 
En la parte intermedia de la pieza se encuentran 5 varillas, una en la mitad, dos formando un triángulo, y dos a los costados. El motivo de estas varillas es reducir el peso sin perder rigidez en la pieza, además de que la forma del triángulo se caracteriza por ser una de las más rígidas del mundo y es por esta razón que se posicionaron las varillas de dichas posiciones. En caso hipotético que las varillas laterales se quiebren, queda el triángulo y en caso de que éste también se desprenda, quedará la varilla central. El tamaño de ésta sección del chasis es de 7cm de largo. 

  Con esto en mente podemos pasar al tren delantero, donde reposa la transmisión que se encarga de la dirección, esta última sección cuenta con dos pilares de igual dimensión al igual que la parte trasera cumpliendo la misma función de otorgar soporte al motor, esto en el modelo antecesor, ya que el servomotor de la dirección se encuentra sobre el chasis en el nuevo modelo. Esta sección tiene una forma más estrecha en el frente, con el fin de dar mayor libertad a las ruedas y a los sensores para girar, además de reducir el peso del vehículo. En el lado derecho de esta parte reposa la dirección (esto en el modelo antecesor).  
  

![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/3192a14e-2c05-4049-a3b1-508dbd41b6b3)
![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/5658bad8-aead-4968-91ad-f4b8118558d7)


### 2. Electrónica


#### 2.1 Sensores
#### 2.2 Control de Velocidad - Dirección
  
  
  Con los sensores cubiertos, es importante después de que estos provean la información necesaria, la misma sea ejecutada, y aquí es donde influyen los motores tipo codificador fotoeléctrico, los cuales poseen la filosofía de un servomotor, pero al ser utilizado a 360 grados, y se lleva a su mayor potencia (combinado con todo el peso que tiene que mover por el apartado de dirección y propulsión), lo cual hace que tenga segundos de apagado donde genere cierto tiempo para detenerse el sistema de propulsión y dirección por completo.

  Un motor de tipo codificador fotoeléctrico posee la capacidad de tener una buena precisión debido a su sistema de codificación óptica, por ello su nombre de fotoeléctrico, y no hace cumplir del todo con las características de un servomotor. Utilizando dos motores ubicados por debajo del chasis, uno conectado con el sistema de propulsión y otro conectado hacia el sistema de dirección, ubicado en la parte superior del chasis. Esto aparte de ir conectados con dichos sistemas, van conectados con el CyberPi, con el objetivo de recibir las ordenes que le dé en base al código implantado en el mismo.

  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/f2eb837d-10e1-4aaa-bdc4-cdad9cb2d863)

  La ubicación que posee el motor trasero es debido a la conexión que tiene que tener con los engranajes mecánicos de la transmisión trasera, priorizando la propulsión en ambas ruedas del carro, haciendo que no se transmita de manera directa tomando en cuenta los engranajes que ayudan en la transmisión de la fuerza hacia las ruedas, incluyendo esto, el motor posee una capacidad de voltaje que va hasta los 7,4 voltios y en cuanto a su potencia es mayor a las 300 revoluciones por minuto, esto aplicado para el motor de propulsión, mientras que en la dirección se presenta de manera individual, sin el uso de engranajes que facilita tanto en fuerza como en funcionamiento, para cada caso se debe de aplicar una fuerza diferente cada vez que se haga un cambio de dirección, debido al peso de los sensores y su posición en el sistema de dirección, siendo los siguientes:
  
  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/e5235a43-37e2-4d53-bc61-5dcd5ab72fea)

  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/52737f42-dba2-4111-bc67-400b879670e9)



6 RPM para ejecución hacia la derecha
6 RPM para la ejecución hacia la izquierda
4.5 RPM para enderezar viniendo de la derecha
5 RPM para enderezar viniendo de la izquierda

  Por otro lado, también este es controlado por el mismo CyberPi, para hacer los cambios de dirección, parándose el sistema de propulsión, activándose el sistema de dirección, y después de girar de nuevo volver a ejecutarse.

#### 2.3 Diagrama de Cableado
  
  
  Los cables se ajustan a las necesidades de conexión requeridos por el modelo Cybercooper, compuestos por dos cable para los servomotores “EM” y tres cables “mBuild”, que forman parte del kit “mBot Neo 2", y son compatibles con gran parte de los componentes de makeblock. Planteado de mejor manera en el siguiente diagrama:

  ![image](https://github.com/kaolof/wro2023-adagroup/assets/143504227/5f89377c-6a0a-4827-95d9-5083a895c123)

  
