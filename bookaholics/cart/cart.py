class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('sessionKey')

        if 'sessionKey' not in request.session:
            cart = self.session['sessionKey'] = {}

        self.cart = cart