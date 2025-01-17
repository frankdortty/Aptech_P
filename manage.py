import importlib.util

settings_spec = importlib.util.find_spec("settings")
if settings_spec is None:
    import sys
    sys.stderr.write(
        "Error: Can't find the file 'settings.py' in the directory containing %r. "
        "It appears you've customized things.\n"
        "You'll have to run django-admin.py, passing it your settings module.\n" % __file__
    )
    sys.exit(1)


import settings

if __name__ == "__main__":
    execute_manager(settings)
