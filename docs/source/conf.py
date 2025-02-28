import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Thông tin dự án
project = 'Handson ML3'
author = 'Pham Binh'
release = '1.0'

# Kích hoạt Sphinx và các extension
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'nbsphinx',  # Hỗ trợ Jupyter Notebook
    'myst_parser'  # Hỗ trợ Markdown
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

html_theme = 'sphinx_rtd_theme'
