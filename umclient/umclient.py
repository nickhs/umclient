import requests
from urlparse import urlparse


class AuthenticatedUMClientException(Exception):
    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return "[HTTP Code: %s] Failed at %s" % (self.status_code, self.url)


class AuthenticatedUMClient():
    WEBLOGIN_COSIGN_URL = "https://weblogin.umich.edu/cosign-bin/cosign.cgi"

    def __init__(self, username, password, verbose=False):
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.verbose = verbose

    def _login(self, ref, username=None, password=None):
        if not username:
            username = self.username

        if not password:
            password = self.password

        payload = {
            'login': username,
            'password': password,
            'required': None,
            'tokencode': None
        }

        parsed_ref = urlparse(ref)
        netloc = parsed_ref[1]
        service = netloc[:netloc.find('.umich.edu')]
        payload['service'] = 'cosign-' + service
        payload['ref'] = ref

        resp = self.session.post(self.WEBLOGIN_COSIGN_URL, data=payload)
        return resp

    def _noisy_login(self, resp, username=None, password=None):
        self._print("[.] Logging in")
        resp = self._login(resp.history[-1].url, username, password)
        if resp.ok is True:
            self._print("[.] Logged in")
        else:
            self._print("[x] Failed to log in")
            self._print("[x] Response Code: %s" % resp.status_code)
            self._print("[x] Response URL: %s" % resp.url)
            raise AuthenticatedUMClientException(resp.status_code, resp.url)

    def _print(self, msg):
        if self.verbose:
            print msg

    def get(self, url, **kwargs):
        resp = self.session.get(url, **kwargs)
        if 'weblogin.umich.edu' in resp.url:
            self._noisy_login(resp)

        return resp

    def post(self, url, data=None, **kwargs):
        resp = self.session.post(url, data, **kwargs)
        if 'weblogin.umich.edu' in resp.url:
            self._noisy_login(resp)

        return resp
