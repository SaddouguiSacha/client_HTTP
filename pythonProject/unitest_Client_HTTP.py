import unittest
from unittest.mock import patch
from io import StringIO
import Client_HTTP

class TestHTTPClient(unittest.TestCase):
    @patch("builtins.input", side_effect=["https://httpbin.org/get\n"])
    def test_client_http_get(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            url = mock_input()
            Client_HTTP.client_http_get(url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Reponse :", output)

    @patch("builtins.input", side_effect=["https://httpbin.org/post\n"])
    def test_client_http_post(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            data = {"key": "value"}
            url= mock_input()
            Client_HTTP.client_http_post(data, url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Reponse :", output)

    @patch("builtins.input", side_effect=["https://httpbin.org/put\n"])
    def test_client_http_put(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            data = {"key": "value"}
            url= mock_input()
            Client_HTTP.client_http_put(data, url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Reponse :", output)
            

if __name__ == '__main__':
    unittest.main()