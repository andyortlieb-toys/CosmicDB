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

class excSchemaViolation(excCosmicDB):
	pass

def parsePath(path):
	if (not path):
		return []

	if (isinstance(path,str)):
		path = path.strip('/').split('/')

		## TODO: Try to support some sort of escape sequence.
		# while ('' in path):
		# 	idx = path.index('')

		# 	# Is this item surrounded?
		# 	if idx>0 and idx<(len(path)-1):
		# 		# Then join them!
		# 		path[idx] = '/'
		# 		path[idx] = ''.join(path[idx-1:idx+2])
		# 		path.pop(idx+1)
		# 		path.pop(idx-1)

		# 	else:
		# 		print "woop: %s: %s ... %s"%(idx, path[idx], path)

		# 		path.pop(idx)

	if (isinstance(path,list)):
		return path

	raise excPathType



class StorageBase:

	def __init__(self,*args,**kwargs):
		self.procedures = {}
		self.impl_init(*args,**kwargs)

	def _testSchema(self,path):
		print "STUB: Test Schema"

		return True

	def open(self,*args, **kwargs):
		return self.impl_open(*args, **kwargs)

	def close(self):
		return self.impl_close()

	def read(self,path=None):
		return self.impl_read(parsePath(path))

	def write(self,path,val):
		if (self._testSchema(path)):
			return self.impl_write(parsePath(path),val)
		else:
			raise excSchemaViolation

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




class StorageMemory(StorageBase):

	def impl_init(self,*args,**kwargs):
		return True

	def impl_open(self,*args,**kwargs):
		self.root = self.root if hasattr(self,'root') else NodeMemory()

	def impl_write(self,path,val):
		return self.root.set(path, val)

	def impl_read(self,path):
		return self.root.get(path)



if __name__=='__main__':

	Storage = StorageMemory()
	Storage.open()

	# Quick storage test
	Storage.root.set(['one','two','three'],"blablabla")
	print Storage.root.get(['one','two','three'])

	import IPython
	embedshell = IPython.Shell.IPShellEmbed(argv=["-colors", "NoColor"])
	embedshell()

