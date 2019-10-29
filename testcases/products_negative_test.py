from tools import Requests


rq = Requests.Requests()


def test_neg_tc1_product_empty_payload():
    """

    :return:
    """
    print("Running Test Case 1: Testing 'products' endpoint, with payload empty json")

    input_data = {}
    info = rq.post('products', input_data)

    print(info)


test_neg_tc1_product_empty_payload()