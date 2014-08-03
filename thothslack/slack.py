# -*- coding: utf-8 -*-

import os
import re
import shlex

from pyramid.httpexceptions import HTTPUnauthorized

from thoth.service import Service


class Slack(Service):

    def validate(self, request):
        token = request.params.get('token')
        if not token or token != os.environ.get('THOTH_SLACK_OUTGOING_TOKEN'):
            raise HTTPUnauthorized()

    def make_argument(self, request):
        user_name = request.params.get('user_name')
        user_arg = ['-u', user_name] if user_name else []
        room_name = request.params.get('channel_name')
        room_arg = ['-r', room_name] if room_name else []
        m = re.match(
            r'^{}\W*(.*)$'.format(request.params.get('trigger_word', '')),
            request.params.get('text', '')
        )
        return (user_arg + room_arg + shlex.split(m.group(1).decode('utf8'))) if m is not None else ''

    def make_response(self, result):
        return {
            'text': result,
            'link_names': 1,
            'parse': 'full',
        }

slack = Slack()
