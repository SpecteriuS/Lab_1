import json

from tornado.testing import AsyncHTTPTestCase

from main import make_app

class TestMain(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_main(self):
        test_table = [
            ("America", "Top 1 BruTo, America"),
            ("Asia", "Top 1 levik, Asia"),
            ("Europe", "Top 1 Ustycmd, Europe")
        ]

        for test_case in test_table:
            responce = self.fetch(f"/?region={test_case[0]}")
            self.assertEqual(responce.code, 200)
            self.assertEqual(
                json.loads(responce.body)["ab"],
                test_case[-1]
            )