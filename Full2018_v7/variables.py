# variables

# 0 = not fold (default)
# 1 = fold underflow bin
# 2 = fold overflow bin
# 3 = fold underflow and overflow bins

variables = {}

variables['events'] = {
    'name'  : '1',
    'range' : (1, 0, 2),
    'xaxis' : 'events',
    'fold'  : 3
}

variables['mll'] = {
    'name'  : 'mll',
    'range' : (100, 0, 200),
    'xaxis' : 'm_{ll} [GeV]',
    'fold'  : 3
}

variables['drll'] = {
    'name'  : 'drll',
    'range' : (30, 0, 3.15),
    'xaxis' : '#DeltaR_{ll}',
    'fold'  : 3
}

variables['mth'] = {
    'name'  : 'mth',
    'range' : (30, 50, 400),
    'xaxis' : 'm_{T}^{H} [GeV]',
    'fold'  : 3
}

variables['mtw2'] = {
    'name'  : 'mtw2',
    'range' : (30, 20, 300),
    'xaxis' : 'm_{T}^{W2} [GeV]',
    'fold'  : 3
}

variables['ptll'] = {
    'name'  : 'ptll',     
    'range' : (30, 30, 300),   
    'xaxis' : 'p_{T}^{ll} [GeV]',
    'fold'  : 3
}

variables['pt1'] = {
    'name'  : 'Lepton_pt[0]',     
    'range' : (30, 20, 250),   
    'xaxis' : 'p_{T} 1st lepton [GeV]',
    'fold'  : 3
}

variables['pt2'] = {
    'name'  : 'Lepton_pt[1]',     
    'range' : (30, 10, 150),   
    'xaxis' : 'p_{T} 2nd lepton [GeV]',
    'fold'  : 3 
}

variables['eta1'] = {
    'name'  : 'Lepton_eta[0]',     
    'range' : (30, -3, 3),   
    'xaxis' : '#eta 1st lepton',
    'fold'  : 3                         
}

variables['eta2'] = {
    'name'  : 'Lepton_eta[1]',     
    'range' : (30, -3, 3),   
    'xaxis' : '#eta 2nd lepton',
    'fold'  : 3                         
}

variables['puppimet'] = {
    'name'  : 'PuppiMET_pt',
    'range' : (30, 20, 200),
    'xaxis' : 'PUPPI MET [GeV]',
    'fold'  : 3
}

variables['mpmet'] = {
    'name'  : 'mpmet',
    'range' : (30, 20, 200),
    'xaxis' : 'mpmet [GeV]',
    'fold'  : 3
}

variables['dphill'] = {
    'name'  : 'abs(dphill)',     
    'range' : (30, 0, 3.15),   
    'xaxis' : '#Delta#phi_{ll}',
    'fold'  : 3
}

variables['dphillmet'] = {
    'name'  : 'dphillmet',     
    'range' : (30, 0, 3.15),   
    'xaxis' : '#Delta#phi_{ll, MET}',
    'fold'  : 3
}

variables['mjj'] = {
    'name'  : 'mjj*(CleanJet_pt[1]>30)',
    'range' : (20, 0, 1000),
    'xaxis' : 'm_{jj} [GeV]',
    'fold'  : 3
}
