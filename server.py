import os

import config

from flask import Flask, request, Response

from notifications import SmsNotificator

app = Flask(__name__)
app.config.from_object(config.__name__)


@app.route('/auth', methods=['POST'])
def authenticate_passphrase() -> Response:
    is_passphrase_correct = request.json['passphrase'] == os.environ.get('PASSPHRASE')
    return Response(status=200 if is_passphrase_correct else 403)


@app.route('/deploy', methods=['POST'])
def send_message() -> Response:
    repo, phone_number = request.json['repository'], request.json['phone_number']
    # TODO: Make the deploy happen then send the notification if enabled
    if config.NOTIFICATIONS_ENABLED:
        notificator = SmsNotificator(config={'key': config.VONAGE_KEY, 'secret': config.VONAGE_SECRET})
        notificator.notify(sender='K8s-deploy', receiver=phone_number, text='Your app is deployed!!!')
    return Response({'repo': repo, phone_number: phone_number})
