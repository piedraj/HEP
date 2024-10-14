# cuts

cuts = {}


_tmp = [
    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'Lepton_pt[0] > 25.',
    'Lepton_pt[1] > 20.',
    '(nLepton >= 2 && Alt(Lepton_pt,2, 0) < 10.)',
    'mll > 12',
    'mpmet > 20.',
    'PuppiMET_pt > 20.',
     ]

preselections = ' && '.join(_tmp)

cuts['dhww2l2v_13TeV_sr'] = {
    'expr': 'ptll>30 && mth > 50 && drll < 2.5',
    'categories' : {
        '0j' : 'zeroJet',
        '1bj' : 'bReq',
        #'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0',
        #'2j' : 'Sum(CleanJet_pt>30.0)==2',
    }
}





