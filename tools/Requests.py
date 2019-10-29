from woocommerce import API


class Requests:

    def __init__(self):
        admin_consumer_key = 'ck_e5bf8b09f7dddc049037c01bb6cd540695363b75'
        admin_consumer_secret = 'cs_2543d5b7ed833e6cf83ae4c3e8f2e5f0ccf5538a'

        self.wcapi = API(
            url="http://127.0.0.1/wp",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            version="wc/v3")

    def test_api(self):
        """

        :return:
        """

        print(self.wcapi.get("").json())

    def post(self, endpoint, data):
        """

        :param endpoint:
        :param data:
        :return:
        """
        result = self.wcapi.post(endpoint, data)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def get(self, endpoint):
        """

        :param endpoint:
        :return:
        """
        result = self.wcapi.get(endpoint)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]
