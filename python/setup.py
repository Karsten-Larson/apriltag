#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import shutil

# Copy the shared library to the python directory so it can be found
lib_src = os.path.join(os.path.dirname(__file__), '..', 'build', 'lib', 'libapriltag.so')
lib_dest = os.path.join(os.path.dirname(__file__), 'libapriltag.so')

if os.path.exists(lib_src):
    shutil.copy2(lib_src, lib_dest)
    print(f"Copied {lib_src} to {lib_dest}")
else:
    print(f"Warning: {lib_src} not found. Make sure to build the library first.")

setup(
    name="apriltag",
    version="0.0.1",
    author="AprilTag Developers",
    description="AprilTag detection library Python wrapper",
    long_description="Python wrapper for the AprilTag fiducial marker detection library",
    py_modules=["apriltag"],
    install_requires=[
        "numpy",
    ],
    extras_require={
        "opencv": ["opencv-python"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires='>=3.6',
)