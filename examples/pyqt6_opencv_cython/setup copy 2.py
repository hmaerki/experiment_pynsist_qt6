import warnings
import setuptools

from snakehouse import Multibuild, build, find_all, find_pyx_and_c

warnings.filterwarnings("ignore", "Config variable 'Py_DEBUG' is unset")
warnings.filterwarnings("ignore", "setup.py install is deprecated")

extensions = build(
    [
        Multibuild(
            extension_name="app",
            files=find_pyx_and_c(directory_path="app"),
            dont_snakehouse=False,
            nthreads=None,
        )
    ],
    compiler_directives={
        "language_level": "3",
    },
)

setuptools.setup(
    name="app",
    version="0.1",
    packages=["app",],
    ext_modules=extensions,
    include_package_data=True,
    package_data={"app": ["*.ui"]},
    exclude_package_data={
        "app": ["*.c", "*.h", "*.pyx", "*.py"],
    },
)
