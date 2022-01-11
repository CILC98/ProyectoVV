from behave import *


@step("que no existen tareas destacadas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que no existen tareas destacadas')


@step('se  presione el botón "Mostrar destacadas"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se  presione el botón "Mostrar destacadas"')


@step('se presione el botón "Mostrar destacadas"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se presione el botón "Mostrar destacadas"')





@step("que existen las siguientes tareas con prioridad:")
def step_impl(context):
    """
    :type context: behave.runner.Context
          | nombre                 | fechaInicio | fechaFin   | responsable | estado      | prioridad |
      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    | Finalizada  | Alta      |
      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       | Atrasada    | Media     |
      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        | En progreso | Baja      | `
    """
    raise NotImplementedError(u'STEP: Dado que existen las siguientes tareas con prioridad:')


@step('se mostrará la tarea con el nombre "Plan de Proyecto"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se mostrará la tarea con el nombre "Plan de Proyecto"')