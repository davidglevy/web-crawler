import re
from urllib.parse import urlparse
import unittest


def convertUrlToFile(url):
    parsed_uri = urlparse(url)

    regex = re.compile('([A-Za-z\.]+)(:[\d]+)?/.*')
    netloc = parsed_uri.netloc

    host = re.sub("([A-Za-z\.]+)(:[\d]+)?", "\g<1>", netloc)
    host = re.sub("\.", "-", host)

    path = parsed_uri.path
    path = re.sub("/", "-", path)
    if path.startswith("-"):
        path = path[1:]

    if len(path) > 0:
        result = host + "_" + path + ".pdf"
    else:
        result = host + ".pdf"

    return result


class TestConvertUrlToFile(unittest.TestCase):

    def test_with_port(self):
        test_url_1 = "https://www.github.com:443/my/path"
        result = convertUrlToFile(test_url_1)
        expected_file_name_1 = "www-github-com_my-path.pdf"
        self.assertEqual(expected_file_name_1, result)







