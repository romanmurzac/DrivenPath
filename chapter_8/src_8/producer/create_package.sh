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
mkdir -p producer_package

# Install dependencies into the 'producer_package' directory.
echo "Installing dependencies..."
pip install -r requirements.txt --target producer_package/

# Copy lambda_function.py into the 'producer_package' directory.
echo "Copying lambda_function.py..."
cp "$LAMBDA_FUNCTION_NAME.py" producer_package/

# Move to 'producer_package' directory to create the zip archive.
cd producer_package

# Zip the contents of the 'producer_package' directory.
echo "Creating deployment producer_package..."
zip -r9 "../$ZIP_FILE" .

# Move back to the original directory and clean up.
cd ..
rm -rf producer_package

echo "Deployment package $ZIP_FILE created successfully."
