from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Userprofile
from team.models import Team
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            Userprofile.objects.create(user=user)

            team = Team.objects.create(name='The team name', created_by=request.user)
            team.members.add(request.user)
            team.save()

            return redirect('/log-in/')
    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })


@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]

    return render(request, 'userprofile/myaccount.html', {
        'team': team,
    })
