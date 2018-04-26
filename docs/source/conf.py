# -*- coding: utf-8 -*-
DESCRIPTION = (
    'pyecharts map extensions - world countries - python package' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'echarts-countries-pypkg'
copyright = u'2018 pyecharts dev team'
version = '0.1.4'
release = '0.1.4'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'echarts-countries-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'echarts-countries-pypkg.tex',
     'echarts-countries-pypkg Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'echarts-countries-pypkg',
     'echarts-countries-pypkg Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'echarts-countries-pypkg',
     'echarts-countries-pypkg Documentation',
     'pyecharts dev team', 'echarts-countries-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
