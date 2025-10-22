import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('../../'))

project = 'UTI - Educação em Terapia Intensiva'
current_year = datetime.now().year
copyright = f'{current_year}, Comunidade UTI'
extensions = [
    'myst_parser',
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.ipynb': 'nbsphinx',
}
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme = 'alabaster'
html_static_path = ['_static']

nbsphinx_execute = 'never'
nb_execution_timeout = 300

myst_enable_extensions = [
    'colon_fence',
]

todo_include_todos = True
