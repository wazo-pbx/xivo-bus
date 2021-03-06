# -*- coding: utf-8 -*-
# Copyright 2013-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import unicode_literals

import unittest
from ..event import ExtensionConfigEvent


class ConcreteExtensionConfigEvent(ExtensionConfigEvent):

    name = 'foo'


ID = 42
EXTEN = '1001'
CONTEXT = 'default'


class TestAbstractExtensionIDParams(unittest.TestCase):

    def setUp(self):
        self.msg = {
            'id': ID,
            'exten': EXTEN,
            'context': CONTEXT
        }

    def test_marshal(self):
        command = ConcreteExtensionConfigEvent(ID, EXTEN, CONTEXT)

        msg = command.marshal()

        self.assertEqual(msg, self.msg)

    def test_unmarshal(self):
        command = ConcreteExtensionConfigEvent.unmarshal(self.msg)

        self.assertEqual(command.name, ConcreteExtensionConfigEvent.name)
        self.assertEqual(command.id, ID)
        self.assertEqual(command.exten, EXTEN)
        self.assertEqual(command.context, CONTEXT)
