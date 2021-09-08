from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
import smtplib
from django.core.mail import send_mail


# from currency.utils import generate_password as gen_pass


# def hello_world(request):
#     return HttpResponse('Hello World')

# class GeneratePasswordView(TemplateView):
#     template_name = 'generate_password.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         password_len = int(self.request.GET.get('password-len'))
#         context['password'] = gen_pass(password_len)
#
#         return context

# def generate_password(request):
#     password_len = int(request.GET.get('password-len'))
#     password = gen_pass(password_len)
#     return HttpResponse(password)
# ContactUs function
# def contact_us(request):
#     contacts = ContactUs.objects.all()
#     context = {
#         'contacts': contacts,
#     }
#     return render(request, 'contact_us.html', context=context)
class ContactUsView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    template_name = 'contactus_create.html'
    fields = (
        'firstname',
        'lastname',
        'mail',
        'body',
    )

    def form_valid(self, form):
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        body = form.cleaned_data['body']
        mail = form.cleaned_data['mail']
        full_email_body = f'''
                Email From: {mail}
                Body: {body}
                '''
        # subject =
        send_mail(
            # firstname,
            lastname,
            full_email_body,
            'currency.testmail@gmail.com',
            ['goldraccon@gmail.com'],
            fail_silently=False,
        )

        return super().form_valid(form)

        # fromaddr = 'currency.testmail@gmail.com'
        # toaddrs = 'goldraccon@gmail.com'
        # msg = 'Why,Oh why!'
        # username = 'currency.testmail@gmail.com'
        # password = 'Mijpyk-fisku2-qanmum'
        # server = smtplib.SMTP('smtp.gmail.com:587')
        # server.starttls()
        # server.login(username, password)
        # server.sendmail(fromaddr, toaddrs, msg)
        # server.quit()
        # return super().form_valid(form)
# class version CRUD Rate

class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    # model = Rate the same as next line
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateDetailsView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


# class version Source
class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceDetailsView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceCreateView(CreateView):
    # model = Source the same as next line
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'

# function version CRUD
# def rate_list(request):
#     rates = Rate.objects.all()
#     context = {
#         'rate_list': rates,
#     }
#     return render(request, 'rate_list.html', context=context)
#  Create
# def rate_create(request):
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_create.html', context=context)
# first version of Rate create
# def rate_create(request):
# result =[]
# for rate in rates:
#     result.append(
#         f'Id:{rate.id} Sale: {rate.sale} Buy: {rate.buy}</br>'
#     )
# return HttpResponse("Rate List")
# from datetime import datetime
#
#
# context ={
#     'message': f'Current time : {datetime.now()}'

# }

# Details View
# def rate_details(request, rate_id):
#     # /rate/details/?rate-d = .. VS rate/details/102/
#     # try:
#     #     rate = Rate.objects.get(id=rate_id)
#     # except Rate.DoesNotExist as exc:
#     #         raise Http404(exc)
#     rate = get_object_or_404(Rate, id=rate_id)
#     context = {
#         'object': rate,
# #     }
#     return render(request, 'rate_details.html', context=context)


# Rate update
# def rate_update(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm(instance=rate)
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_update.html', context=context)

# ### Delete
# def rate_delete(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == "POST":
#         rate.delete()
#         return HttpResponseRedirect('/rate/list/')
#     # if request method is 'GET'
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_delete.html', context=context)


# def get_source_list(request):
#     sources = Source.objects.all()
#     # result =[]
#     # for source in sources:
#     #     result.append(
#     #         f'Id:{source.id} URL: {source.source_url} Name: {source.name}</br>'
#     #     )
#     # return HttpResponse(str(result))
#     context = {
#         'source_list': sources,
#     }
#     return render(request, 'source_list.html', context=context)


# Source Create
# def source_create(request):
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source-list/')
#     elif request.method == 'GET':
#         form = SourceForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'source_create.html', context=context)


# Source Details
# def source_details(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#     context = {
#         'object': source,
#     }
#     return render(request, 'source_details.html', context=context)

# ### Source Update
# def source_update(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=source)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source-list/')
#     elif request.method == 'GET':
#         form = SourceForm(instance=source)
#     context = {
#         'form': form,
#     }
#     return render(request, 'source_create.html', context=context)

# Source delete
# def source_delete(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#
#     if request.method == "POST":
#         source.delete()
#         return HttpResponseRedirect('/source-list/')
#     # if request method is 'GET'
#     context = {
#         'object': source,
#     }
#     return render(request, 'source_delete.html', context=context)

# def response_codes(request):
#     response = HttpResponse("Response", status=404)
#     return response
