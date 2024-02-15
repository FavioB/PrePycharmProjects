from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return HttpResponse("Hello, Improved world! \n You actually did it")


class EditCustomerView(View):
    # permission_required = ('OrderMgmtApp.change_customer')
    def get(self, request, *args, **kwargs):
        # *args vraible list of parameters **kwargs extracts ID from
        id = kwargs.get("id")
        id = 0 if id is None else id
        print( " id = " + str (kwargs.get("id")))

        if (id > 0 ) :
            # This is a Edit
            customer = Customer.objects.get(id = kwargs.get("id"))
        else :
            customer = Customer()

        # form = CustomerForm(initial={"firstName":customer.first_name, "lastName":customer.last_name,
        # "customer_since":customer.created_date, "preferred_customer":customer.special_customer})
        form = CustomerModelForm(instance = customer)
        return render(request, 'create_customer.html', {'form': form})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print ( " id = " + str (kwargs.get("id")))

        if (id > 0) :
            #this is an edit transaction
            customer = Customer.objects.get(id=kwargs.get("id"))
        else :
            #this is a new transaction
            customer = Customer()

        form = CustomerModelForm(request.POST, instance=customer);
        if form.is_valid():
            # cd = form.cleaned_data
            # customer.first_name = cd["firstName"]
            # customer.last_name = cd["lastName"]
            # customer.special_customer = cd["preferred_customer"]
            # customer.created_date = cd["customer_since"]
            customer.save()
            return HttpResponseRedirect(reverse('index'))
        else:
           return render(request, 'create_customer.html', {'form': form})

    def createContactFromModelForm(request, fk):

        if request.POST:
            form = ContactModelForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                customer = Customer.objects.get(id=fk)
                contact.customer = customer
                contact.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'create_contact.html', {'form': form})
        else:
            form = ContactModelForm()
            return render(request, 'create_contact.html', {'form': form})


class EditContactView(View):
    def validate(self):
        #implement contact validation code
        print("Validate method called")

    def get(self, request, *args, **kwargs):
        print( " id = " + str (kwargs.get("id")))

        contact = Contact.objects.get(id = kwargs.get("id"))

        form = ContactModelForm(instance = contact)
        return render(request, 'create_contact.html', {'form': form})

    def post(self, request, *args, **kwargs):
        print ( " id = " + str (kwargs.get("id")))

        contact = Contact.objects.get(id=kwargs.get("id"))

        form = ContactModelForm(request.POST, instance = contact)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'create_contact.html', {'form': form})