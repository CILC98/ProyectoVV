# Created by CESAR at 10/01/2022#
# language: es
Característica Visualización del progreso de las tareas
  Como gerente de proyecto deseo visualizar en un diagrama de Gantt el progreso de
  tareas de cada uno de los miembros de proyectos de la organización para poder determinar
  de una manera más eficiente los costos de producción de los recursos humanos.

  Escenario No existen tareas
    Dado que no existen tareas tareas
    Cuando se visualice el diagrama de Gantt
    Entonces se mostrará el mensaje "No existen tareas para mostrar" al Usuario
    Y se le mostrará un botón que le lleve a "Crear una nueva tarea"

  Escenario Existen tareas
    Dado que existen las siguientes tareas:
      | nombre                 | fechaInicio | fechaFin   | responsable | estado      |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    | Finalizada  |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       | Atrasada    |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        | En progreso |
    Cuando se presente el diagrama de Gantt
    Entonces se mostrará el nombre de la tarea
    Y una barra que representa la cantidad de días en los cuales está planificado su desarrollo
    Y los miembros del proyectos responsables de cada tarea
    Y el estado de la tarea

