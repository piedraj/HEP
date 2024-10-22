Deep neural network that aims at separating the VBF, top, WW, and ggH processes.

# 0. Documentation

To be filled.

# 1. Installation

The code has to be run with an el7 image that allows login to 'lxplus' while emulating logging to 'lxplus7.cern.ch'. Follow the [El7 image with condor support for lxplus](https://gitlab.cern.ch/cms-cat/cmssw-lxplus/) instructions to run the emulator.

ssh -Y -l <user> lxplus.cern.ch -o ServerAliveInterval=240
./start_el7.sh
unset SCRAM_ARCH
Initialize a CMSSW release.


cmsrel CMSSW_10_6_0
cd CMSSW_10_6_0/src/
cmsenv


cp -r miPathVFB/DNN .
----------------------

# 2. Always do

Everytime you start a new session you need to follow these steps.

ssh -Y -l <user> lxplus.cern.ch -o ServerAliveInterval=240
./start_el7.sh
unset SCRAM_ARCH
cd CMSSW_10_6_0/src/

cmsenv

# 3. Run the DNN


cd DNN
python keras_test.py
