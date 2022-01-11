from behave import *



@step("que no existen tareas tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que no existen tareas tareas')


@step("se visualice el diagrama de Gantt")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se visualice el diagrama de Gantt')


@step('se mostrará el mensaje "No existen tareas para mostrar" al Usuario')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se mostrará el mensaje "No existen tareas para mostrar" al Usuario')


@step('se le mostrará un botón que le lleve a "Crear una nueva tarea"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se le mostrará un botón que le lleve a "Crear una nueva tarea"')


@step("que existen las siguientes tareas:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que existen las siguientes tareas:')


@step("se presente el diagrama de Gantt")
def step_impl(context):
    """
     | nombre                 | fechaInicio | fechaFin   | responsable | estado      |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    | Finalizada  |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       | Atrasada    |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        | En progreso |
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se presente el diagrama de Gantt')


@step("se presente el diagrama de Gantt")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se presente el diagrama de Gantt')


@step("se mostrará el nombre de la tarea")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se mostrará el nombre de la tarea')


@step("los miembros del proyectos responsables de cada tarea")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y los miembros del proyectos responsables de cada tarea')


@step("una barra que representa la cantidad de días en los cuales está planificado su desarrollo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Y una barra que representa la cantidad de días en los cuales está planificado su desarrollo')


@step("el estado de la tarea")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y el estado de la tarea')