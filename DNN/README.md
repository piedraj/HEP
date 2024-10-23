Deep neural network (DNN) that reads `v9` Monte Carlo files to separate the VBF, top, WW, and ggH processes.

# 0. Documentation

* [The Keras Sequential model](https://keras.io/guides/sequential_model/)

# 1. Installation

Log in to the CERN LXPLUS cluster.

    ssh -Y -l <user> lxplus.cern.ch -o ServerAliveInterval=240

The code has to be run with an el7 image. Follow the [El7 image with condor support for lxplus](https://gitlab.cern.ch/cms-cat/cmssw-lxplus/) instructions to create a `start_el7.sh` script, and then make it executable.

    chmod u+x start_el7.sh

Now you can run it.

    ./start_el7.sh

Initialize a CMSSW release.

    unset SCRAM_ARCH
    cmsrel CMSSW_10_6_0
    cd CMSSW_10_6_0/src
    cmsenv

Get the necessary files to run the DNN.

    mkdir $CMSSW_BASE/src/DNN
    cd $CMSSW_BASE/src/DNN
    
    wget https://raw.githubusercontent.com/piedraj/TFG/refs/heads/main/DNN/loader.py
    wget https://raw.githubusercontent.com/piedraj/TFG/refs/heads/main/DNN/keras_test.py

# 2. Always do

Everytime you start a new session you need to follow these steps.

    ssh -Y -l <user> lxplus.cern.ch -o ServerAliveInterval=240
    ./start_el7.sh
    cd CMSSW_10_6_0/src/
    cmsenv

# 3. Run the DNN

    cd $CMSSW_BASE/src/DNN
    python keras_test.py

Current output.

```
1771846
1526781
1767596
1424739
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense_1 (Dense)              (None, 240)               5280
_________________________________________________________________
dropout_1 (Dropout)          (None, 240)               0
_________________________________________________________________
dense_2 (Dense)              (None, 120)               28920
_________________________________________________________________
dropout_2 (Dropout)          (None, 120)               0
_________________________________________________________________
dense_3 (Dense)              (None, 60)                7260
_________________________________________________________________
dropout_3 (Dropout)          (None, 60)                0
_________________________________________________________________
dense_4 (Dense)              (None, 4)                 244
=================================================================
Total params: 41,704
Trainable params: 41,704
Non-trainable params: 0
_________________________________________________________________
Traceback (most recent call last):
  File "keras_test.py", line 123, in <module>
    validation_split=0.25)
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-Keras/2.2.4-pafccj2/lib/python2.7/site-packages/keras/engine/training.py", line 952, in fit
    batch_size=batch_size)
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-Keras/2.2.4-pafccj2/lib/python2.7/site-packages/keras/engine/training.py", line 789, in _standardize_user_data
    exception_prefix='target')
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-Keras/2.2.4-pafccj2/lib/python2.7/site-packages/keras/engine/training_utils.py", line 138, in standardize_input_data
    str(data_shape))
ValueError: Error when checking target: expected dense_4 to have shape (4,) but got array with shape (2,)
```
