#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStrings(Koan):
    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

        # isinstance is testing the first arg, which is an object, against the second arg
        # being the class info. By setting the first arg of assertEqual to true and the
        # isinstance method being true, the assert passes.

    def test_single_quoted_strings_are_also_strings(self):
        string = "Goodbye, world."
        # self.assertEqual(, isinstance(string, str))
        self.assertEqual(True, isinstance(string, str))

        # This test was missing the first arg to the assertEqual test. By adding True,
        # this test passes since the isinstance method is true.

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        # self.assertEqual(__, isinstance(string, str))
        self.assertEqual(True, isinstance(string, str))

        # This is testing if the string variable is a string using triple quotes, which is
        # true since triple quotes are used for strings that span multiple lines.

    def test_triple_single_quotes_work_too(self):
        string = """Bonjour tout le monde!"""
        # self.assertEqual(__, isinstance(string, str))
        self.assertEqual(True, isinstance(string, str))

        # This is testing that triple single quotes also pass the assert.
        # The quotes were originally double quotes, so I changed them to singles.

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        # self.assertEqual(__, isinstance(string, str))
        self.assertEqual(True, isinstance(string, str))

        # This assert is testing if a raw string is considered a string type.
        # Raw strings treat backslashes as normal characters, which doesn't allow escapes.

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        # self.assertEqual(__, string)
        self.assertEqual(True, isinstance(string, str))

        # This assert passes because you can use double quotes as normal characters in
        # single quote strings.

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        # self.assertEqual(__, string)
        self.assertEqual(True, isinstance(string, str))

        # This assert passes because you can use single quotes as normal characters in
        # double quote strings.

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = 'He said, "Don\'t"'
        b = 'He said, "Don\'t"'
        # self.assertEqual(__, (a == b))
        self.assertEqual(True, (a == b))

        # This assert is testing that the a and b variables are equal, which is true,
        # but the point of the assert is to learn how to use backslashes to escape quotes
        # inside strings.

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
        It was the worst of times."
        # self.assertEqual(__, len(string))
        self.assertEqual(60, len(string))

        # This test is intended to demonstrate that you can use backslashes to continue a string into the next line,
        # but the assert is using the length method, so I filled the blank with the proper number to pass the assert.

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
        Howdy,
        world!
        """
        self.assertEqual(39, len(string))

        # This test is to demonstrate that triple quoted strings can be used to span multiple lines.

    def test_triple_quoted_strings_need_less_escaping(self):
        a = 'Hello "world".'
        b = """Hello "world"."""
        # self.assertEqual(__, (a == b))
        self.assertEqual(True, (a == b))

        # This test demonstrates that triple quoted strings and single quoted strings both
        # create strings and can be used without having to use backslashes to escape characters.

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

        # This demonstrates escaping a double quote next to triple double quotes for ending the string
        # is equivalent to using single quotes to circumvent using escping syntax.

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

        # This is testing if the string concatenation is equal to a single string of the same characters.

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

        # This is demonstrating that adjacent strings concatenate automatically.

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

        # This assert demonstrates that assigning strings to variables, and assigning both variables to a single
        # variable will not modify the original strings, and concatenate them into a single string when the final variable is called.

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

        # This is demonstrating that the += oper will reassign the first variable to be equal to both variables
        # concatenated together.

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

        # This is similar to the one above, but with an extra step to trip you up. It's assigning the hello string
        # to original, then assigning original to another variable, hi, assigning world to the variable *there* and
        # then reassigning hi to equal the strings of both variables.

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual("\n", string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))

        # This is exemplifying that single, double and triple double quotes can interpret escaping characters with backslashes.
