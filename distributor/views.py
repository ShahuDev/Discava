from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import DistributorCreationForm
from .models import Distributor


class DistributorSignUpView(View):
    def get(self, request):
        form = DistributorCreationForm()
        return render(request, 'distributors/signup.html', {'form': form})

    def post(self, request):
        form = DistributorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            distributor = Distributor(user=user, phone_number=form.cleaned_data['phone_number'],
                                      company_name=form.cleaned_data['company_name'])
            distributor.save()
            return redirect('login')
        return render(request, 'distributors/signup.html', {'form': form})


from django.shortcuts import render
