#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unittest import TestCase, main
from strash.strash import Strash


class Tests_Safeclean(TestCase):
    def setUp(self):
        self.s = Strash()

    def test_verify_user(self):
        self.assertTrue(self.s.verify_user(0))

    def test_python_version_required(self):
        self.assertTrue(self.s.python_version_required())

    def test_verify_dependencies(self):
        self.assertTrue(self.s.verify_dependencies())

    def test_clean(self):
        self.assertTrue(self.s.clean())


if __name__ == "__main__":
    main()
