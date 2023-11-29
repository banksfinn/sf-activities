# sf-activities
Lots of code for lots of activities


# Python


## Initial Setup
You will need to have python3.10 installed.

```
source scripts/python_initial_setup.sh
```

This will create a virtual environment, and activate it for you.

This only needs to be run once.

## Subsequent Setup
Activating the virtual environment:
```
source venv/bin/activate
```

## Installing new packages
Ensure that the virtual environment has been activated and the existing requirements
have been installed
```
pip freeze > requirements.in
pip-compile
```
This freezes the list of explicit packages being installed, then outputs it in an easier
to read format with pip-compile.
