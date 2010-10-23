import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

class config:
    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates', '')
    TEMPLATE_ENV = Environment(loader = FileSystemLoader(TEMPLATE_PATH))
