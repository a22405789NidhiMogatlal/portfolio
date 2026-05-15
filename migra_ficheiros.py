import os
from django.core.files import File
from portfolio.models import Docente, Tecnologia, Tfc, Projeto, Formacao, MakingOf, Evento

MEDIA_ROOT = '/workspaces/portfolio/media'

print("=== Migrando Docentes ===")
for obj in Docente.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migrando Tecnologias ===")
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join(MEDIA_ROOT, obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migrando TFCs ===")
for obj in Tfc.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migrando Projetos ===")
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migrando Formações ===")
for obj in Formacao.objects.all():
    if obj.certificado and obj.certificado.name:
        local_path = os.path.join(MEDIA_ROOT, obj.certificado.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.certificado.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migrando MakingOf ===")
for obj in MakingOf.objects.all():
    if obj.foto and obj.foto.name:
        local_path = os.path.join(MEDIA_ROOT, obj.foto.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migrando Eventos ===")
for obj in Evento.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")

print("=== Migração concluída ===")
