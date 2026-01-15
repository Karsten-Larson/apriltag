#!/bin/bash

# Build script for AprilTag library with Python wrapper
# This script builds the AprilTag library and sets up the Python wrapper for import

set -e  # Exit on any error

echo "Building AprilTag library..."

# Create build directory if it doesn't exist
if [ ! -d "build" ]; then
    mkdir build
fi

cd build

# Run CMake
echo "Running CMake..."
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build with make
echo "Building with make..."
make -j4

cd ..

# Install Python wrapper globally
echo "Installing Python wrapper globally..."
cd python
python3 setup.py install --user  # Install to user site-packages for global access
cd ..

# Test the import
echo "Testing Python import..."
if python3 -c "import apriltag; print('AprilTag Python wrapper imported successfully!')"; then
    echo "Build and setup completed successfully!"
    echo ""
    echo "Usage:"
    echo "  - Import in Python: import apriltag"
    echo "  - Create detector: detector = apriltag.Detector()"
    echo "  - Note: OpenCV is optional and not required for the Python wrapper"
else
    echo "Error: Python import failed. Check build output above."
    exit 1
fi