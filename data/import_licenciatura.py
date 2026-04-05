import json

from portfolio.models import Licenciatura, Docente, UnidadeCurricular

with open('files/ULHT260-PT.json', encoding='utf-8') as f:
    data = json.load(f)

course = data['courseDetail']

a
licenciatura, _ = Licenciatura.objects.get_or_create(
    nome=course['courseName'],
    defaults={
        'duracao': 3,
        'objetivos': course.get('careerOportunities', ''),
    }
)

for teacher in data.get('teachers', []):
    docente, _ = Docente.objects.get_or_create(
        nome=teacher['fullName'],
        defaults={
            'email': teacher.get('email', ''),
        }
    )
    


for uc_data in data.get('courseFlatPlan', []):
    uc, _ = UnidadeCurricular.objects.get_or_create(
        nome=uc_data['curricularUnitName'],
        defaults={
            'ano': uc_data.get('curricularYear', 1),
            'semestre': int(uc_data.get('semesterCode', 'S1').replace('S', '')),
            'ects': uc_data.get('ects', 0),
        }
    )
    uc.licenciaturas.add(licenciatura)
    

print('\nImportação concluída!')