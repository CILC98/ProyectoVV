# Created by CESAR at 10/01/2022
# language: es
Característica: Ingreso de tareas
  Como gerente del proyecto deseo poder agregar tareas al proyecto para que
  sean asignadas posteriormente a los empleados de manera particular.

  Escenario: Ingreso de tareas
    Dado que el proyecto se ha creado
    Cuando se ingrese a la opción de registrar tareas
    Entonces se podrá agregar las siguientes tareas al proyecto:
      | nombre                 | fechaInicio | fechaFin   | Estimación | Prioridad |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | 3          | Alta      |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | 4          | Baja      |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | 3          | Media     |

