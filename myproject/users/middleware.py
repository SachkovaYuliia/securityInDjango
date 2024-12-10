import logging
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError

logger = logging.getLogger(__name__)

class AccessLogMiddleware:
    """
        Middleware для логування спроб доступу до захищених сторінок.
        Якщо користувач не авторизований, він отримає статус 403.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Access attempt: {request.method} {request.path}")

        allowed_paths = ['/users/login/', '/users/register/', '/users/test/']
        if request.path in allowed_paths:
            return self.get_response(request)

        if request.path.startswith('/admin/') or request.path.startswith('/users/'):
            if not request.user.is_authenticated:
                return HttpResponse("Access denied", status=403)

        response = self.get_response(request)
        return response

class ErrorHandlingMiddleware:
    """
    Middleware для обробки помилок 404 та 500.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            logger.error(f"Page not found: {request.path} - IP: {request.META.get('REMOTE_ADDR')}")
            return HttpResponseNotFound("The page you are looking for is not available.")
        elif response.status_code == 500:
            logger.error(f"Internal server error: {request.path} - IP: {request.META.get('REMOTE_ADDR')}")
            return HttpResponseServerError("Something went wrong. Please try again later.")

        return response