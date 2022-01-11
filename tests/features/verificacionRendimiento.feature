# Created by CESAR at 20/12/2021
# language: es
Característica: Verificación de rendimiento laboral
  Como gerente del proyecto deseo poder visualizar las tareas completadas
  por los empleados para verificar el rendimiento laborar de cada uno de ellos y así conocer
  si se está cumpliendo con sus actividades designadas.

  Escenario: No existen tareas completadas
    Dado que no existen tareas completadas
    Cuando se presente el diagrama de Gantt con todas las tareas
    Entonces ninguna de las tareas estará marcada como completadas

  Escenario: Existen tareas completadas
    Dado que existen las siguientes tareas completadas:
      | nombre                 | fechaInicio | fechaFin   | responsable |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    Cuando se presente el diagrama de Gantt con todas las tareas
    Entonces las tareas que estén completadas estarán marcadas

