# Created by CESAR at 20/12/2021
# language: es
Característica Asignación de tareas automáticas
  Como gerente de  proyecto deseo automatizar
  la asignación de tareas en función de su prioridad para
  mejorar la producción  minimizando el tiempo de espera de
  toma de decisiones y no genera tareas en cola de alta prioridad.

  Escenario Existen tareas con la misma fecha de inicio
    Dado que se ingresan las siguientes tareas:
      | nombre                     | fechaInicio | fechaFin   | responsable | prioridad |
      | Creación de protoripos     | 18-01-2022  | 22-02-2022 | Mauricio    | Alta      |
      | Creación de pruebas        | 18-01-2022  | 27-08-2022 | David       | Media     |
      | Diseño de la base de datos | 18-01-2022  | 01-12-2022 | Rosa        | Baja      |
    Cuando se realiza la asignación de tareas
    Entonces se asignan las tareas desde la que tiene mayor prioridad

  Escenario Existen tareas que no tienen la misma fecha de inicio
    Dado que se ingresan las siguientes tareas:
      | nombre                     | fechaInicio | fechaFin   | responsable | prioridad |
      | Creación de prototipos     | 18-01-2022  | 22-02-2022 | Mauricio    | Alta      |
      | Creación de pruebas        | 18-02-2022  | 27-08-2022 | David       | Media     |
      | Diseño de la base de datos | 18-03-2022  | 01-12-2022 | Rosa        | Baja      |
    Cuando se realiza la asignación de tareas
    Entonces se asignan las tareas desde la que tiene mayor prioridad

  Escenario No existen tareas que no tienen
    Dado que no se tienen tareas para asignarse
    Cuando se realice la asignación de tareas
    Entonces no se modificará ninguno registro de asignación

