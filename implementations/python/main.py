#!/usr/bin/env python

fn = type(lambda:1)

class excCosmicDB(Exception):
	pass

class excProcedureNotFound(excCosmicDB):
	pass

class excPathType(excCosmicDB):
	pass

class excNodeNotFound(excCosmicDB):
	pass

class excNodeType(excCosmicDB):
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

	def set(self,path,val):

		# Are we the last path in the path? set the value.
		if (len(path)==1):
			self[path[0]] = val

		# Do recursivey things
		elif (len(path)>1):

			# Is it already an NodeMemory?
			if (self.has_key(path[0]) and (isinstance(self[path[0]], NodeMemory))):
				self[path[0]].set(path[1:], val)

			# The path pathibute needs to be created (or overwritten.  We need to trust our base class that it's okay.)
			else:
				self[path[0]] = NodeMemory()
				self[path[0]].set(path[1:], val)

		# Baffled.
		#else:
		#		raise TypeError "What on earth is going on here?" # FIXME

	def get(self,path=[]):
		if (not path):
			return self

		if (self.has_key(path[0])):
			if (len(path)==1):
				return self[path[0]]
			else:
				if (not isinstance(self[path[0]], NodeMemory)):
					raise excNodeType

				return self[path[0]].get(path[1:])

		raise excNodeNotFound




class BackendMemory(BackendBase):






	def impl_init(self,*args,**kwargs):
		self.storage = NodeMemory()

	def impl_write(self,path,val):
		self.node.write(path)



if __name__=='__main__':

	backend = BackendMemory()

	# Quick storage test
	backend.storage.set(['one','two','three'],"blablabla")
	print backend.storage.get(['one','two','three'])

	import IPython
	embedshell = IPython.Shell.IPShellEmbed(argv=["-colors", "NoColor"])
	embedshell()

