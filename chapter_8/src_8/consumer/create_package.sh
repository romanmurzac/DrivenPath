#!/bin/bash

# Set variables.
LAMBDA_FUNCTION_NAME="lambda_function"
ZIP_FILE="lambda_function.zip"

# Clean up any previous zip file.
if [ -f "$ZIP_FILE" ]; then
    echo "Removing old $ZIP_FILE..."
    rm "$ZIP_FILE"
fi

# Create a directory for dependencies if not exists.
mkdir -p consumer_package

# Install dependencies into the 'consumer_package' directory.
echo "Installing dependencies..."
pip install -r requirements.txt --target consumer_package/

# Copy lambda_function.py into the 'consumer_package' directory.
echo "Copying lambda_function.py..."
cp "$LAMBDA_FUNCTION_NAME.py" consumer_package/

# Move to 'consumer_package' directory to create the zip archive.
cd consumer_package

# Zip the contents of the 'consumer_package' directory.
echo "Creating deployment consumer_package..."
zip -r9 "../$ZIP_FILE" .

# Move back to the original directory and clean up.
cd ..
rm -rf consumer_package

echo "Deployment consumer_package $ZIP_FILE created successfully."
