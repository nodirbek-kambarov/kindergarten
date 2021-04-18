from django.shortcuts import render
from .models import Order
from kg.sendmessage import sendTelegram


def contact_page(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        text = 'Оставил заявку' + '\n' + name + '\n' + 'Номер: ' + phone + '\n' + 'Сообщение: ' + message
        element = Order(order_name=name, order_phone=phone, order_text=message)
        sendTelegram(text)
        element.save()
        return render(request, './contact.html', {'name': name,
                                                  'phone': phone,
                                                  'message': message})
    else:
        return render(request, './contact.html')
