from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import ikntprofils, Mc3025, Mc3026, Mc4, A021, A022, A024, A302, A305, A402, A405
from .forms import profForm, McForm
from django.shortcuts import redirect
from django.views import View
import main_choose, elect1d, elect2d02, elect2d05, elect3d02, elect3d05, online3d02, online3d05, online4d02, online4d05


# Create your views here.
def index(request):
	return render(request, 'Home/index.html')


class profile(View):
	def get(self, request):
		form = profForm()
		profch = ikntprofils.objects.all()
		return render(request, 'Home/profiles.html', context={'form': form,
															  'profch': profch})

def Mcourses(request):
	return render(request, 'Home/Mcourses.html')

def file_input(request):
	IFIO=request.POST['FIO']
	groupp=request.POST['group']
	ball=request.POST['sred']
	RFIO=request.POST['FIO2']
	prof=request.POST['profile1']
	main_choose.profils2(RFIO, groupp, ball, IFIO, prof)
	return render(request, 'Home/GenProfileFile.html')
	
def profdoc(request):
	return FileResponse(open('main_choose.pdf', 'rb'), content_type='application/pdf')

class Mc302(View):
	def get(self, request):
		form = McForm()
		sem5 = Mc3025.objects.all()
		sem6 = Mc3026.objects.all()
		return render(request, 'Home/302.html', context={'form': form,
														 'sem5': sem5,
														 'sem6': sem6})

def filem302(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['seme5']
	d=request.POST['seme6']
	online3d02.profils2(RFIO, IFIO, group, r, d)
	return render(request, 'Home/Mc302.html')

def docMc302(request):
	return FileResponse(open('online3d02.pdf', 'rb'), content_type='application/pdf')

class Mc305(View):
	def get(self, request):
		form = McForm()
		sem5 = Mc3025.objects.all()
		sem6 = Mc3026.objects.all()
		return render(request, 'Home/305.html', context={'form': form,
														 'sem5': sem5,
														 'sem6': sem6})

def filem305(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['seme5']
	d=request.POST['seme6']
	online3d05.profils2(RFIO, IFIO, group, r, d)
	return render(request, 'Home/Mc305.html')

def docMc305(request):
	return FileResponse(open('online3d05.pdf', 'rb'), content_type='application/pdf')

class Mc402(View):
	def get(self, request):
		form = profForm()
		sem7 = Mc4.objects.all()
		return render(request, 'Home/402.html', context={'form': form,
														 'sem7': sem7})

def filem402(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['sem7']
	online4d02.profils2(RFIO, IFIO, group, r)
	return render(request, 'Home/Mc402.html')

def docMc402(request):
	return FileResponse(open('online4d02.pdf', 'rb'), content_type='application/pdf')

class Mc405(View):
	def get(self, request):
		form = profForm()
		sem7 = Mc4.objects.all()
		return render(request, 'Home/405.html', context={'form': form,
														 'sem7': sem7})

def filem405(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['sem7']
	online4d05.profils2(RFIO, IFIO, group, r)
	return render(request, 'Home/Mc405.html')

def docMc405(request):
	return FileResponse(open('online4d05.pdf', 'rb'), content_type='application/pdf')


def applications(request):
	return render(request, 'Home/applications.html')

class A02(View):
	def get(self, request):
		form = McForm()
		sem1 = A021.objects.all()
		sem2 = A022.objects.all()
		sem3 = A024.objects.all()
		return render(request, 'Home/02.html', context={'form': form,
														 'sem1': sem1,
														 'sem2': sem2,
														 'sem3': sem3})

def fileA02(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['seme1']
	d=request.POST['seme2']
	k=request.POST['seme3']
	elect1d.profils2(RFIO, IFIO, group, r, d, k)
	return render(request, 'Home/A02.html')

def docA02(request):
	return FileResponse(open('elect1d.pdf', 'rb'), content_type='application/pdf')

class Ap302(View):
	def get(self, request):
		form = McForm()
		s1 = A302.objects.all()[:2]
		s2 = A302.objects.all()[2:4]
		s3 = A302.objects.all()[4:6]
		s4 = A302.objects.all()[6:8]
		return render(request, 'Home/3-02.html', context={'form': form,
														 's1': s1,
														 's2': s2,
														 's3': s3,
														 's4': s4})

def fileA302(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['sem51']
	d=request.POST['sem52']
	z=request.POST['sem61']
	x=request.POST['sem62']
	c=request.POST['sem63']
	elect2d02.profils2(RFIO, IFIO, group, r, d, z, x, c)
	return render(request, 'Home/A302.html')

def docA302(request):
	return FileResponse(open('elect2d02.pdf', 'rb'), content_type='application/pdf')



class Ap305(View):
	def get(self, request):
		form = McForm()
		s1 = A305.objects.all()[:2]
		s2 = A305.objects.all()[2:4]
		s3 = A305.objects.all()[4:6]
		s4 = A305.objects.all()[6:8]
		s5 = A305.objects.all()[8:10]
		return render(request, 'Home/3-05.html', context={'form': form,
														 's1': s1,
														 's2': s2,
														 's3': s3,
														 's4': s4,
														 's5': s5})

def fileA305(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['sem51']
	d=request.POST['sem52']
	z=request.POST['sem61']
	x=request.POST['sem62']
	c=request.POST['sem63']
	v=request.POST['sem64']
	elect2d05.profils2(RFIO, IFIO, group, r, d, z, x, c, v)
	return render(request, 'Home/A305.html')

def docA305(request):
	return FileResponse(open('elect2d05.pdf', 'rb'), content_type='application/pdf')



class Ap402(View):
	def get(self, request):
		form = McForm()
		s1 = A402.objects.all()[:2]
		s2 = A402.objects.all()[2:4]
		s3 = A402.objects.all()[4:6]
		return render(request, 'Home/4-02.html', context={'form': form,
														 's1': s1,
														 's2': s2,
														 's3': s3})

def fileA402(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['sem7']
	d=request.POST['sem78']
	z=request.POST['sem8']
	elect3d02.profils2(RFIO, IFIO, group, r, d, z)
	return render(request, 'Home/A402.html')

def docA402(request):
	return FileResponse(open('elect3d02.pdf', 'rb'), content_type='application/pdf')



class Ap405(View):
	def get(self, request):
		form = McForm()
		s1 = A405.objects.all()[:2]
		s2 = A405.objects.all()[2:4]
		return render(request, 'Home/4-05.html', context={'form': form,
														 's1': s1,
														 's2': s2})

def fileA405(request):
	IFIO=request.POST['FIO']
	group=request.POST['group']
	RFIO=request.POST['FIO2']
	r=request.POST['sem7']
	d=request.POST['sem78']
	elect3d05.profils2(RFIO, IFIO, group, r, d)
	return render(request, 'Home/A405.html')

def docA405(request):
	return FileResponse(open('elect3d05.pdf', 'rb'), content_type='application/pdf')