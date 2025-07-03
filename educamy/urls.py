from django.urls import path
from .views import loginView, registerView, userProfile, changePassword, DashboardView, generateContent, logoutApp, ItinerariesView, SchoolSubjectsView, SchoolSubjectEditView, SchoolSubjectDeleteView, MicroPlanDeleteView, AnnualPlanDeleteView, AnnualItinerarieDetailView, MicroItinerarieDetailView, delete_quiz

app_name = 'educamy'

urlpatterns = [
    path('', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutApp, name='logout'),
    path('profile/<int:pk>/', userProfile, name='profile'),
    path('profile/password/', changePassword, name='change_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('school_subjects/', SchoolSubjectsView.as_view(), name='school_subjects'),
    path('school_subjects/edit/<int:pk>/', SchoolSubjectEditView.as_view(), name='edit_school_subject'),
    path('school_subjects/delete/<int:pk>/', SchoolSubjectDeleteView.as_view(), name='delete_school_subject'),
    path('itineraries/', ItinerariesView.as_view(), name='itineraries'),
    path('itineraries/generate_content/', generateContent, name='generate_content'),
    path('itineraries/annual/<int:pk>/delete/', AnnualPlanDeleteView.as_view(), name='delete_annual_plan'),
    path('itineraries/annual/<int:pk>/detail', AnnualItinerarieDetailView.as_view(), name='detail_annual_plan'),
    path('itineraries/micro/<int:pk>/detail', MicroItinerarieDetailView.as_view(), name='detail_micro_plan'),
    path('itineraries/micro/<int:pk>/delete/', MicroPlanDeleteView.as_view(), name='delete_micro_plan'),


    path('quiz/delete/<int:quiz_id>/', delete_quiz, name='delete_quiz'),

    

    


]
