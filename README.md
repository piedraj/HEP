# 0. Documentation

* [mkShapesRDF](https://mkshapesrdf.readthedocs.io/en/latest/)
* [ROOT RDataFrame class reference](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
* [HTCondor batch system](https://twiki.cern.ch/twiki/bin/view/ABPComputing/LxbatchHTCondor)
* [Condor commands](https://twiki.cern.ch/twiki/bin/view/CENF/NeutrinoClusterCondorDoc)
* [PyROOT tutorials](https://root.cern.ch/doc/master/group__tutorial__pyroot.html)
* [SWAN](https://swan.cern.ch/)
* [Monte Carlo particle numbering scheme](https://pdg.lbl.gov/2020/reviews/rpp2020-rev-monte-carlo-numbering.pdf)

# 1. Installation

Log in to the CERN LXPLUS cluster.

    ssh -Y -l <username> lxplus.cern.ch -o ServerAliveInterval=240

Switch to a [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) shell.
    
    bash -l

Clone the project.

    git clone https://github.com/BlancoFS/mkShapesRDF.git
    cd mkShapesRDF
    git checkout Run3

Once you have cloned the project you need to modify `install.sh`.

    emacs -nw install.sh

Add the following line right before `python -m pip install -e ".[docs,dev,processor]"`.

    unset SSH_ASKPASS

Now you can proceed with the installation.

    ./install.sh

<!---
*Only necessary if Grid access is needed.* Set `eosTmpWorkDir` as `/eos/home-p/piedra/work/LatinosPostProcessing` in `Sites_cfg.py`. Write your home path instead of `/home-p/piedra`.

    emacs -nw mkShapesRDF/processor/framework/Sites_cfg.py
-->

Get the analysis configuration.

    git clone https://github.com/piedraj/HEP

# 2. Always do

Everytime you start a new session you need to follow these steps.

    ssh -Y -l <username> lxplus.cern.ch -o ServerAliveInterval=240
    bash -l
    cd mkShapesRDF
    source start.sh

Currently the analysis can be performed on `v7` or `v9` samples. To choose one set simply go to the corresponding folder.
    
    cd HEP/Full2018_v7/
    cd HEP/Full2018_v9/

<!---
*Only necessary if Grid access is needed.* Produce a valid VOMS proxy.

    voms-proxy-init -voms cms -rfc --valid 168:0
-->

# 3. Produce the analysis histograms

| Action                        | Command                                                                 |
|:------------------------------|:------------------------------------------------------------------------|
| Compile                       | `mkShapesRDF --compile 1`                                               |
| Run on local                  | `mkShapesRDF --operationMode 0 --folder . --doBatch 0 --limitEvents 10` |
| Run on batch                  | `mkShapesRDF --operationMode 0 --folder . --doBatch 1`                  |
| Check filled jobs             | `mkShapesRDF --operationMode 1 --folder .`                              |
| Resubmit jobs                 | `mkShapesRDF --operationMode 1 --folder . --resubmit 1`                 |
| Merge root files (batch only) | `mkShapesRDF --operationMode 2 --folder .`                              |
| Available arguments           | `mkShapesRDF --help`                                                    |

Always proceed as follows:

1. **Modify the code.** This is where the analaysis development starts.
2. **Compile.** If you miss this step the implemented changes won't be considered when running the code.
3. **Run on local.** This is a very important step, as it allows you to check if any error has been introduced with the latest modifications.
4. **Run on batch.**
5. **Merge root files.**

# 4. Check job status

    condor_q

If you need to cancel all the submitted jobs.

    condor_rm <username>

# 5. Plot the analysis histograms

    mkPlot --showIntegralLegend 1 --onlyPlot cratio --fileFormats png

If needed, the available arguments can be printed.

    mkPlot --help

When running on batch check that you have produced these [v7](https://piedra.web.cern.ch/plots-v7/) or [v9](https://piedra.web.cern.ch/plots-v9/) default distributions.

# 6. How to know a tree content

Both data and Monte Carlo (MC) files have the event variables stored in a ROOT `TTree` object named `Events`. Once you have followed the instructions below, you just need to open the file `TreeContent.h` to see all the variables.

    root -l /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9/nanoLatino_TTJets__part52.root
    Events->MakeClass("TreeContent")
    .q

    emacs -nw TreeContent.h

# 7. Share on the web

Once the analysis plots have been produced, the best way to look at them is by [creating a webEOS site](https://webeos.docs.cern.ch/create_site/).
