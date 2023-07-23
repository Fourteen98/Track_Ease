from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response and response.status_code == 403:
        response.data = {"status": "error", "message": response.data['detail']}

    return response
