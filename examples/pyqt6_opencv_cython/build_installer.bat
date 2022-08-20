rmdir build\cython
merak cythonize app build\cython
copy app\mainwindow.ui build\cython\app
python setup.py bdist_wheel
@rem pynsist.exe --no-makensis .\installer.cfg
pynsist.exe .\installer.cfg
