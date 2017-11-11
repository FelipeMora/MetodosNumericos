from cx_Freeze import setup, Executable
import os
import stat
os.chmod("D:\\DOCUMENTOS\\GitHub\\MetodosNumericos\\SetupCOM.py",stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH|stat.S_IXUSR|stat.S_IRUSR|stat.S_IWUSR|stat.S_IWGRP|stat.S_IXGRP)

os.environ['TCL_LIBRARY'] = "C:\\Python36-32\\Python36-32\\tcl\\tcl8.6\\"
os.environ['TK_LIBRARY'] = "C:\\Python36-32\\Python35-32\\tcl\\tk8.6\\"

setup(name="Métodos Numéricos",
      version="0.1",
      author = "Felipe Mora Fajardo",
      author_email = "felipedeveloper@hotmail.com",
      description="Programa para la solución de ecuaciones complejas por métodos numéricos desarrollado en Python",
      executables=[Executable("SerieDeTaylor.py")],
      targetName="MetodosNumericos.exe")