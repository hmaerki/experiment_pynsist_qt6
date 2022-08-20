import os
import pathlib
import setuptools

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent
DIRECTORY_CYTHON = DIRECTORY_OF_THIS_FILE / "build" / "cython"
assert DIRECTORY_CYTHON.exists()

os.chdir(DIRECTORY_CYTHON)

setuptools.setup(
    name="app",
    version="0.1.0",
    packages=["app"],
    include_package_data=True,
    package_data={"app": ["*"]},
)
