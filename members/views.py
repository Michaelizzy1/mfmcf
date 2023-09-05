from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member
from django.contrib import messages

# Create your views here.


def index(request):
    form = MemberForm()
    if request.method == "POST":
        form = MemberForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            messages.success(request, 'Your record has been successfully saved!!!')
            return redirect('index')
    context = {
        'form':form,
    }
    return render(request, 'members/index.html', context)


def members(request):
    members = Member.objects.all()
    context = {
        'members':members,
    }
    return render(request, 'members/all-members.html', context)


def profile(request, id):
    profile = Member.objects.get(id=id)
    context = {
        'profile':profile,
    }
    return render(request, 'members/profile.html', context)