#!/bin/bash


# Set the installation directory
#install_dir="Nemo_dir"

# Create a new directory for the application
#mkdir -p "$install_dir"

# Copy necessary files to the installation directory
#cp nemo_2.py "$install_dir"
#cp start.sh "$install_dir"

# Optionally, copy other required files
# cp -r other_files "$install_dir"

# Grant execution permissions to the launch script
#chmod +x "$install_dir/start.sh"

# Update PATH and PYTHONPATH in the user's shell configuration file
#echo "export PATH=\$PATH:$(realpath $install_dir)" >> ~/.bashrc
#echo "export PYTHONPATH=\$PYTHONPATH:$(realpath $install_dir)" >> ~/.bashrc

# Apply changes to the current shell session
#source ~/.bashrc

#echo "Installation completed. Run the application using:"
#echo "cd $install_dir"
#echo "./launch_script.sh"

# Installation script for your application

# Set the installation directory
INSTALL_DIR="/usr/local/bin/your_app"
#INSTALL_DIR="/home/your_app"

# Create the installation directory if it doesn't exist
sudo mkdir -p $INSTALL_DIR

# Copy the Python script and launch script to the installation directory
sudo cp nemo_2.py $INSTALL_DIR
sudo cp start.sh $INSTALL_DIR
#sudo cp bin.txt
#sudo cp bin1.txt

# Set execution permissions for the scripts
sudo chmod +x $INSTALL_DIR/nemo_2.py
sudo chmod +x $INSTALL_DIR/start.sh

# Add the installation directory to the PATH
echo "export PATH=\$PATH:$INSTALL_DIR" | sudo tee -a /etc/profile

# Add the installation directory to the PYTHONPATH
echo "export PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR" | sudo tee -a /etc/profile

# Source the profile to apply changes immediately
source /etc/profile
source ~/.bashrc

echo "Installation completed. You can now launch your application with the command: start.sh"

