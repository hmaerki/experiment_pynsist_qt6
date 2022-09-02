@rem only required when using 'venv'
set PYTHON_CMD=C:\data\MTANA\gits_experiments\experiment_pynsist_qt6\.venv\Scripts\python.exe

rmdir /q/s build\cython
merak cythonize app build\cython
copy app\mainwindow.ui build\cython\app
del build\cython\app\*.exp build\cython\app\*.lib
@rem copy dummy_placeholder.py build\cython\app
python setup.py bdist_wheel
@rem pynsist.exe --no-makensis .\installer.cfg
pynsist.exe .\installer.cfg
