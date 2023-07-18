import seldom


class TestBaidu(seldom.TestCase):
    """
    http api test demo
    doc: https://requests.readthedocs.io/en/master/
    """


    def test_get_method(self):
        """
        test get request
        """
        payload = {'source_country_code': 'sg'}
        self.get("/v1/transfercarrentalapisrv/app_home", params=payload)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True, base_url="http://t21.fat.klook.io")

