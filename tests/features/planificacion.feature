# Created by CESAR at 15/12/2021
# language: es
Característica Planificación diaria
  Como gerente de proyecto deseo visualizar en un
  diagrama de Gantt  las  tareas diarias de cada
  uno de los miembros de proyectos de la organización
  para poder determinar los costos de producción diarios
  de los recursos humanos de manera más eficiente.

  Escenario No existen tareas
    Dado que no existen tareas
    Cuando se visualice el diagrama de Gantt
    Entonces se mostrará el mensaje "No existen tareas para mostrar" al usuario
    Y se mostrará un botón que le lleve a "Crear una nueva tarea"

  Escenario Existen tareas
    Dado que existen las siguientes tareas:
      | nombre                 | fechaInicio | fechaFin   | responsable |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    Cuando se presente el diagrama de Gantt
    Entonces se mostrará el nombre de la tarea
    Y una barra que representa la cantidad de días en los cuales está planificado su desarrollo
    Y los miembros del proyectos responsables de cada tarea

