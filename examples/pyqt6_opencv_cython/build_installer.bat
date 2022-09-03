rmdir /q/s build

cythonize -3 app\*.py
@REM python setup.py bdist_wheel --dist-dir build/cython
python setup.py --verbose clean --all bdist_wheel
@REM python setup.py bdist_wheel
@rem pynsist.exe --no-makensis .\installer.cfg
pynsist.exe .\installer.cfg
