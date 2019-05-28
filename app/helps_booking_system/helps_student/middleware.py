from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
import time


class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated():
            # Can't log out if not logged in
            return

        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass

        request.session['last_touch'] = datetime.now()

        # datetime.now() is equivalent to time.time()

        # class timeOutMiddleware(object):
        #
        #     def process_request(self, request):
        #         if request.user.is_authenticated():
        #             if 'lastRequest' in request.session:
        #                 elapsedTime = datetime.datetime.now() - \
        #                               request.session['lastRequest']
        #                 if elapsedTime.seconds > 15 * 60:
        #                     del request.session['lastRequest']
        #                     #logout(request)
        #
        #             request.session['lastRequest'] = datetime.datetime.now()
        #         else:
        #             if 'lastRequest' in request.session:
        #                 del request.session['lastRequest']
        #
        #         return None
