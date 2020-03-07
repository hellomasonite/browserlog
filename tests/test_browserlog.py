from masonite.testing import TestCase
from browserlog.utils import parse_log


class TestBrowserlog(TestCase):

    def test_log_1_file(self):
        for line in open('tests/1.log', 'r'):
            self.assertEqual(parse_log(line)['logged_at'], 'March 07 2020 19:42:41 PM')
            self.assertEqual(parse_log(line)['level'], 'error')
            self.assertEqual(parse_log(line)['message'], 'ContainerError')
            break

    def test_log_2_file(self):
        for line in open('tests/2.log', 'r'):
            self.assertIsNone(parse_log(line))
            break
