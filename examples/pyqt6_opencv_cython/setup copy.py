import os
import pathlib
import setuptools

from snakehouse import Multibuild, build, find_all

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent
DIRECTORY_APP = DIRECTORY_OF_THIS_FILE / "app"
DIRECTORY_CYTHON = DIRECTORY_OF_THIS_FILE / "build" / "cython"
DIRECTORY_CYTHON.mkdir(parents=True, exist_ok=True)

extensions = build(
    [
        Multibuild(
            extension_name="app",
            # files=find_all(directory=str(DIRECTORY_APP), include_c_files=True, only_c_files=False),
            files=list(find_all(directory="app", include_c_files=True, only_c_files=False)),
            dont_snakehouse=True,
        )
    ],
    compiler_directives={
        "language_level": "3",
    },
)

os.chdir(DIRECTORY_CYTHON)

setuptools.setup(
    name="app",
    version="0.1",
    packages=["app"],
    ext_modules=extensions,
    include_package_data=True,
    # package_dir={"app": "src"},
)
