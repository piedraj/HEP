#include "TLorentzVector.h"


float mlj(float lepton_pt,
	  float lepton_eta,
	  float lepton_phi,
	  float jet_pt,
	  float jet_eta,
	  float jet_phi)
{
  TLorentzVector lepton;
  TLorentzVector jet;

  lepton.SetPtEtaPhiM(lepton_pt, lepton_eta, lepton_phi, 0.);
  jet.SetPtEtaPhiM(jet_pt, jet_eta, jet_phi, 0.);

  return (lepton+jet).M();
}
