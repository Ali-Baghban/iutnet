import sys, os, django
sys.path.append("iutnet") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iutnet.settings")
django.setup()

from demoapp import models
#while True:
#    name = input('Enter a name => ')
#    t = models.test(name=name)
#    t.save()
#    print('Well done !',"\n")
#    records = models.test.objects.all()
#    for data in records:
#        print(data)

objs = models.Request.objects.all()
for obj in objs:
    print(obj.id)

print(sys.path)
