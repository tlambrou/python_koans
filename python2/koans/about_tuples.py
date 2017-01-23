#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTuples(Koan):
    def test_creating_a_tuple(self):
        count_of_three = (1, 2, 5)
        self.assertEqual(5, count_of_three[2])

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):
        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            self.assertMatch("'tuple' object does not support item assignment", ex[0])

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three = (1, 2, 5)
        try:
            count_of_three.append("boom")
        except Exception as ex:
            self.assertEqual(AttributeError, type(ex))

            # Note, assertMatch() uses regular expression pattern matching,
            # so you don't have to copy the whole message.
            self.assertMatch("'tuple' object has no attribute 'append'", ex[0])

        # Tuples are less flexible than lists, but faster.

    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual((1, 2, 5, "boom"), count_of_three)

    def test_tuples_of_one_look_peculiar(self):
        self.assertEqual(int, (1).__class__)
        self.assertEqual(tuple, (1,).__class__)
        self.assertEqual(("Hello comma!", ), ("Hello comma!", ))

    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!'), tuple("Surprise!"))

    def test_creating_empty_tuples(self):
        self.assertEqual(__, ())
        self.assertEqual(__, tuple())  # Sometimes less confusing

    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(__, place)

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append(
            ("Cthulhu", (26, 40, 1, 'N'), (70, 45, 7, 'W'))
        )

        self.assertEqual(__, locations[2][0])
        self.assertEqual(__, locations[0][1][2])