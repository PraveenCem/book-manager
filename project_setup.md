# Project Setup & Troubleshooting Notes

## Project

**Book Manager**

A small learning application built to understand MongoDB fundamentals
using:

-   React
-   Python
-   FastAPI
-   MongoDB
-   Motor
-   Pydantic

The main purpose of this project is to learn MongoDB operations step by
step through a practical application.

------------------------------------------------------------------------

## Backend Structure

Current backend structure:

``` text
backend/
└── app/
    ├── core/
    │   └── database.py
    │
    └── models/
        ├── book.py
        └── book_repo.py
```

The repository layer currently contains MongoDB operations such as:

-   `find()`
-   `insert_one()`
-   `delete_one()`

------------------------------------------------------------------------

# Setup Issues & Resolutions

## Issue 1 --- `bson.ObjectId` could not be imported

### Problem

The following import produced an error:

``` python
from bson import ObjectId
```

Error:

``` text
ImportError: cannot import name 'ObjectId' from 'bson' (unknown location)
```

### Investigation

PyMongo was already installed:

``` text
pymongo 4.18.0
```

The standalone `bson` package was **not** installed:

``` text
pip show bson
WARNING: Package(s) not found: bson
```

However, Python was loading `bson` as a namespace package:

``` text
<module 'bson' (namespace)>
```

and the `bson` directory was missing `objectid.py`.

### Resolution

The PyMongo installation was incomplete/broken.

We reinstalled the existing PyMongo version:

``` bash
pip uninstall pymongo -y
pip install pymongo==4.18.0
```

Then verified:

``` bash
python -c "from bson import ObjectId; print(ObjectId)"
```

Successful result:

``` text
<class 'bson.objectid.ObjectId'>
```

### Important Note

Do **not** install the separate `bson` package.

`bson` is provided by PyMongo.

------------------------------------------------------------------------

## Issue 2 --- VS Code still showed a warning for `bson`

### Problem

Even after the terminal confirmed that:

``` python
from bson import ObjectId
```

worked correctly, VS Code still showed an import warning.

### Cause

VS Code/Pylance was using a different Python interpreter or had stale
import analysis.

### Resolution

In VS Code:

1.  Press `Ctrl + Shift + P`
2.  Select **Python: Select Interpreter**
3.  Select the project's virtual environment:

``` text
D:\pythonook-managerackendenv\Scripts\python.exe
```

4.  Reload VS Code using:

``` text
Developer: Reload Window
```

After selecting the correct interpreter and reloading, the warning
disappeared.

### Lesson

If an import works from the terminal but VS Code reports that it cannot
resolve the import, first check the Python interpreter selected by VS
Code.

------------------------------------------------------------------------

## Issue 3 --- `app.core.database` could not be imported

### Problem

This import:

``` python
from app.core.database import db
```

initially produced:

``` text
ModuleNotFoundError: No module named 'app.core'
```

### Investigation

The initial project structure was:

``` text
backend/
└── app/
    └── models/
        ├── book.py
        └── book_repo.py
```

There was no `core` directory at that point.

### Resolution

The correct structure was established:

``` text
backend/
└── app/
    ├── core/
    │   └── database.py
    │
    └── models/
        ├── book.py
        └── book_repo.py
```

Therefore this import is now structurally correct:

``` python
from app.core.database import db
```

### Lesson

Python imports depend on the actual project/package structure. Before
changing an import, verify that the referenced package and file actually
exist.

------------------------------------------------------------------------

# Current Python Packages

The project virtual environment currently uses:

``` text
fastapi           0.141.1
pydantic          2.13.5
motor             3.7.1
pymongo           4.18.0
python-dotenv     1.2.3
pydantic-settings 2.15.0
uvicorn           0.52.4
```

Other installed dependencies include packages required by these
libraries.

------------------------------------------------------------------------

# Useful Diagnostic Commands

### Check Python interpreter

``` bash
python --version
```

### Check installed packages

``` bash
pip list
```

### Check a specific package

``` bash
pip show pymongo
```

### Test a Python import directly

``` bash
python -c "from bson import ObjectId; print(ObjectId)"
```

### Test the application package import

Run from the `backend` directory:

``` bash
python -c "from app.core.database import db; print('app import OK')"
```

### View project structure on Windows

``` bash
tree /F
```

------------------------------------------------------------------------

# Project Learning Goal

This project is intentionally small.

The main MongoDB learning progression is:

``` text
CREATE
  ↓
insert_one()

READ
  ↓
find()
find_one()

UPDATE
  ↓
update_one()

DELETE
  ↓
delete_one()

FILTERING
  ↓
MongoDB query operators

SORTING / LIMITING
  ↓
sort()
limit()

INDEXES
  ↓
create_index()

AGGREGATION
  ↓
aggregate()
```

The goal is to understand the MongoDB operations themselves instead of
hiding them behind too many abstraction layers.

------------------------------------------------------------------------

# Troubleshooting Principle

When something fails:

1.  Reproduce the exact error.
2.  Check whether the package is actually installed.
3.  Check which Python interpreter is being used.
4.  Check the actual project/file structure.
5.  Test the failing import or operation independently.
6.  Only then change code or reinstall packages.

This helps distinguish between:

-   Code problems
-   Package installation problems
-   Python environment problems
-   VS Code/Pylance problems
-   Project structure/import problems
