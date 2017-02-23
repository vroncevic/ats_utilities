# encoding: utf-8
"""
app.build_date - class BuildDate

Usage:
	from app.build_date import BuildDate

	build_date = BuildDate("23 Feb 2017")
	date = build_date.get()
	build_date.set("22 Feb 2017")

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class BuildDate:
	"""
	Define class BuildDate with atribute(s) and method(s).
	Keep, set, get build date of App/Tool/Script.
	It defines:
		attribute:
			__build_date - build date of App/Tool/Script (use string format)
		method:
			__init__ - create and initial instance
			set - setting build date
			get - getting build date
	"""

	def __init__(self, build_date=None):
		"""
		@summary: Basic constructor
		@param build_date: build date (provide in string format)
		"""
		self.__build_date = build_date

	def set(self, build_date):
		"""
		@summary: Setter for build date of App/Tool/Script
		@param build_date: build date (provide in string format)
		"""
		self.__build_date = build_date

	def get(self):
		"""
		@summary: Getter for build date of App/Tool/Script
		@return: build date (string representation)
		"""
		return self.__build_date

