#!/usr/bin/env python3
"""Module for testing GithubOrgClient"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class  # type: ignore

from typing import Dict, List, Union

get_json = __import__("utils").get_json

GithubOrgClient = __import__("client").GithubOrgClient
TEST_PAYLOAD = __import__("fixtures").TEST_PAYLOAD

(
    test_repos_url,
    test_public_repos,
    expected_public_repos,
    public_repos_apache_license,
) = TEST_PAYLOAD[0]


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient Class"""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json", return_value={})
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """Test that the org property calls get_json as expected.

        Args:
            org_name (str): Name of the organization.
            mock_get_json (MagicMock): Mock of the get_json function
                in client.py
        """
        instance = GithubOrgClient(org_name)
        instance.org

        mock_get_json.assert_called_once_with(
            instance.ORG_URL.format(org=org_name)
        )

    @patch.object(
        GithubOrgClient,
        "org",
        new_callable=PropertyMock,
        return_value=test_repos_url,
    )
    def test_public_repos_url(self, mock_org: PropertyMock):
        """Test that _public_repos_url property returns expected value

        Args:
            mock_org (PropertyMock): A mock of the org property.
        """
        instance = GithubOrgClient("google")
        repos_url = instance._public_repos_url

        self.assertEqual(repos_url, test_repos_url["repos_url"])
        mock_org.assert_called_once()

    @patch("client.get_json", return_value=test_public_repos)
    def test_public_repos(
        self,
        mock_get_json: MagicMock,
    ):
        """Test the public_repos method in GithubOrgClient.

        Args:
            mock_get_json (MagicMock): A mock of the get_json function.
        """
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="",
        ) as mock_public_repos_url:
            instance = GithubOrgClient("google")
            public_repos = instance.public_repos()

            self.assertEqual(public_repos, expected_public_repos)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""

        instance = GithubOrgClient("google")
        has_license = instance.has_license(repo, license_key)

        self.assertEqual(has_license, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (
            test_repos_url,
            test_public_repos,
            expected_public_repos,
            public_repos_apache_license,
        )
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set the get_patcher that mocks requests.get"""

        def mocked_requests_get(url):
            """Mock requests.get function.

            Returns:
                MockResponse: An instance of MockResponse that implements
                    the json method used in retrieving the json data.
            """

            class MockResponse:
                """Mocks the Response returned by a requests.get call.
                Returned as the response object by the mocked_requests_get.
                """

                def __init__(
                    self, json_data: Union[Dict, List, None], status_code: int
                ):
                    """Initializing a new MockResponse"""
                    self.json_data = json_data
                    self.status_code = status_code

                def json(self):
                    """Returns json data"""
                    return self.json_data

            if url == "https://api.github.com/orgs/google":
                return MockResponse(cls.org_payload, 200)
            elif url == "https://api.github.com/orgs/google/repos":
                return MockResponse(cls.repos_payload, 200)
            elif url.startswith("https://api.github.com/repos/google/"):
                repo_name = url.split("/")[-1]
                for repo in cls.repos_payload:
                    if repo["name"] == repo_name:
                        return MockResponse(repo, 200)

            return MockResponse(None, 404)

        cls.get_patcher = patch(
            "requests.get", side_effect=mocked_requests_get
        )

        cls.get_patcher.start()

    def test_public_repos(self):
        """Test the public_repos method without providing license"""

        instance = GithubOrgClient("google")
        repos = instance.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license key provided"""

        instance = GithubOrgClient("google")
        repos = instance.public_repos(license="apache-2.0")

        self.assertEqual(repos, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """Stop get_patcher mocking requests.get"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
