from doreah.control import mainfunction
from doreah.io import col

@mainfunction({},shield=True)
def main(*args):
	print("Flacco's functionality is now taken over by",col['yellow']("mumema"))
	print(col['lightblue']("https://pypi.org/project/mumema"))
