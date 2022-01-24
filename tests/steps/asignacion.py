from behave import *

from Gantt.models import Proyecto, Tarea


@step("que se ingresan las siguientes tareas:")
def step_impl(context):
    #      | nombre                     | fechaInicio | fechaFin   | responsable | prioridad |
    #      | Creación de prototipos     | 18-01-2022  | 22-02-2022 | Mauricio    | Alta      |
    #      | Creación de pruebas        | 18-01-2022  | 27-08-2022 | David       | Media     |
    #      | Diseño de la base de datos | 18-01-2022  | 01-12-2022 | Rosa        | Baja      |
    """
    :type context: behave.runner.Context
    """



@step("se realiza la asignación de tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se realiza la asignación de tareas')


@step("se asignan las tareas desde la que tiene mayor prioridad")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se asignan las tareas desde la que tiene mayor prioridad')


@step("que no se tienen tareas para asignarse")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que no se tienen tareas para asignarse')


@step("se realice la asignación de tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se realice la asignación de tareas')


@step("no se modificará ninguno registro de asignación")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces no se modificará ningun registro de asignación')