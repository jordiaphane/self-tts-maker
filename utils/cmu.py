import os, sys, re
from collections import defaultdict
import pronouncing, cmudict



84
cmu_symbols = ['AA', 'AA0', 'AA1', 'AA2', 'AE', 'AE0', 'AE1', 'AE2', 'AH', 'AH0', 'AH1', 'AH2', 'AO', 'AO0', 'AO1', 'AO2', 'AW', 'AW0', 'AW1', 'AW2', 'AY', 'AY0', 'AY1', 'AY2', 'B', 'CH', 'D', 'DH', 'EH', 'EH0', 'EH1', 'EH2', 'ER', 'ER0', 'ER1', 'ER2', 'EY', 'EY0', 'EY1', 'EY2', 'F', 'G', 'HH', 'IH', 'IH0', 'IH1', 'IH2', 'IY', 'IY0', 'IY1', 'IY2', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OW0', 'OW1', 'OW2', 'OY', 'OY0', 'OY1', 'OY2', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH', 'UH0', 'UH1', 'UH2', 'UW', 'UW0', 'UW1', 'UW2', 'V', 'W', 'Y', 'Z', 'ZH']


cmudictionary = cmudict.dict()
def primarycmu(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k][0] = primarycmu(v)
        try:
            secondary_cmu_dict = {}
            if len(v) > 1:
                secondary_cmu_dict.update(d[k][0],v[1:])
            
        except:
            pass
        return dict(d), secondary_cmu_dict
primary_cmu, secondary_cmu = primarycmu(cmudictionary)

#dialect questions
dialect_categories = ["vowel", "semivowel", "stop", "affricate", "aspirate", "liquid", "nasal", "fricative"]

phone_vars = {}
phone_vars["vowel"] = ["AA", "AE", "AH", "AO", "AW", "AY","EH", "ER","EY","IH", "IY", "OW", "OY", "UW", "UH"]
phone_vars["stop"] = ['B','D','G', 'K','P','T']
phone_vars["fricative"]=['DH','F','S','SH','TH', 'V', 'Z', 'ZH'] 
phone_vars["liquid"]['L', 'R']
phone_vars["nasal"]=['M','N','NG']
phone_vars["semivowel"]=['W', 'Y']
phone_vars['aspirate'] = 'HH'
phone_vars["affricate"] = ['CH','JH'] 


