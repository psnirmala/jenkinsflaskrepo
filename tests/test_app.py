import unittest
from .. import app

class BasicTests(unittest.TestCase):
    app1=app.app
    tester=app1.test_client(self)
    response=tester.get("/",content_type='html/text')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.data,b"HEllo, Jenkins CI/CD from Flask App on Windows!")


if __name__=="__main__":
    unittest.main()