from behave import *

@step("que no existen tareas completadas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que no existen tareas completadas')


@step("se presente el diagrama de Gantt con todas las tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se presente el diagrama de Gantt con todas las tareas')


@step("ninguna de las tareas estará marcada como completadas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces ninguna de las tareas estará marcada como completadas')


@step("que existen tareas completadas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que existen tareas completadas')


@step("las tareas que estén completadas estarán marcadas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces las tareas que estén completadas estarán marcadas')


@step("que existen las siguientes tareas completadas:")
def step_impl(context):
    #      | nombre                 | fechaInicio | fechaFin   | responsable |
    #      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
    #      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
    #      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado  que existen las siguientes tareas completadas')