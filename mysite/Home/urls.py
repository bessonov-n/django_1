from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('profile/', views.profile.as_view(), name='profile_url'),
    path('profile/file_input',views.file_input),
    path('profdoc', views.profdoc, name='profdoc_url'),

    path('Mcourses/', views.Mcourses, name='Mcourses_url'),
    path('Mcourses/3-02', views.Mc302.as_view(), name='Mc302_url'),
    path('Mcourses/fileM302',views.filem302),
    path('docMc302', views.docMc302, name='docMc302_url'),
    path('Mcourses/3-05', views.Mc305.as_view(), name='Mc305_url'),
    path('Mcourses/fileM305',views.filem305),
    path('docMc305', views.docMc305, name='docMc305_url'),
    path('Mcourses/4-02', views.Mc402.as_view(), name='Mc402_url'),
    path('Mcourses/fileM402',views.filem402),
    path('docMc402', views.docMc402, name='docMc402_url'),
    path('Mcourses/4-05', views.Mc405.as_view(), name='Mc405_url'),
    path('Mcourses/fileM405',views.filem405),
    path('docMc405', views.docMc405, name='docMc405_url'),

    path('Applications/', views.applications, name='applications_url'),
    path('Applications/02', views.A02.as_view(), name='A02_url'),
    path('Applications/file02',views.fileA02),
    path('doc02', views.docA02, name='docA02_url'),

    path('Applications/302', views.Ap302.as_view(), name='A302_url'),
    path('Applications/file302',views.fileA302),
    path('doc302', views.docA302, name='docA302_url'),

    path('Applications/305', views.Ap305.as_view(), name='A305_url'),
    path('Applications/file305',views.fileA305),
    path('doc305', views.docA305, name='docA305_url'),

    path('Applications/402', views.Ap402.as_view(), name='A402_url'),
    path('Applications/file402',views.fileA402),
    path('doc402', views.docA402, name='docA402_url'),

    path('Applications/405', views.Ap405.as_view(), name='A405_url'),
    path('Applications/file405',views.fileA405),
    path('doc405', views.docA405, name='docA405_url'),
]