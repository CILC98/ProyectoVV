# Created by CESAR at 10/01/2022
# language: es

Característica: Visualización de tareas destacadas
  Como gerente del proyecto deseo poder visualizar las tareas que tienen mayor
  prioridad en el proyecto para mantener un control sobre el avance y estado del proyecto

  Escenario No existen tareas destacadas
    Dado que no existen tareas destacadas
    Cuando se  presione el botón "Mostrar destacadas"
    Entonces se mostrará el mensaje "No existen tareas para mostrar" al Usuario

  Escenario Existen tareas destacadas
    Dado que existen las siguientes tareas con prioridad:
      | nombre                 | fechaInicio | fechaFin   | responsable | estado      | prioridad |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    | Finalizada  | Alta      |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       | Atrasada    | Media     |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        | En progreso | Baja      |

    Cuando se presione el botón "Mostrar destacadas"
    Entonces se mostrará la tarea con el nombre "Plan de Proyecto"
    Y una barra que representa la cantidad de días en los cuales está planificado su desarrollo
    Y los miembros del proyectos responsables de cada tarea
    Y el estado de la tarea