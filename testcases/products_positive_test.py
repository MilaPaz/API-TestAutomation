import json
from tools import Requests
from tools import DBConnect

rq = Requests.Requests()
qry = DBConnect.DBConnect()


def test_create_a_product():
    """

    :return:
    """
    global product_id
    global name
    global price

    name = 'Test Product1'
    price = '9.99'
    input_data = {
        "name": name,
        "type": "simple",
        "regular_price": price,
        "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
        "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.",
        "categories": [
            {
                "id": 9
            },
            {
                "id": 14
            }
        ],
        "images": [
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg"
            }
        ]
    }

    info = rq.post('products', input_data)
    response_code = info[0]
    response_body = info[1]
    # print(json.dumps(info[1], indent=4))

    assert response_code == 201, "The status code returned for created product is not as expected. " \
                                 "Expected: 201, Actual: {act}".format(act=response_code)
    # 201 Created. The request has been fulfilled and has resulted in one or more new resources being created.

    rs_name = response_body["name"]
    rs_price = response_body["regular_price"]
    product_id = response_body["id"]

    print("product name is: {} and product id is: {}".format(rs_name, product_id))

    assert rs_name == name, "The name in the response is not the same as in the request. " \
                            "The response name is: {}".format(rs_name)

    assert rs_price == price, "The price in the response is not the same as in the request. " \
                              "Expected: {}, Actual: {}".format(price, rs_price)

    print("The create a product test passed")


def test_verify_product_created_in_db():
    """

    :return:
    """

    # get product information from database
    sql = '''SELECT p.post_title, p.post_type, pm.meta_value FROM wppo_posts p JOIN wppo_postmeta pm 
             ON p.id=pm.post_id WHERE p.id={} AND pm.meta_key='_regular_price' '''.format(product_id)
    qrs = qry.select('wp487', sql)

    print(qrs)

    # data extraction
    db_title = qrs[0][0]
    db_type = qrs[0][1]
    db_regular_price = qrs[0][2]

    # verify the title in db is as expected
    assert db_title == name, "The title in DB is not as expected. DB title: {}, Expected: {}".format(db_title, name)

    # verify the post type is as expected
    assert db_type == 'product', "The post type in DB is not 'product'. Expected: 'product', Actual: {}".format(db_type)

    # verify the regular price is as expected
    assert db_regular_price == price, "The price in DB is not as expected. " \
                                      "Expected: {}, Actual: {}".format(price, db_regular_price)

    print(" 'products_positive test case, verify product was created in DB, PASS")


test_create_a_product()
test_verify_product_created_in_db()
