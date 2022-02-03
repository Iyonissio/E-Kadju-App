from email import message
from pyexpat import model
from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Sub_Categoria(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, default='')
    sub_categoria = models.ForeignKey(Sub_Categoria, on_delete=models.CASCADE, null=False, default='')
    image = models.ImageField(upload_to='ecommerce/pimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_products_by_id(ids):
        return Producto.objects.filter(id__in_=ids)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'existe':'Este email ja existe'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Nome'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Palavra Passe'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme Palavra Passe'

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'])
            #Melhorar esse eeroo
        return self.cleaned_data['email']


class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name