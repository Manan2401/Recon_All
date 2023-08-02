#!/usr/bin/env bash

clear

cat << "EOF"
    //   ) )                                            // | |           
   //___/ /   ___      ___      ___       __           //__| |    // //  
  / ___ (   //___) ) //   ) ) //   ) ) //   ) ) ____  / ___  |   // //   
 //   | |  //       //       //   / / //   / /       //    | |  // //    
//    | | ((____   ((____   ((___/ / //   / /       //     | | // //     


~~by Manan (https://github.com/Manan2401)

EOF

echo "Press CTRL+C to cancel."
echo
echo "Note that this script might ask for sudo password."
sleep 3

echo "Creating virtual environment..."
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

echo "Updating pip..."
sleep 1
pip3 install --upgrade pip

echo "Installing dependencies in 3 seconds..."
sleep 3

# Install dependencies
if command -v pip3 >/dev/null 2>&1; then
    pip3 install -r requirements.txt
else
    echo "python3-pip not installed, failed to install dependencies."
fi

sleep 1
echo "Making Recon_All into a Linux command..."
sleep 1

chmod +x Recon_All.py

if command -v pyinstaller >/dev/null 2>&1; then
    pyinstaller Recon_All.py --onefile -F
    sleep 1
    chmod +x dist/Recon_All
    sudo mv dist/Recon_All /usr/local/bin/
    rm Recon_All.spec
    rm -r build
    rm -r dist
    echo "Done! Type Recon_All in your terminal to start! OR Do you want to start Recon_All now? [y/n]"
    read -r answer
    if [ "$answer" = "y" ]; then
        Recon_All
    fi
else
    echo "pyinstaller not installed or not in PATH!"
fi
