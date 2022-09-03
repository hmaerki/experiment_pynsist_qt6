import os
from distutils import log
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

# from wheel.pep425tags import get_impl_ver
import warnings
import setuptools

from snakehouse import Multibuild, build, find_pyx_and_c

warnings.filterwarnings("ignore", "Config variable 'Py_DEBUG' is unset")
warnings.filterwarnings("ignore", "setup.py install is deprecated")

# https://gist.github.com/ophers/093c31bce28f1356b7bf149a99e58326
# Produce a Python Wheel without sources with CLI option --exclude-source-files
class build_py(_build_py):
    def initialize_options(self):
        _build_py.initialize_options(self)
        wc = self.get_finalized_command("bdist_wheel", 0)
        self.exclude_source_files = wc and wc.exclude_source_files

    def finalize_options(self):
        if self.exclude_source_files:
            self.force = 1
            self.compile = 1
        _build_py.finalize_options(self)

    def byte_compile(self, files):
        # _build_py.byte_compile(self, files)
        if self.exclude_source_files:
            for file in files:
                if file.endswith(".py"):
                    os.unlink(file)
                    log.info("removing source file %s", file)


class bdist_wheel(_bdist_wheel):
    _bdist_wheel.user_options.append(
        ("exclude-source-files", None, "remove all .py files from the generated wheel")
    )

    def initialize_options(self):
        _bdist_wheel.initialize_options(self)
        self.python_tag = None
        self.exclude_source_files = False

    def finalize_options(self):
        if self.python_tag is None:
            self.python_tag = "py"
            # if self.exclude_source_files:
            #     self.python_tag = 'py' + get_impl_ver()
            # else:
            #     self.python_tag = 'py' + get_impl_ver()[0]
        _bdist_wheel.finalize_options(self)


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
    packages=["app"],
    ext_modules=extensions,
    include_package_data=True,
    package_data={"app": ["*.ui"]},
    exclude_package_data={
        "app": ["*.c", "*.h", "*.pyx"],
    },
    cmdclass={"build_py": build_py, "bdist_wheel": bdist_wheel},
)
