#!/usr/bin/env python3
"""TestAccessNestedMap module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized  # type: ignore
from typing import Any, Dict, Mapping, Sequence

# Local
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function from utils."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """Test that the access_nested_map function returns expected
        results.

        Args:
            nested_map (Mapping): A nested map.
            path (Sequence): a sequence of key representing a path to the value
            expected (Any): Expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ):
        """Test that when access_nest_map is called with invalid path
        it raises KeyError.

        Args:
            nested_map (Mapping): A nested map.
            path (Sequence): A sequence of key representing a path to the value
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json from utils."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict):
        """Test get_json returns correct data from the requested url.

        Args:
            test_url (str): URL to get.
            test_payload (Dict): JSON data used in testing.
        """
        with patch(
            "requests.get", side_effect=self.mocked_requests_get
        ) as mock_get:
            returned_payload = get_json(test_url)
            self.assertEqual(returned_payload, test_payload)

            self.assertEqual(mock_get.call_count, 1)

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        """Mock requests.get function.

        Returns:
            MockResponse: An instance of MockResponse that implements
                the json method used in retrieving the json data.
        """

        class MockResponse:
            """Mocks the Response returned by a requests.get call.
            Returned as the response object by the mocked_requests_get.
            """

            def __init__(self, json_data, status_code):
                """Initializing a new MockResponse"""
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                """Returns json data"""
                return self.json_data

        if args[0] == "http://example.com":
            return MockResponse({"payload": True}, 200)
        elif args[0] == "http://holberton.io":
            return MockResponse({"payload": False}, 200)

        return MockResponse(None, 404)


class TestMemoize(unittest.TestCase):
    """Test the memorize decorator from utils"""

    def test_memoize(self):
        """Test the memoize decorator"""

        class TestClass:
            """TestClass"""

            def a_method(self):
                """A method"""
                return 42

            @memoize
            def a_property(self):
                """A property decorated by the memoize decorator"""
                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=42
        ) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
