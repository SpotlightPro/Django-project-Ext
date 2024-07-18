from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MemberForm
from .forms import AuditsForm
from .models import Member
from .models import Audit



# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def qmo_member(request):
    all_members = Member.objects.all
    return render(request, 'qmo_member.html', {'all': all_members})


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
            return render(request, 'join.html', {'fname': fname,
                                                 'lname': lname,
                                                 'email': email,
                                                 'qmo_level': qmo_level,
                                                 'passwd': passwd,
                                                 'passwd2': passwd2,
                                                 })
        messages.success(request, 'Your form has been Submitted Successfully!')
        return redirect('home')
    else:
        return render(request, 'join.html', {})


def area(request):
    return render(request, 'area.html', {})


def audits(request):
    all_audits = Audit.objects.all
    return render(request, 'audits.html', {'all_audits':all_audits})
