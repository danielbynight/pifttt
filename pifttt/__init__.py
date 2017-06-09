from __future__ import unicode_literals

import requests
import json
from urllib2 import quote


def if_this(key, event_name, value1=None, value2=None, value3=None):
    connector = IFTTTWebhook(key, event_name)
    return connector.send(value1, value2, value3)


class HookRequestError(Exception):
    """Base error with the request sent"""

    def __init__(self, response, *args):
        super(HookRequestError, self).__init__(self, *args)
        self.response = response


class InvalidKey(HookRequestError):
    """The key sent is not valid"""
    pass


class InvalidArgument(Exception):
    """One of the arguments passed to a method is incorrect"""
    pass


class IFTTTWebhook(object):
    URL = 'https://maker.ifttt.com/trigger/{event_name}/with/key/{key}'

    def __init__(self, key, event_name):
        if '/' in key or '/' in event_name:
            raise InvalidArgument('Keys and event names cannot contain forward slashes.')
        self.key = key
        self.event_name = event_name

    @property
    def url(self):
        return IFTTTWebhook.URL.format(key=self._format_url(self.key), event_name=self._format_url(self.event_name))

    def _format_post_data(self, value1=None, value2=None, value3=None):
        data = {}
        if value1 is not None:
            data['value1'] = value1
        if value2 is not None:
            data['value2'] = value2
        if value3 is not None:
            data['value3'] = value3

        return data

    def _format_url(self, value):
        return quote(value.encode('utf-8'))

    def send(self, value1=None, value2=None, value3=None):
        response = requests.post(self.url, data=self._format_post_data(value1, value2, value3))
        if response.status_code == 200:
            return response.content
        else:

            try:
                errors = json.loads(response.content)['errors']
                if errors == 'You sent an invalid key.':
                    raise InvalidKey(response, self.key)
            except KeyError:
                raise HookRequestError(response, 'Something went wrong, but no errors were found.')
            except ValueError:
                # No JSON data
                raise HookRequestError(response, 'Something went wrong.')
