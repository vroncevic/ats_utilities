# encoding: utf-8
"""
app.error.lookup_error - class AppError

Usage:
	from app.error.lookup_error import AppError

	try:
		if important_key not in resource_dict and not ok_to_be_missing:
			raise AppError("resource is missing, and that is not ok.")
	except AppError as e:
		print("Error: ", e)
		# ...

@date: Mar 07, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AppError(LookupError):
	"""
	Define class AppError with attribute(s) and method(s).
	Lookup error mechanism.
	It defines:
		attribute:
			None
		method:
			None
	"""