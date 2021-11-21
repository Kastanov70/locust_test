master:
    locust -f mongo_test.py --master --master-bind-host=51.250.19.17 --master-bind-port=8089 --expect-workers=2

worker:
    locust -f mongo_test.py --worker --master-host=51.250.19.17 --master-port=8089