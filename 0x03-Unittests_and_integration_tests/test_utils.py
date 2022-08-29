#!/usr/bin/env python3
"""
Parameterize a unit test
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ inherits from unittest class """
   
    """ path test case with expected output """ 
    @parameterized.expand([
        ({"a" : 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """ test accss of the path from a nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    """ values that can raise error but are exceptional """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])

    def test_access_nested_map_exception(self, nested_map, path):
    """ raises exception error from the code """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])

class TestGetJson(unittest.TestCase):
    """ test class that inherits from unittest """
    
    """ assigns data to prevent delay from loading over a network """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
 
    def test_get_json(self, test_url, test_payLoad, mock_get):
        """ test if the function works without loading """
        mock_get.return_value = test_payLoad
        result = get_json(test_url)
        self.assertEqual(result, test_payLoad)

class TestMemoize(unittest.TestCase):
    """ class that extends from unittest """

    def test_memoize(self):
        """ tsst function for memoize - iy initializes the test method """
 
        class TestClass:
            """ class that extends Test Memoize """
            
            def a_method(self):
                return 42
       
            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
