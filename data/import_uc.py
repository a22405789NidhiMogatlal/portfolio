import json
import os

from portfolio.models import UnidadeCurricular, Docente

files_dir = 'files'

for filename in os.listdir(files_dir):
    if not filename.endswith('-PT.json') or filename.startswith('ULHT260-PT'):
        continue

    filepath = os.path.join(files_dir, filename)
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)

    nome_uc = data.get('curricularUnitName', '')
    if not nome_uc:
        continue

   
    try:
        uc = UnidadeCurricular.objects.get(nome=nome_uc)
        uc.apresentacao = data.get('presentation', '')
        uc.programa = data.get('programme', '')
        uc.save()
        
    except UnidadeCurricular.DoesNotExist:
        print(f'- Não encontrada: {nome_uc}')

print('\nAtualização concluída!')