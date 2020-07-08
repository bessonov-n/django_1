from django import forms
from .models import ikntprofils


class profForm(forms.Form):
	FIO = forms.CharField(
		max_length = 200, 
		label="Полные ФИО в родительном падеже",
		widget=forms.TextInput(attrs={'size': '40'})
	)
	FIO2 = forms.CharField(
		max_length = 200,	
		label = "Сокращенные Фамилия И.О. в именительном падеже"
	)
	group = forms.CharField(
		max_length = 200,	
		label = "Введите номер группы"
	)
	sred = forms.CharField(
		max_length = 200,	
		label = "Введите средний балл"
	)
	profile1 = forms.ModelChoiceField(
	 	queryset=ikntprofils.objects.all(),
	 	label="Выберите желаемый профиль"
	)
	profile1.empty_label = None






class McForm(forms.Form):
	FIO = forms.CharField(
		max_length = 200, 
		label="Полные ФИО в родительном падеже",
		widget=forms.TextInput(attrs={'size': '40'})
	)
	FIO2 = forms.CharField(
		max_length = 200,	
		label = "Сокращенные Фамилия И.О. в именительном падеже"
	)
	group = forms.CharField(
		max_length = 200,	
		label = "Введите номер группы"
	)