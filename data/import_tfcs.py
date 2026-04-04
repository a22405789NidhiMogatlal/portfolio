import json

from portfolio.models import Tfc,Licenciatura,Tecnologia

with open('data/tfcs_2024_2025.json') as f:
    tfcs=json.load(f)

for item in tfcs:

    
