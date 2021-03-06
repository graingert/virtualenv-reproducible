"""
ensure virtualenv doesn't download new copies of pip/setuptools/wheel.
"""

__version__ = "0.1.0.post0"

import os


def pth(*args, **kwargs):
    os.environ.update(
        {
            "VIRTUALENV_NO_PERIODIC_UPDATE": "1",
            "VIRTUALENV_PIP": "embed",
            "VIRTUALENV_SETUPTOOLS": "embed",
            "VIRTUALENV_WHEEL": "embed",
        }
    )
