#!/usr/bin/env python

from distutils.core import setup

setup(
	name='configuration',
	version='1.0',
	description='Python configuration utilities',
	author='Vladimir Roncevic',
	author_email='elektron.ronca@gmail.com',
	url='https://github.com/vroncevic/py_util',
	license='GPL 2017 Free software to use and distributed it.',
	long_description='Configuration mechanism for python app/tool/script.',
	keywords='configuration, xml, cfg, ini, json, yaml',
	platforms='POSIX',
	packages=[
		'configuration',
		'configuration.cfg',
		'configuration.ini',
		'configuration.json',
		'configuration.xml',
		'configuration.yaml'
	]
)

