#
from app1.models import Person
##### to get all person record
# objs = Person.objects.all()
##### if you want to print in list
# print(list(objs))       

##### to get single person record 
# for Person in objs:
#     print(Person.__dict__)

##### to get first person record
# first_record = Person.objects.first()

# print(first_record) 

##### to get record by id
# obj = Person.objects.get(id=1)
# print(obj)
# O/p:
# Anuj--Amravati

##### if you dont get your record in database
# obj = Person.objects.get(id=4)
# print(obj)
# O/p: show error
# app1.models.Person.DoesNotExist: Person matching query does not exist.

# then aplly exeption handaling

# try:
#     obj = Person.objects.get(id=4)
#     print(obj)
# except Person.DoesNotExist:
#     print("record does not exist")

# O/p:
# record does not exist

##### to get multiple record by id passing filter on field

# objs = Person.objects.filter(age=25)
# print(objs)

# O/p:
# <QuerySet [<Person: Ruchu--Mumbai>, <Person: Parth--Nagpur>]>

##### to know which quaery fetch then
# objs = Person.objects.filter(age=25)
# print(objs.query)

#####to acess multiple field
# objs = Person.objects.filter(age=25, address="Nagpur")  # ,--- and
# print(objs)

##### to modify existing data
# p1 = Person.objects.get(id=1)           # need to fetch record from database
# print(p1.__dict__)
##### get mobile no 
# print(p1.mobile_num)
#####modify that mobile no
# p1.mobile_num = 1230334498
# print(p1.__dict__)                      # here modify mobile no
# p1.save()                               # to save chnges in database


##### to delte data from database
# p1 = Person.objects.get(id=3)
# p1.delete()

##### Creation of bojects to save in 3 ways:
# 1st way:
# p1 = Person(name="ABC",age=28,mobile_num=1230334498,address="Amravat", email= "anujronghe@gmail.com")
# p1.save()

# 2nd way:
# Person.objects.create(name="PQR",age=28,mobile_num=1230334498,address="PUNE", email= "xyz@gmail.com")

##to get all directories:
# print(dir(Person.objects))
# ['__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter', '_update', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 
# 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']


###### BULK CREATION ########
# p1 = Person(name="Chhaya",age=38,mobile_num=1230344498,address="PUNE", email= "chhaya@gmail.com")
# p2 = Person(name="Rajesh",age=48,mobile_num=1230354498,address="Vardha", email= "rajesh@gmail.com")
# p3 = Person(name="Anushree",age=18,mobile_num=1220334498,address="Sangali", email= "anush@gmail.com")
# p4 = Person(name="Ira",age=29,mobile_num=1230034498,address="Latur", email= "ira@gmail.com")

# Person.objects.bulk_create([p1,p2,p3,p4])                   # need to stored in list

##### to get count
# print(Person.objects.count())                                 # 11