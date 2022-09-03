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
vs_BuildTools.exe --norestart --passive --downloadThenInstall --includeRecommended --config vs_buildtools.vsconfig

```

```
cmd.exe in C:\data\gits_temp\experiment_pynsist_qt6\examples\pyqt6_opencv_cython
cythonize -3 --inplace --exclude app\__init__.py app\*.py
```



```
BADBADBAD
See: https://stackoverflow.com/questions/66838238/cython-setup-py-cant-find-installed-visual-c-build-tools

`python -c "import sys; print(sys.version)"`
`3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]`

So I need MSVC version 1928
--> 1928 (Visual Studio 2019 Version 16.8 + 16.9)


Only this version is available: Visual Studio Community 2019 (version 16.11)
  vs_community__Visual_Studio_Community_2019_v16.11.exe (1.4 MBytes)

  MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28-16.9)
    2.66 GBytes
    Release notes: https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes#16.11.18
```

```
BADBADBAD
MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.29-16.11)
```


```
BADBADBAD
vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools

Desktop development with C++
  MSVC v143 - VS 2022 C++
  Windows 10 SDK (10.0.10-41.0)
  C++ CMake tools
  Testing tools
  C++ AddressSanitizer
```

