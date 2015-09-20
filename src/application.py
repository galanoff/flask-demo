# coding: utf-8
"""
    application
    ~~~~~~~~~~~

    Application initialization
    and app-specific registrations.
"""

from flask import Flask
from flask import request
from flask.ext.restplus import Api, Resource
from flask.ext.pymongo import PyMongo
from exceptions import Exception

import sys
import json
import hashlib
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object('settings')

api = Api(app)
mongo = PyMongo(app)

@api.route('/v1/store', endpoint='store_payload')
class PayloadStore(Resource):
    """ Store a json payload to the database
    :return: JSON structure
        POST /v1/store
        {'body': <POST params>}
        >> {'code': 201}

    :error: JSON structure
        POST /v1/store
        {'body': <POST params>}
        >> {'code': 500, 'errors': ['exception message']}
    """

    def post(self):
        payloads = request.get_json()
        resp = { 'errors': [] }
        for payload in payloads:
            try:
                data = self._clear_payload(payload)
                self._store_payload(data)
            except Exception, e:
#                resp['code'] = 500
                resp['errors'].append({'uid': payload['uid'], 'msg': str(e)})
        resp['code'] = 201
        return resp, resp['code']

    def _clear_payload(self, payload):
        data = {}
        for key in ("date", "uid", "name"):
            data[key] = payload[key]

        if hashlib.md5(json.dumps(data)).hexdigest() == payload['md5checksum']:
            return data
        else:
            raise Exception('Incorrect MD5 checksum')


    def _store_payload(self, payload):
        payload['date'] = datetime.strptime(payload['date'],'%Y-%m-%dT%H:%M:%S.%f')
        mongo.db.payloads.insert(payload)


@api.route('/v1/payloads/<uid>/<date>', endpoint='count_payloads')
@api.doc(params={'uid': 'User ID', 'date': 'Data filter'})
class PayloadCount(Resource):
    """ Count payloads accumulated by date

    :return: JSON structure
        GET /v1/payloads/1/20150920
        >> {
            "count": 1,
            "code": 200
        }

    :error: JSON structure
        GET /v1/payloads/invalid_uid/20150920
        >> {
            "count": 0,
            "code": 200
        }

    :error: JSON structure
        GET /v1/payloads/1/invalid_date
        >> {'code': 500, 'errors': ['exception message']}

    """

    def get(self, uid, date):
        resp = {}
        try:
            from_date = datetime.strptime(date,"%Y%m%d")
            to_date = from_date + timedelta(days=1)
        except ValueError, e:
            resp['errors'] = [str(e)]
            resp['code'] = 500
        else:
            count = mongo.db.payloads.find({'uid': uid, 'date': {'$gte': from_date, '$lt': to_date}}).count()
            resp = {'count': count, 'code': 200}
        return resp, resp['code']



