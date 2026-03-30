import os
import sys

# 1. Ubicar la carpeta raíz del proyecto (tersicore/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. Agregar tersicore/ al PYTHONPATH
sys.path.insert(0, BASE_DIR)

# 3. Configurar settings correctamente
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# 4. Inicializar Django
import django
django.setup()

# 5. Auditoría
import importlib
from django.conf import settings

def audit_urls():
    print("\n=== AUDITORÍA DE URLS ===")
    for app in settings.INSTALLED_APPS:
        try:
            module = importlib.import_module(f"{app}.urls")
            urlpatterns = getattr(module, "urlpatterns", None)
            if urlpatterns is None:
                print(f"⚠ {app}.urls existe pero NO tiene urlpatterns")
            elif not isinstance(urlpatterns, list):
                print(f"❌ {app}.urls urlpatterns NO es una lista")
            else:
                print(f"✔ {app}.urls OK ({len(urlpatterns)} rutas)")
        except ModuleNotFoundError:
            pass

def audit_appconfigs():
    print("\n=== AUDITORÍA DE APPCONFIG ===")
    for app in settings.INSTALLED_APPS:
        try:
            module = importlib.import_module(app)
            if hasattr(module, "apps"):
                print(f"⚠ {app} tiene apps.py pero no está configurado correctamente")
        except Exception:
            pass

def run():
    audit_urls()
    audit_appconfigs()

if __name__ == "__main__":
    run()
