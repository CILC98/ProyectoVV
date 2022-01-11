from behave import *


@step("que el proyecto se ha creado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que el proyecto se ha creado')


@step("se ingrese a la opción de registrar tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se ingrese a la opción de registrar tareas')


@step("se podrá agregar las siguientes tareas al proyecto:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se podrá agregar las siguientes tareas al proyecto:
                              | nombre | fechaInicio | fechaFin | Estimación | Prioridad |
                              | Plan
    del Proyecto | 18 - 01 - 2022 | 22 - 02 - 2022 | 3 | Alta |
        | Ejecución
    del Proyecto | 23 - 02 - 2022 | 27 - 0
    8 - 2022 | 4 | Baja |
    | Ejecución
    de
    Pruebas | 28 - 0
    8 - 2022 | 01 - 12 - 2022 | 3 | Media | ')