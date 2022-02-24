from doreah.control import mainfunction
from doreah.io import col

@mainfunction({'p':'preset','n':'new'},shield=True)
def main(url=None,preset=None,new=None,**additionals):
	print("fsclean is now its own package")
	print(col['lightblue']("https://pypi.org/project/fsclean"))
