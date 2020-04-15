from app import app
import unittest


class FlaskTestCode(unittest.TestCase):
    def test_index(self):
        tester= app.test_client(self)
        responds = tester.get('/login', content_type='html/text')
        self.assertEqual(responds.status_code, 200)



if __name__ == '__name__':
    unittest.main()