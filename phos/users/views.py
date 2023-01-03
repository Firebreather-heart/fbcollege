from django.shortcuts import render, redirect 
from users.forms import CustomUserCreationForm
from courses.models import Course
from courses.forms import CourseEnrollForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
from django.contrib.auth import login
def register(request):
    if request.POST:
        userform = CustomUserCreationForm(request.POST)
        if userform.is_valid():
            new_user = userform.save(commit=False)
            cd = userform.cleaned_data
            new_user.set_password(
                cd['password']
            )
            try:
                new_user.save()
            except Exception as e:
                print(e)
        return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'user_form':user_form})

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None 
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form) 
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args = [self.course.id])

class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

class StudentCourseDetailView(DetailView):
    model = Course 
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in = [self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(
                id = self.kwargs['module_id']
            )
        else:
            context['module'] = course.modules.all()[0]
        return context