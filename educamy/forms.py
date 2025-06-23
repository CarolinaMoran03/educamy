from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm
from .models import SchoolSubject
from django.core.exceptions import ValidationError
from datetime import date
  # Ya lo tienes arriba, perfecto



class CreateUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

        self.fields['username'].widget.attrs.update({
    'class': 'w-full p-2 border-2 border-black rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500'
})
        self.fields['password1'].widget.attrs.update({
    'class': 'w-full p-2 border-2 border-black rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500'
})
        
        self.fields['password2'].widget.attrs.update({
    'class': 'w-full p-2 border-2 border-black rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500'
})
        

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso. Elige otro.")
        return username

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': _('Solo se aceptan letras o estos caracteres @/./+/-/_ '),
            'password2': _('Vuelve a ingresar la misma contraseña'),
            'password1': _('Tu contraseña no debe ser similar a tu usuario.\n'
                           'Debe contener al menos 8 caracteres\n'
                           'No uses contraseñas habituales\n'
                           'No debe ser solo numeros'),
        }




DAYS_CHOICES = [
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miércoles', 'Miércoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes')
]

LEVELS = [
    ('Primero', 'Primero'),
    ('Segundo', 'Segundo'),
    ('Tercero', 'Tercero'),
    ('Cuarto', 'Cuarto'),
    ('Quinto', 'Quinto'),
    ('Sexto', 'Sexto'),
    ('Septimo', 'Septimo'),
]

BASE_INPUT_CLASS = 'appearance-none w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500 transition'


ITINERARY_CHOICES = [
        ('micro', 'Plan Microcurricular'),
        ('annual', 'Plan Anual'),
    ]

class itinerarieForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de inicio")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de fin")
    itinerarieType = forms.ChoiceField(
        choices=ITINERARY_CHOICES,
        label="Tipo de itinerario",
        widget=forms.Select(attrs={'class': 'absolute'}),
    )
    units_number   = forms.IntegerField(
        label="Número de unidades",
        min_value=1,
        error_messages={'min_value': "Debes generar al menos una unidad."}
    )
    level = forms.ChoiceField(
        choices=LEVELS,
        label="Nivel",
        widget=forms.Select(attrs={'class': 'absolute'}),
    )
    school_subject = forms.ModelChoiceField(
        queryset=SchoolSubject.objects.all(),
        label="Materia",
        widget=forms.Select(attrs={'class': 'absolute'}),
        
    )
    teacher_name = forms.CharField(
        max_length=200,
        label="Nombre del docente",
        required=False,
        widget=forms.TextInput(attrs={'class': BASE_INPUT_CLASS})
    )
    college_name = forms.CharField(
        max_length=200,
        label="Nombre del colegio",
        required=False,
        widget=forms.TextInput(attrs={'class': BASE_INPUT_CLASS})
    )

    parallel = forms.CharField(
        max_length=200,
        label="Paralelo",
        required=False,
        widget=forms.TextInput(attrs={'class': BASE_INPUT_CLASS})
    )
    



    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        if start_date < date.today():
            raise ValidationError("La fecha de inicio no puede ser anterior a hoy.")
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        if end_date < date.today():
            raise ValidationError("La fecha de fin no puede ser anterior a hoy.")
        return end_date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        teacher_name = cleaned_data.get("teacher_name")
        college_name = cleaned_data.get("college_name")
        parallel = cleaned_data.get("parallel")

        if not teacher_name or not teacher_name.strip():
            self.add_error('teacher_name', "El nombre del docente es obligatorio.")

        if not college_name or not college_name.strip():
            self.add_error('college_name', "El nombre del colegio es obligatorio.")
        
        if not parallel or not parallel.strip():
            self.add_error('parallel', "El paralelo es obligatorio.")


        

        if start_date and end_date and end_date < start_date:
            raise ValidationError("La fecha de fin debe ser igual o posterior a la fecha de inicio.")




class AddSchoolSubjectForm(forms.ModelForm):
    class Meta:
        model = SchoolSubject
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': _('Nombre de la materia'),
            'description': _('Descripción de la materia'),
        }
        