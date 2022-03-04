import pdb
from rest_framework.views import exception_handler


def customExceptionHandler(exception, context):

    handlers = {
        "ValidationException": _handle_generic_error,
        "Http404": _handle_generic_error
    }

    response = exception_handler(exception, context)

    exception_class = exception.__class__.__name__

    if response is not None:
        import pdb
        pdb.set_trace()

        response.data['status_code'] = response.status_code

    if exception_class in handlers:
        return handlers[exception_class](exception, context, response)

    return response



def _handle_generic_error(exception, context, response):
    return response