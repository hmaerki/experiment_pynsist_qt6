# Description

This example shows how to include **OpenCV** in a **PyQt6** application
using **Python 3.8**.

The application requires some sort of camera to display.

### Requirements

- FFMPEG
- Visual C++ Redistributable for Visual Studio 2015

==============================

# Install VC++
https://visualstudio.microsoft.com/visual-cpp-build-tools/
  vs_BuildTools.exe (2.08 MBytes)

```
vs_BuildTools.exe --help
vs_BuildTools.exe --norestart --passive --downloadThenInstall --includeRecommended --config <FULLPATH...>\vs_buildtools.vsconfig
```

# Install NSIS
https://nsis.sourceforge.io/Download
nsis-3.08-setup.exe
Install using defaults

# Python requirements
```
pip install wheel merak cython pynsist
```

# Build the installer
```
build_installer.bat
```

## Test the application without the installer
```
cd build\nsis\Python
python "..\Camera_App_Cython_(PyQt6).launch.pyw"
```
