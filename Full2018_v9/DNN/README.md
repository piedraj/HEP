Deep neural network that aims at separating the VBF, top, WW, and ggH processes.


***************** Installation


The code has to be run with an el7 image that allows login to lxplus9 while emulating logging to lxplus7.cern.ch. Follow the [El7 image with condor support for lxplus](https://gitlab.cern.ch/cms-cat/cmssw-lxplus/) instructions to run the emulator. The start_el7.sh script to run the emulator needs to be executed every time accessing to lxplus.


ssh -Y -l <user> lxplus.cern.ch -o ServerAliveInterval=240
./start_el7.sh
unset SCRAM_ARCH
Initialize a CMSSW release.


cmsrel CMSSW_10_6_0
cd CMSSW_10_6_0/src/
cmsenv


cp -r miPathVFB/DNN .
----------------------

********************** Running


ssh -Y -l <user> lxplus.cern.ch -o ServerAliveInterval=240
./start_el7.sh
unset SCRAM_ARCH
cd CMSSW_10_6_0/src/

cmsenv
cd DNN
python keras_test.py


A mí me da algún mensaje de error al principio [1] pero parece que hace algo y me sale algo así al final [2] y me genera ciertos ficheros. Ahora bien, a partir de ahí como seguir no lo tengo muy claro, porque nunca he manejado estos códigos. Pero a lo mejor puedes ir probando a ver que te sale (y la segunda parte del código de dels kerasnew_to_C.py que en teoría creemos que es la parte que leía el .pkl

Ya me dices cuando puedas si te funciona más o menos (si te da errores podemos hacer un chat rápido antes del viernes para mirarlos).

Un saludo,

Jesús

[1]
Singularity> cd DNN_Final/
Singularity> python kerasnew_to_C.py
Using TensorFlow backend.
/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-requests/2.21.0-pafccj2/lib/python2.7/site-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.25.2) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
[2]
21470/21470 [==============================] - 0s 20us/step - loss: 0.5863 - categorical_accuracy: 0.7720 - val_loss: 0.6615 - val_categorical_accuracy: 0.7525
Epoch 229/500
21470/21470 [==============================] - 0s 18us/step - loss: 0.5886 - categorical_accuracy: 0.7710 - val_loss: 0.6655 - val_categorical_accuracy: 0.7499
Confusion Matrix
[[0.921 0.061 0.014 0.176]
 [0.071 0.78  0.053 0.137]
 [0.025 0.213 0.151 0.048]
 [0.127 0.042 0.025 0.4  ]]
Classification Report
              precision    recall  f1-score   support

         VBF       0.81      0.92      0.86      1628
         Top       0.71      0.78      0.74       853
          WW       0.62      0.15      0.24       285
         ggH       0.53      0.40      0.45       415

   micro avg       0.75      0.75      0.75      3181
   macro avg       0.67      0.56      0.58      3181
weighted avg       0.73      0.75      0.72      3181
