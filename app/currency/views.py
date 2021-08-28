from currency.models import ContactUs, Rate, Source

# from currency.forms import RateForm
# from currency.utils import generate_password as gen_pass

from django.shortcuts import render
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
    # form = RateForm()
    context = {
        # 'form': form
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

#
# def response_codes(request):
#     response = HttpResponse("Response", status=404)
#     return response
