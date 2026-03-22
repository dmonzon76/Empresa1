import re
from django.test import SimpleTestCase
from django.template import Template, Context
from django.urls import reverse, NoReverseMatch
from django.template.loader import get_template, TemplateDoesNotExist
from django.conf import settings
from pathlib import Path

class TemplateURLResolutionTests(SimpleTestCase):
    """
    Recorre todos los templates del proyecto y verifica que
    cada {% url 'namespace:name' %} sea resolvible.
    """

    URL_PATTERN = re.compile(r"{%\s*url\s+'([^']+)'\s*[^%]*%}")

    def test_all_template_urls_resolve(self):
        templates_dir = Path(settings.BASE_DIR) / "templates"

        for template_path in templates_dir.rglob("*.html"):
            with self.subTest(template=str(template_path)):
                content = template_path.read_text(encoding="utf-8")

                matches = self.URL_PATTERN.findall(content)

                for url_name in matches:
                    with self.subTest(url=url_name):
                        try:
                            reverse(url_name)
                        except NoReverseMatch:
                            self.fail(f"La URL '{url_name}' no existe pero aparece en {template_path}")