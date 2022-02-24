from doreah.control import mainfunction
from doreah.io import col

@mainfunction({'p':'preset','n':'new'},shield=True)
def main(url=None,preset=None,new=None,**additionals):
	print("ytd's functionality is now taken over by",col['yellow']("dlvh"))
	print(col['lightblue']("https://pypi.org/project/dlvh"))
