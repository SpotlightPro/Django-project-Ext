from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.
def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all': all_members})


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            qmo_level = request.POST['qmo_level']
            passwd = request.POST['passwd']
            passwd2 = request.POST['passwd2']
            messages.success(request, 'There was an error in your form. Please try again...')
            return render(request, 'join.html', {'fname':fname,
                                                 'lname':lname,
                                                 'email':email,
                                                 'qmo_level':qmo_level,
                                                 'passwd':passwd,
                                                 'passwd2':passwd2,
                                                 })
        messages.success(request, 'Your form has been Submitted Successfully!')
        return redirect('home')
    else:
        return render(request, 'join.html', {})
