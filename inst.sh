#!/bin/bash


# Set the installation directory
install_dir="Nemo_dir"

# Create a new directory for the application
mkdir -p "$install_dir"

# Copy necessary files to the installation directory
cp nemo_2.py "$install_dir"
cp start.sh "$install_dir"

# Optionally, copy other required files
# cp -r other_files "$install_dir"

# Grant execution permissions to the launch script
chmod +x "$install_dir/start.sh"

echo "Installation completed. Run the application using:"
echo "cd $install_dir"
echo "./start.sh"

