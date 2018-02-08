pip freeze
nosetests --with-coverage --cover-package echarts_countries_pypkg --cover-package tests  tests docs/source echarts_countries_pypkg && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
