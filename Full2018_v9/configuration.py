"""
Configuration file for mkShapesRDF script.

It's the only necessary python configuration file, all the other files are imported and defined by this one.
"""

treeName = 'Events'

# Tag used to identify the configuration folder version
tag = 'v9'

# File to use as runner script, default uses mkShapesRDF.shapeAnalysis.runner, otherwise specify path to script
runnerFile = "default"

# Output file name
outputFile = "mkShapes__{}.root".format(tag)

# Path to ouput folder
outputFolder  = "rootfiles__{}".format(tag)

# Path to batch folder (used for condor submission)
batchFolder = "condor"

# Path to configuration folder (will contain all the compiled configuration files)
configsFolder = "configs"

# Luminosity to normalize to (in 1/fb)
# https://github.com/latinos/LatinoAnalysis/blob/UL_production/NanoGardener/python/data/TrigMaker_cfg.py#L868 (874)
#  59.832475339
lumi = 59.83

# File with dict of aliases to define
aliasesFile = "aliases.py"

# File with dict of variables
variablesFile = "variables.py"

# File with dict of cuts
cutsFile = "cuts.py"

# File with dict of samples
samplesFile = "samples.py"

# File with dict of samples for plotting
plotFile = 'plot.py' 

# File with dict of structure (used to define processes in combine)
structureFile = "structure.py"

# Nuisances file for mkDatacards and for mkShape
nuisancesFile = "nuisances.py"

# Path to folder where to save plots
plotPath = "plots__{}".format(tag)

# This lines are executed right before the runner on the condor node
mountEOS = []

# List of imports to import when compiling the whole configuration folder, it should not contain imports used by configuration.py
imports = ["os", "glob", ("collections", "OrderedDict"), "ROOT"]

# List of files to compile
filesToExec = [
    samplesFile,
    aliasesFile,
    variablesFile,
    cutsFile,
    plotFile,
    nuisancesFile,
    structureFile,
]

# List of variables to keep in the compiled configuration folder
varsToKeep = [
    "batchVars",
    "outputFolder",
    "batchFolder",
    "configsFolder",
    "outputFile",
    "runnerFile",
    "tag",
    "samples",
    "aliases",
    "variables",
    ("cuts", {"cuts": "cuts", "preselections": "preselections"}),
    ("plot", {"plot": "plot", "groupPlot": "groupPlot", "legend": "legend"}),
    "nuisances",
    "structure",
    "lumi",
]

# List of variables to keep in the batch submission script (script.py)
batchVars = varsToKeep[varsToKeep.index("samples") :]

varsToKeep += ['plotPath']
