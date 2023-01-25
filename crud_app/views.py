from django.shortcuts import render, redirect
from .models import Students


def read(request):
    students = Students.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)


def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect(read)


def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    students = Students.objects.all()
    students.create(name=name, age=age)
    return redirect(read)


def edit(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'update.html', {'student': student})


def update(request, id):
    name = request.POST.get('name')
    student = Students.objects.get(id=id)
    student.name(name)
    student.save()
    return redirect(read)
