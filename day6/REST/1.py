from flask import Flask, json
from flask_restful import Resource, Api, reqparse

companies = []

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
    return json.dumps(companies)

@api.route('/companies', methods=['POST'])
def post_companies():
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True)
    parser.add_argument('name', required=False)

    args = parser.parse_args()

    new_company = {"id":args['id'], "name":args['name']}

    companies.append(new_company)
    return json.dumps({"succuessfully added company to list":True}), 201

@api.route('/companies', methods=['DELETE'])
def delete_companies():

    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True)
    args = parser.parse_args()
    
    for i in range(len(companies)):
        if companies[i]['id'] == args['id']:
            del companies[i]
            break

    
    return json.dumps({"succuessfully deleted the company the list":True}), 201

api.run()
