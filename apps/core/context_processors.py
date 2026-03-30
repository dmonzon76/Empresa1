from .routes import ROUTES

def routes_context(request):
    return {
        "ROUTES": ROUTES
    }
