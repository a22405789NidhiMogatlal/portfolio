import json

from portfolio.models import Tfc,Licenciatura,Tecnologia,Docente

Tfc.objects.all().delete()
Licenciatura.objects.all().delete()
Tecnologia.objects.all().delete()
Docente.objects.all().delete() 

with open('data/tfcs_2024_2025.json') as f:
    tfcs=json.load(f)

for item in tfcs:

    titulo=item['titulo']
    
    alunos=item['alunos']
    
    orientadores=item['orientadores']
    

    linha_lic=item['licenciatura']
    partes=linha_lic.split('.')
    ano_lic=partes[-1].strip() 

    licenciaturas=[p.strip() for p in partes[:-1] if p.strip() ]

    pdf=item['pdf']
    email=item['email']
    img=item['imagem']
    areas=item['areas']

    tecnologias=item['tecnologias']
    rate=item['rating']

    lics = []
    for nome_lic in licenciaturas:
        lic,_ = Licenciatura.objects.get_or_create(nome=nome_lic) 
        lics.append(lic)
    

    docs = []
    for nome_orientador in orientadores:
        doc, _ = Docente.objects.get_or_create(nome=nome_orientador)
        docs.append(doc)

    tecs = []
    for nome_tec in tecnologias:
        tec,_= Tecnologia.objects.get_or_create(nome=nome_tec)
        tecs.append(tec)
    tfc, created = Tfc.objects.get_or_create(
        titulo=titulo,
        defaults={
            'alunos': ', '.join(alunos),
            'ano': int(ano_lic) if ano_lic.isdigit() else 2025,
            'url_relatorio':pdf,
            'email': email,
            'areas': ', '.join(areas),
            'classificacao': rate,
        }
    )
       
        #ASSCOIAR AS LICENCIATURAS E TECNOLOGIAS AO TFC
    for lic in lics:
        tfc.licenciatura.add(lic)
    for tec in tecs:
        tfc.tecnologia.add(tec)
    for doc in docs:
        tfc.orientadores.add(doc)
    
  

print('\nImportação concluída!')





    
