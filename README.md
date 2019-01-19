# Robot-2019
Destination: Deep Space

# Installing to the Robot itself (
py install -rev

# Upgrading from the prior 2018 libraries
If you already installed the libraries from last year, you'll need to update to 2019 in order to get the 2019 game simulator field (in addition to the other proper libraries)

## OSX (Mac)
To upgrade from previous versions type in 
make devenvironment (it will install and/or upgrade to the lastest)

## Windows
In the Spyder window/terminal:
pip install pyfrc --upgrade
pip install pyrobot --upgrade
pip install robotpy-ctre --upgrade

# Running the Simulator
## OSX (Mac)
python3 robot.py sim

# Installation

## Windows
You'll probably have to update Spyder to add "sim" to the option

## OSX (Mac)
brew install python3
make devenvironment

## Linux

# Troubleshooting

## Hal error when running robot.py
ModuleNotFoundError: No module named 'hal'
DO NOT attempt to pip3 install hal. This is the wrong module. Instead, you are missing the pyfrc packages. pip3 install pyfrc
