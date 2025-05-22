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

```
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
```
