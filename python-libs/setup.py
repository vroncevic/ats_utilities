#!/usr/bin/env python

from distutils.core import setup

setup(
	name='app',
	version='1.0',
	description='Python utilities',
	author='Vladimir Roncevic',
	author_email='elektron.ronca@gmail.com',
	url='https://github.com/vroncevic/py_util',
	license='GPL 2017 Free software to use and distributed it.',
	long_description='Configuration mechanism for python app/tool/script.',
	keywords='app, configuration, logging, option, xml, cfg, ini, json, yaml',
	platforms='POSIX',
	packages=[
		'app',
		'app.configuration',
		'app.configuration.cfg',
		'app.configuration.ini',
		'app.configuration.json',
		'app.configuration.xml',
		'app.configuration.yaml',
		'app.logging',
		'app.option',
		'app.error'
	]
)

