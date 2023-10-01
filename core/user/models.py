from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=234)
    age = models.IntegerField(max_length=1000)

    #1.  Student.objects.filter(age=2) isase data ko filter kr skte hai
    #2.  Student.objects.exclude(age=2) exclude ka use jo hm age = 2 diy hai use chhodkr sb value ko print kr de
    #3. Student.objects.exclude(age__lte=2) ye 2 ko chhodkr sbka value print kr dega
    #4. Student.objects.exclude(age__gte=2) ye 2 se chhoti no. ko ayega 
    #5. Student.objects.all() isase se sara data aa jata hai
    #6. for p in Student.objects.all().order_by('name'):  ye order me print krat hai
    #7. for p in Student.objects.all().order_by('-age'):  ye deccending order me krega
    #8. Student.objects.aggregate(Count('age')) ye aggregate function me average, count, sum , count etc pe kam krta hai
    #9. Student.objects.aggregate(Sum('age')) ye aggregate function me average, count, sum , count etc pe kam krta hai 
        # aggregate ka use jb HR , management project bnta hai wha use hota hai

    #10 Student.objects.filter(name_icontains='raj').aggregate(Sum)('age')
    #11. from django.db.models import Q
    # obje = Student.objects.filter(Q(age=1) | Q(age=2))  
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # 12 >>> obje = Student(name = "Simran",age =23)
    # obje.save()
    # obje = Student(name = "Maya",age =13)   
    # obje.save()
    # a= Student.objects.get(id = 7)
    # print(a.name)

    #  Change name and anything this topic

    #13.  a.name = "Rajesh"
    # a.save()
    # a = Student.objects.get(id = 7)
    # a = Student: Student object (7)>
    # print(a.name)
    # Rajesh