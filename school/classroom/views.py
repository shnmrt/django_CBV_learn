from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from classroom.models import Teacher
from classroom.forms import ContactForm
# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

# model based CBV
class TeacherCrateView(CreateView):
    model = Teacher
    #model_form.html
    #.save()
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    # success URL?
    #success_url =  '/classroom/thank_you/'
    success_url =  reverse_lazy('classroom:thank_you')
    
    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        # ContractForm(request.POST)
        return super().form_valid(form)