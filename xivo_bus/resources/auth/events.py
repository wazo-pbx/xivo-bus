# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


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


class _BaseTenantEvent(object):

    def __init__(self):
        self.routing_key = self.routing_key_fmt.format(**self._body)
        self.required_acl = 'events.{}'.format(self.routing_key)

    def marshal(self):
        return self._body

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._body == other._body

    @classmethod
    def unmarshal(cls, body):
        return cls(**body)


class TenantCreatedEvent(_BaseTenantEvent):

    name = 'auth_tenant_added'
    routing_key_fmt = 'auth.tenants.{uuid}.created'

    def __init__(self, uuid, name):
        self._body = {'uuid': uuid, 'name': name}
        super(TenantCreatedEvent, self).__init__()


class TenantUpdatedEvent(_BaseTenantEvent):

    name = 'auth_tenant_updated'
    routing_key_fmt = 'auth.tenants.{uuid}.updated'

    def __init__(self, uuid, name):
        self._body = {'uuid': uuid, 'name': name}
        super(TenantUpdatedEvent, self).__init__()


class TenantDeletedEvent(_BaseTenantEvent):

    name = 'auth_tenant_deleted'
    routing_key_fmt = 'auth.tenants.{uuid}.deleted'

    def __init__(self, uuid):
        self._body = {'uuid': uuid}
        super(TenantDeletedEvent, self).__init__()


class UserExternalAuthAdded(_BaseExternalAuthEvent):

    name = 'auth_user_external_auth_added'
    routing_key_fmt = 'auth.users.{user_uuid}.external.{external_auth_name}.created'


class UserExternalAuthAuthorized(_BaseExternalAuthEvent):

    name = 'auth_user_external_auth_authorized'
    routing_key_fmt = 'auth.users.{user_uuid}.external.{external_auth_name}.authorized'


class UserExternalAuthDeleted(_BaseExternalAuthEvent):

    name = 'auth_user_external_auth_deleted'
    routing_key_fmt = 'auth.users.{user_uuid}.external.{external_auth_name}.deleted'


class SessionCreatedEvent(_BaseTenantEvent):

    name = 'auth_session_created'
    routing_key_fmt = 'auth.sessions.{uuid}.created'

    def __init__(self, uuid, user_uuid, **kwargs):
        self._body = {
            'uuid': uuid,
            'user_uuid': user_uuid,
            'mobile': kwargs.get('mobile', False),
        }
        super(SessionCreatedEvent, self).__init__()


class SessionDeletedEvent(_BaseTenantEvent):

    name = 'auth_session_deleted'
    routing_key_fmt = 'auth.sessions.{uuid}.deleted'

    def __init__(self, uuid):
        self._body = {'uuid': uuid}
        super(SessionDeletedEvent, self).__init__()
