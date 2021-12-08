from django.shortcuts import render, HttpResponseRedirect
from .forms import student_form
from .models import Student

# Create your views here.


def add_remove(request):
    data = Student.objects.all()
    if request.method == "POST":
        fm = student_form(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            fn = fm.cleaned_data['f_name']
            cl = fm.cleaned_data['sclass']
            st = Student(name=nm, f_name=fn, sclass=cl)
            st.save()
            return HttpResponseRedirect("/")
    else:
        fm = student_form()
    return render(request, "addremove.html", {'form':fm, 'data':data})

def delete(request, id):
    if request.method=="POST":
        ky = Student.objects.get(pk=id)
        ky.delete()
        return HttpResponseRedirect("/")


def update_data(request, st):

    if request.method == "POST":
        stu = Student.objects.get(pk=st)
        fm = student_form(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")

    else:
        print("false")
        stu = Student.objects.get(pk=st)
        fm = student_form(instance=stu)


    return render(request, "update.html", {'form':fm})


