from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            "script": "sourcewin.py",
            "icon_resources": [(1, "randomcopy.ico")]
        }
    ],
)
