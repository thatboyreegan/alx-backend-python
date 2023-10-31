#!/usr/bin/env python3
"""Module with class TestAccessNestedMap"""

import unittest
from parameterized import parameterized
from typing import Sequence, Mapping, Any, Dict
from unittest.mock import patch

access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """test for the acces_nested_map function"""
    @parameterized.expand(
        [
           ({"a": 1}, ("a",), 1),
           ({"a": {"b": 2}}, ("a",), {"b": 2}),
           ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_acces: Mapping, path: Sequence, expected: Any
    ):
        """Tests that access_nested_map returns the expected output

        Args:
            nested_map (Mapping): a nested map
            path (sequence): path to the value in the nested map
            expected (Any): expected result according to the logic of thefn
        """
        self.assertEqual(access_nested_map(nested_acces, path), expected)

    @parameterized.expand(
        [({}, ("a",)),
         ({"a": 1}, ("a", "b"))]
    )
    def test_access_nested_map_exception(
        self, nested_access: Mapping, path: Sequence
    ):
        """Tests if access_nested_map raises a keyerror
        Args:
            nested_map (Mapping): nested map
            path (Sequence): a path to the expected value
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_access, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json in utils"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict):
        with patch(
            "requests.get", side_effect=self.mocked_requests
        ) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            self.assertEqual(mock_get.call_count, 1)

    @staticmethod
    def mocked_requests(*args):
        class MockedResponse:
            def __init__(self, json_data=None, status_code=404):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if args[0] == "http://example.com":
            return MockedResponse({"payload": True}, 200)
        elif args[0] == "http://holberton.io":
            return MockedResponse({"payload": False}, 200)

        return MockedResponse


class TestMemoize(unittest.TestCase):
    """Tests the utils.memoize decorator"""
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
            TestClass, "a_method", return_value=42
        ) as mock_method:
            class_instance = TestClass()
            self.assertEqual(class_instance.a_property, 42)
            self.assertEqual(class_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
