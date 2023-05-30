from django.shortcuts import render
from .forms import *
from twilio.rest import Client
from .keys import *
account_sid = 'AC72c0219aa883e4fa0e4ec2111889003b'
auth_token = 'b04e1de6fe6e0510c8a26098be3aa9ea'
twilio_number = '+13157125392'


def send_sms(request):
    form = SmsModel(request.POST or None)
    if form.is_valid():
        client = Client(account_sid, auth_token)
        phone_number = form.cleaned_data['phone_number']
        message = client.messages.create(
            body='Hello, World !',
            from_=twilio_number,
            to=request
        )
        print(message.sid)
        context = {'message': message, 'form': form}
    else:
        context = {'form': form}
    return render(request, 'sms_.html', context)





# client = Client(keys.account_sid, keys.auth_token)
# message = client.messages.create(
#     body='Hello, World !',
#     from_=keys.twilio_number,
#     to=keys.target_number,
# )
