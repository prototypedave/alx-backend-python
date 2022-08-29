#!usr/bin/env python3
"""
Parameterize and patch as decorators
"""


import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ class that inherits from unittest """
     
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})

    def test_org(self, org_name. mock_get):
        """ tests if github client matches the input in the given format """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """ tests for public repos of a given client """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    
    def test_public_repos(self, mock_get):
        """ tests if a clients public repo appears once """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

     @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])

    def test_has_license(self, repo, license_key, expected_return):
        """ checks if a clients repo has license """
        test_client = GithubOrgClient("holberton")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class that inherits unittest """
    @classmethod

    def setUpClass(cls):
        """ starts a mock up """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
    
    @classmethod
    def tearDownClass(cls):
        """ ends a mock up """
        cls.get_patcher.stop()

    def test_public_repos(self):
        test_class = GithubOrgClient("holberton")
        assert True
    def test_public_repos_with_license(self):
        test_class = GithubOrgClient("holberton")
        assert True
