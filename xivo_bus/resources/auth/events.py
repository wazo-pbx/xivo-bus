# -*- coding: utf-8 -*-
# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


class _BaseExternalAuthEvent(object):

    def __init__(self, user_uuid, external_auth_name):
        self._body = dict(user_uuid=str(user_uuid), external_auth_name=external_auth_name)
        self.routing_key = self.routing_key_fmt.format(**self._body)
        self.required_acl = 'events.{}'.format(self.routing_key)

    def marshal(self):
        return self._body

    def __ne__(self, other):
        return not self._body == other._body

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._body == other._body

    @classmethod
    def unmarshal(cls, body):
        return cls(**body)




class UserExternalAuthAdded(_BaseExternalAuthEvent):

    name = 'auth_user_external_auth_added'
    routing_key_fmt = 'auth.users.{user_uuid}.external.{external_auth_name}.created'


class UserExternalAuthAuthorized(_BaseExternalAuthEvent):

    name = 'auth_user_external_auth_authorized'
    routing_key_fmt = 'auth.users.{user_uuid}.external.{external_auth_name}.authorized'


class UserExternalAuthDeleted(_BaseExternalAuthEvent):

    name = 'auth_user_external_auth_deleted'
    routing_key_fmt = 'auth.users.{user_uuid}.external.{external_auth_name}.deleted'