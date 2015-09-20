# coding: utf-8

from flask.ext.testing import TestCase
from application import app

class TaskTestCase(TestCase):
    def create_app(self):
        test_app = app
        test_app.config.update(
                DEBUG = True,
                TESTING = True
        )

        return test_app

    def test_valid_payload(self):
        payload =  [{
            'uid': '1',
            'name': 'John Doe',
            'date': '2015-05-12T14:36:00.451765',
            'md5checksum': 'e8c83e232b64ce94fdd0e4539ad0d44f'}]
        resp = self.client.post(
            url_for('store_payload'),
            data=payload
        )
        self.assertStatus(resp, 201)

    def test_invalid_payload(self):
        payload =  [{
            'uid': '1',
            'name': 'John Doe',
            'date': '2015-05-12T14:36:00.451765',
            'md5checksum': 'e8c83e232b64ce94fdd0e4539ad0d44e'}]
        resp = self.client.post(
            url_for('store_payload'),
            data=payload
        )
        self.assertStatus(resp, 500)

    def test_payload_count(self):
        resp = self.client.get(
            url_for('count_payloads', uid = "1", date = "20150512")
        )
        self.assertStatus(resp, 200)
        self.assertTrue(resp.json['count'] > 0)


