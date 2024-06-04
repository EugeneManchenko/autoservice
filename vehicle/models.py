from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # Пользователь, связанный с этой учетной записью
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Фотография профиля
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    # Адрес
    email = models.EmailField(max_length=254, null=False)
    # Мобильный телефон
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Mechanic(models.Model):
    # Пользователь, связанный с этой учетной записью
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Фотография профиля
    profile_pic = models.ImageField(upload_to='profile_pic/MechanicProfilePic/', default='default_profile_pic.jpg')
    # Адрес
    email = models.EmailField(max_length=254, null=False)
    # Телефон
    mobile = models.CharField(max_length=20, null=False)
    # Навыки
    skill = models.CharField(max_length=500, null=True)
    # Зарплата
    salary = models.PositiveIntegerField(null=True)
    # Статус (работает или нет)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    cat = (
        ('Легковой более 2т.', 'Легковой более 2т.'),
        ('Грузовой до 3.5т', 'Грузовой до 3.5т'),
        ('Грузовой выше 3.5т', 'Грузовой выше 3.5т'),
        ('Легковой до 2т', 'Легковой до 2т')
    )
    category = models.CharField(max_length=50, choices=cat)
    mileage = models.PositiveIntegerField(default=0)
    vehicle_no = models.CharField(max_length=17, null=False)
    vehicle_name = models.CharField(max_length=40, null=False)
    vehicle_model = models.CharField(max_length=40, null=False)
    vehicle_brand = models.CharField(max_length=40, null=False)
    year = models.PositiveIntegerField(default=0)
    problem_description = models.CharField(max_length=500, null=False)
    date = models.DateField(auto_now=True)
    cost = models.PositiveIntegerField(null=True)

    # Связь с заказчиком
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    # Связь с механиком
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)

    stat = (
        ('Ожидание', 'Ожидание'),
        ('Утверждено', 'Утверждено'),
        ('В ремонте', 'В ремонте'),
        ('Ремонт завершен', 'Ремонт завершен'),
        ('Выпущено', 'Выпущено')
    )
    status = models.CharField(max_length=50, choices=stat, default='Ожидание', null=True)

    def __str__(self):
        return self.problem_description


class Attendance(models.Model):
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    present_status = models.CharField(max_length=10)


class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)
