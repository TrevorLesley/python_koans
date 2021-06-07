#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutAsserts(Koan):
    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        # self.assertTrue(False) # This should be True
        self.assertTrue(True)

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        # self.assertTrue(False, "This should be True -- Please fix this")
        self.assertTrue(True, "This is now true, with a message.")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        # self.assertEqual(__, 1 + 1)
        self.assertEqual(2, 1 + 1)

        # A test that measures if the first and second arguments are equal.

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """

        #  A test that measures if each variable are equal to one another.

        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

        # This test is to test equal value rather than the boolean value.

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        # assert False
        assert True
        # The assert keyword is shorthand for testing the boolean for true false values.

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        # self.assertEqual(__, "navel".__class__)  # It's str, not <type 'str'>
        self.assertEqual(str, "navel".__class__)

        # This test is testing if the first and second arg are identical datatypes.
        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute
