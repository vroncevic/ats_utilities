# encoding: utf-8
"""
app.configuration.file_config - class FileConfig

Usage:
	from app.configuration.file_config import FileConfig

	config_file = "main_configuration.json"
	if FileConfig.check_file(config_file):
		if FileConfig.check_format(config_file, ".json"):
			print("File: {0} is regular!".format(config_file))

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from os.path import exists, isfile, splitext

class FileConfig(object):
	"""
	Define class FileConfig with attribute(s) and method(s).
	File can contain configuration in next formats:
	XML  -  Configuration described by Extensible Markup Language.
	INI  -  Configuration described by basic structure composed of sections,
			properties, and values.
	CFG  -  Configuration described by keys and values.
	YAML -  Configuration described by basic structure composed of sections,
			properties, and values.
	JSON -  Configuration described by basic structure composed of sections,
			properties, and values.
	It defines:
		attribute:
			None
		method:
			check_file - Check configuration file path
			check_format - Check configuration file format by extension
	"""

	@classmethod
	def check_file(cls, file_path):
		"""
		:arg: file_path - Absolute configuration file path
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		if exists(file_path) and isfile(file_path):
			return True
		return False

	@classmethod
	def check_format(cls, file_path, file_extension):
		"""
		:arg: file_path - Absolute configuration file path
		:type: str
		:arg: file_extension - File format (file extension)
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		ext = splitext(file_path)[-1].lower()
		if ext == file_extension:
			return True
		return False
