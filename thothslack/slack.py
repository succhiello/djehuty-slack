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

    def get_user(self, request):
        return request.params.get('user_name')

    def get_room(self, request):
        return request.params.get('channel_name')

    def make_command_line(self, request):
        m = re.match(
            r'^{}\W*(.*)$'.format(request.params.get('trigger_word', '')),
            request.params.get('text', '')
        )
        return shlex.split(m.group(1).encode('utf8')) if m is not None else []

    def make_response(self, result):
        return {
            'text': result,
            'link_names': 1,
            'parse': 'full',
        }

slack = Slack()
