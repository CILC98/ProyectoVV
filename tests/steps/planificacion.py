from behave import *


@step("que no existen tareas")
def no_existen_tareas(context):
    assert True


@step("se visualice el diagrama de Gantt")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True


@step('se mostrará el mensaje "No existen tareas para mostrar" al usuario')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True


@step('se mostrará un botón que le lleve a "Crear una nueva tarea"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True


@step("que existen las siguientes tareas:")
def step_impl(context):
    #      | nombre                 | fechaInicio | fechaFin   | responsable |
    #      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
    #      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
    #      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError("que existen las siguientes tareas:")


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


@step("se presente el diagrama de Gantt")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se presente el diagrama de Gantt')


@step("una barra que representa la cantidad de días en los cuales está planificado su desarrollo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Y una barra que representa la cantidad de días en los cuales está planificado su desarrollo')


@step("los miembros del proyectos responsables de cada tarea")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y los miembros del proyectos responsables de cada tarea')

