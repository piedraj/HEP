# Cloned from https://github.com/latinos/PlotsConfigurations/tree/master/Configurations/VBF/DNN_Final

import os
import ROOT
import root_numpy

dir18 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9/'


#-------------------------------------------------------------------------------
# VBF
#-------------------------------------------------------------------------------
def load_dataset_vbf (max_entries = -1) :

  _branches = ["mjj", "mll", "ptll", "detajj", "dphill", "PuppiMET_pt", "mTi", "dphillmet", "drll", "ht", "mth", "Lepton_pt[0]", "Lepton_pt[1]", "Lepton_eta[0]", "Lepton_eta[1]", "CleanJet_pt[0]", "CleanJet_pt[1]", "CleanJet_eta[0]", "CleanJet_eta[1]"]

  chain = ROOT.TChain('Events')

  for i in range(0,3,1) : # Up to 5 (of 22)
    chain.Add(dir18+'nanoLatino_VBFHToWWTo2L2Nu_M125__part' + str(i) + '.root')

  print chain.GetEntries()
  
  _dataset = root_numpy.tree2array (chain,
      branches = _branches,
      selection = 'mll>12 && PuppiMET_pt>20 && Lepton_pt[0]>25 && Lepton_pt[1]>13 && Alt$(Lepton_pt[2],0)<10 && Sum$(CleanJet_pt>30)==2',
      stop = max_entries
     )

  return { b : _dataset[b] for b in _branches }


#-------------------------------------------------------------------------------
# Top
#-------------------------------------------------------------------------------
def load_dataset_top (max_entries = -1) :

  _branches = ["mjj", "mll", "ptll", "detajj", "dphill", "PuppiMET_pt", "mTi", "dphillmet", "drll", "ht", "mth", "Lepton_pt[0]", "Lepton_pt[1]", "Lepton_eta[0]", "Lepton_eta[1]", "CleanJet_pt[0]", "CleanJet_pt[1]", "CleanJet_eta[0]", "CleanJet_eta[1]"]
  
  chain = ROOT.TChain('Events')

  for i in range(0,1,1) : # Up to 1 (of 154)
    chain.Add(dir18+'nanoLatino_TTTo2L2Nu__part' + str(i) + '.root')
  
  print chain.GetEntries()
  
  _dataset = root_numpy.tree2array (chain,
      branches = _branches,
      selection = 'mll>12 && PuppiMET_pt>20 && Lepton_pt[0]>25 && Lepton_pt[1]>13 && Alt$(Lepton_pt[2],0)<10 && Sum$(CleanJet_pt>30)==2',
      stop = max_entries
     )

  return { b : _dataset[b] for b in _branches }


#-------------------------------------------------------------------------------
# WW
#-------------------------------------------------------------------------------
def load_dataset_ww (max_entries = -1) :

  _branches = ["mjj", "mll", "ptll", "detajj", "dphill", "PuppiMET_pt", "mTi", "dphillmet", "drll", "ht", "mth", "Lepton_pt[0]", "Lepton_pt[1]", "Lepton_eta[0]", "Lepton_eta[1]", "CleanJet_pt[0]", "CleanJet_pt[1]", "CleanJet_eta[0]", "CleanJet_eta[1]"]

  chain = ROOT.TChain('Events')
  
  for i in range(0,3,1) : # Up to 2 (of 36)
    chain.Add(dir18+'nanoLatino_WWTo2L2Nu__part' + str(i) + '.root')
  
  print chain.GetEntries()

  _dataset = root_numpy.tree2array (chain, 
      branches = _branches,
      selection = 'mll>12 && PuppiMET_pt>20 && Lepton_pt[0]>25 && Lepton_pt[1]>13 && Alt$(Lepton_pt[2],0)<10 && Sum$(CleanJet_pt>30)==2 && Sum$(GenPart_pdgId==25)==0',
      stop = max_entries
     )

  return { b : _dataset[b] for b in _branches }


#-------------------------------------------------------------------------------
# ggH
#-------------------------------------------------------------------------------
def load_dataset_ggh (max_entries = -1) :

  _branches = ["mjj", "mll", "ptll", "detajj", "dphill", "PuppiMET_pt", "mTi", "dphillmet", "drll", "ht", "mth", "Lepton_pt[0]", "Lepton_pt[1]", "Lepton_eta[0]", "Lepton_eta[1]", "CleanJet_pt[0]", "CleanJet_pt[1]", "CleanJet_eta[0]", "CleanJet_eta[1]"]

  chain = ROOT.TChain('Events')  

  for i in range(0,4,1) : # Up to 5 (of 25)
    chain.Add(dir18+'nanoLatino_GluGluHToWWTo2L2Nu_M125__part' + str(i) + '.root')

  print chain.GetEntries()

  _dataset = root_numpy.tree2array (chain, 
      branches = _branches,
      selection = 'mll>12 && PuppiMET_pt>20 && Lepton_pt[0]>25 && Lepton_pt[1]>13 && Alt$(Lepton_pt[2],0)<10 && Sum$(CleanJet_pt>30)==2',
      stop = max_entries
     )

  return { b : _dataset[b] for b in _branches }


if __name__ == '__main__':
  print load_dataset (100)
