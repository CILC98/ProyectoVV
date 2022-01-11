from behave import *

@step("que existen las siguientes tareas mostradas en el diagrama de Gantt:")
def step_impl(context):
    #      | nombre                 | fechaInicio | fechaFin   | responsable |
    #      | Plan del Proyecto      | 18-01-2022  | 22-02-2022 | Mauricio    |
    #      | Ejecución del Proyecto | 23-02-2022  | 27-08-2022 | David       |
    #      | Ejecución de Pruebas   | 28-08-2022  | 01-12-2022 | Rosa        |
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'que existen las siguientes tareas mostradas en el diagrama de Gantt:')


@step('se registre el comentario "Se necesita realizar la documentación de la tarea" en la primera tarea')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Cuando se registre el comentario "Se necesita realizar la documentación de la tarea" en la primera tarea')


@step("el comentario será registrado en la tarea")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces el comentario será registrado en la tarea')


@step('se mostrará el mensaje "Comentario registrado"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se mostrará el mensaje "Comentario registrado"')


@step('se registre el comentario "Se necesita realizar la documentación de la tarea" en la pimera tarea')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Cuando se registre el comentario "Se necesita realizar la documentación de la tarea" en la pimera tarea')


@step("se enviará una notificación a los responsables de la tarea")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces se enviará una notificación a los responsables de la tarea')