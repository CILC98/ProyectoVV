# Created by CESAR at 20/12/2021
# language: es
Característica Comentarios en tareas
  Como gerente de proyecto deseo tener
  la opción de comentar las tareas pendientes, finalizadas,
  y en progreso para dar una retroalimentación rápida a los empleados.

  Escenario Comentar tareas
    Dado que existen las siguientes tareas mostradas en el diagrama de Gantt:
      | nombre                 | fechaInicio | fechaFin   | responsable |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    Cuando se registre el comentario "Se necesita realizar la documentación de la tarea" en la primera tarea
    Entonces el comentario será registrado en la tarea
    Y se mostrará el mensaje "Comentario registrado"

  Escenario Notificar comentario
     Dado que existen las siguientes tareas mostradas en el diagrama de Gantt:
      | nombre                 | fechaInicio | fechaFin   | responsable |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    Cuando se registre el comentario "Se necesita realizar la documentación de la tarea" en la primera tarea
    Entonces se enviará una notificación a los responsables de la tarea