mustafw@mustafw
$ python3

>>> languages = list("Python (3x)", "C#", "Java", "ReactJS")
>>> print(f"Languages that I know are \"{''.join((i if i!="C#" else "") for i in languages)}\"")
>>> exit("done")
