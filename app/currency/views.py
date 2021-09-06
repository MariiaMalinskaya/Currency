from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

# from currency.utils import generate_password as gen_pass

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


# def hello_world(request):
#     return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html')


# def generate_password(request):
#     password_len = int(request.GET.get('password-len'))
#     password = gen_pass(password_len)
#     return HttpResponse(password)

def contact_us(request):
    contacts = ContactUs.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'contact_us.html', context=context)

    # result = []
    # for contact in contacts:
    #     result.append(
    #         f'Name:{contact.firstname} {contact.lastname} Contact Info: {contact.phone} {contact.mail}</br>'
    #     )
    # return HttpResponse(str(result))

    # return HttpResponse("Contact Us")


def rate_list(request):
    rates = Rate.objects.all()

    context = {
        'rate_list': rates,
    }
    return render(request, 'rate_list.html', context=context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()
    context = {
        'form': form,
    }
    return render(request, 'rate_create.html', context=context)
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


def get_source_list(request):
    sources = Source.objects.all()
    # result =[]
    # for source in sources:
    #     result.append(
    #         f'Id:{source.id} URL: {source.source_url} Name: {source.name}</br>'
    #     )
    # return HttpResponse(str(result))
    context = {
        'source_list': sources,
    }
    return render(request, 'source_list.html', context=context)


def rate_details(request, rate_id):
    # /rate/details/?rate-d = .. VS rate/details/102/
    # try:
    #     rate = Rate.objects.get(id=rate_id)
    # except Rate.DoesNotExist as exc:
    #         raise Http404(exc)
    rate = get_object_or_404(Rate, id=rate_id)
    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def rate_update(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)
    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)
    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == "POST":
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    # if request method is 'GET'
    context = {
        'object': rate,
    }
    return render(request, 'rate_delete.html', context=context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source-list/')
    elif request.method == 'GET':
        form = SourceForm()
    context = {
        'form': form,
    }
    return render(request, 'source_create.html', context=context)


def source_details(request, source_id):
    source = get_object_or_404(Source, id=source_id)
    context = {
        'object': source,
    }
    return render(request, 'source_details.html', context=context)


def source_update(request, source_id):
    source = get_object_or_404(Source, id=source_id)
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source-list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)
    context = {
        'form': form,
    }
    return render(request, 'source_create.html', context=context)


def source_delete(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == "POST":
        source.delete()
        return HttpResponseRedirect('/source-list/')
    # if request method is 'GET'
    context = {
        'object': source,
    }
    return render(request, 'source_delete.html', context=context)

# def response_codes(request):
#     response = HttpResponse("Response", status=404)
#     return response
