# encoding: utf-8
"""
configuration.file_config - class FileConfig

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from os.path import exists, isfile, splitext

class FileConfig:
	"""
	Define class FileConfig with atribute(s) and method(s).
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
			check_file - check configuration file path
			check_format - check configuration file format by extension
	"""

	@classmethod
	def check_file(cls, file_path):
		"""
		@summary: Check configuration file path (existing and is it file)
		@param file_path: absolute configuration file path
		@return: Success return true, else return false
		"""
		if exists(file_path):
			if isfile(file_path):
				return True
		return False

	@classmethod
	def check_format(cls, file_path, file_extension):
		"""
		@summary: Check configuration file format by extension
		@param file_path: absolute configuration file path
		@param file_extension: file format (file extension)
		@return: Success return true, else return false
		"""
		ext = splitext(file_path)[-1].lower()
		if ext == file_extension:
			return True
		return False

