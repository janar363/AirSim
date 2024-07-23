# setup.py
from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
import pybind11
import sys

# Set the system platform
platform = sys.platform

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "wind_data_processor",
        ["wind_data_processor_python_wrapper.cpp", "wind_data_processor.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++',
        extra_compile_args=['-std=c++17'] if platform != 'win32' else ['/std:c++17'],
    ),
]

# Setup configuration
setup(
    name="wind_data_processor",
    version="0.1.0",
    author="Janardhan karravula",
    author_email="janardhan.karravula@slu.edu",
    description="A Python wrapper for the wind data processor C++ library",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)

#  python WDP_setup.py build_ext --inplace     