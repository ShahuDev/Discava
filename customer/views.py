from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomerCreationForm
from .models import Customer


# Create your views here.


class CustomerSignUpView(View):
    def get(self, request):
        form = CustomerCreationForm()
        return render(request, 'customers/signup.html', {'form': form})

    def post(self, request):
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer(user=user, phone_number=form.cleaned_data['phone_number'],
                                address=form.cleaned_data['address'])
            customer.save()
            return redirect('login')
        return render(request, 'customers/signup.html', {'form': form})
