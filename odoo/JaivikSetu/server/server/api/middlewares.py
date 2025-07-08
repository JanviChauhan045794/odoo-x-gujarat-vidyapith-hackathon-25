from django.http import JsonResponse
from django.conf import settings

class NextJSOnlyMiddleware:
    """
    Middleware to allow access only to requests coming from the Next.js frontend.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # Define allowed origins (e.g., Next.js frontend URL)
        self.allowed_origins = getattr(settings, "NEXTJS_ALLOWED_ORIGINS", settings.CORS_ALLOWED_ORIGINS)

    def __call__(self, request):
        # Skip the middleware for admin routes
        if request.path.startswith('/admin'):
            return self.get_response(request)
        
        # Get the Origin or Referer header
        origin = request.headers.get("Origin") or request.headers.get("Referer")

        if origin and any(origin.startswith(allowed) for allowed in self.allowed_origins):
            return self.get_response(request)

        return JsonResponse({"error": "Unauthorized"}, status=403)