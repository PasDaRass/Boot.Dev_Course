In Python, each .py file is a module, and we can import functions, variables, and classes from one module into another with the import statement. <br />
The name of a module is the filename (without the .py extension).

```
# import the connect_database function
# and the database_version variable
# from database.py into the current file
from database import connect_database, database_version
```

If you want to import everything from a module, you can use the * character:
```
# import everything from the module
# database.py into the current file
from database import *
```
