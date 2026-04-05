from portfolio.models import Tfc, Licenciatura, Tecnologia

Tfc.objects.all().delete()
Licenciatura.objects.all().delete()
Tecnologia.objects.all().delete()

print('Dados eliminados!')