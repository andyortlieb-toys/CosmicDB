#!/usr/bin/env python

fn = type(lambda:1)

class excCosmicDB(Exception):
	pass

class excProcedureNotFound(excCosmicDB):
	pass

class excPathType(excCosmicDB):
	pass

def parsePath(path):
	if (type(path)==str):
		return path.split('/')
	elif (type(path)==list):
		return path
	else:
		raise excPathType


class BackendBase:

	def __init__(self,*args,**kwargs):
		self.procedures = {}
		self.impl_init(*args,**kwargs)

	def _testSchema(self,path):
		print "STUB: Test Schema"

		return True

	def open(self,addr):
		self.impl_open(addr)

	def close(self):
		self.impl_close()

	def read(self,path):
		self.impl_read(path)

	def write(self,path,val):
		if (self._testSchema(path)):
			self.impl_write(path,val)

	def procedure(self,method,*args,**kwargs):
		if (type(method)==str):
			if (method not in self.procedures):
				raise excProcedureNotFound


		#elif (type(method))==fn):
		#	pass

		else:
			raise TypeError("Procedure must be a string or a function")


class NodeMemory(dict):
	def __init__(self):
		self = {}

	def set(self,attr,val):

		# Are we the last attr in the path? set the value.
		if (len(attr)==1):
			self[attr[0]] = val

		# Do recursivey things
		elif (len(attr)>1):

			# Is it already an NodeMemory?
			if (self.has_key(attr[0]) and (isinstance(self[attr[0]], NodeMemory))):
				self[attr[0]].set(attr[1:], val)

			# The path attribute needs to be created (or overwritten.  We need to trust our base class that it's okay.)
			else:
				self[attr[0]] = NodeMemory()
				self[attr[0]].set(attr[1:], val)

		# Baffled.
		#else:
		#		raise TypeError "What on earth is going on here?" # FIXME

	#def get(self,attr):

class BackendMemory(BackendBase):






	def impl_init(self,*args,**kwargs):
		self.storage = NodeMemory()

	def impl_write(self,path,val):
		self.node.write(path)



if __name__=='__main__':

	backend = BackendMemory()

	import IPython
	embedshell = IPython.Shell.IPShellEmbed(argv=["-colors", "NoColor"])
	embedshell()
