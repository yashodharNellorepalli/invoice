from flask import Blueprint, jsonify, request
from app.documents.services import get_document_info, get_document_status, add_document
from app.documents.helpers import allowed_file
from app.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.utils.helpers import get_config_value
from werkzeug.utils import secure_filename
import os


customers_module = Blueprint('customers', __name__, url_prefix='/customers')


@customers_module.route('/upload-document', methods=['POST'])
def upload_document_():
    # insert into documents
    print(request.files)
    if 'file' not in request.files:
        response_data = {
            'error': 'file not found'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    file = request.files['file']

    if file.filename == '':
        response_data = {
            'error': 'file name is not there'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(get_config_value('UPLOAD_FOLDER'), filename))
    else:
        response_data = {
            'error': 'file ext is invalid'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    request_args = request.args
    customer_id = request_args.get('customer_id')
    status, x = add_document(customer_id)

    if not status:
        response_data = {
            'error': x
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    response_data = {
        'document_id': x
    }

    return jsonify(response_data), HTTP_201_CREATED


@customers_module.route('/document-status', methods=["GET"])
def fetch_document_status():
    request_args = request.args
    document_id = request_args.get('document_id')
    document_info = get_document_info(document_id)

    if not document_info:
        response_data = {
            'error': 'document_id not found'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    document_status_id = document_info.get('document_status_id')
    document_status = get_document_status(document_status_id)

    if not document_status:
        response_data = {
            'error': 'document_status not found'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    response_data = {
        "status": document_status.get('status')
    }

    return jsonify(response_data), HTTP_200_OK


@customers_module.route('/digitized-document', methods=['GET'])
def get_digitized_document():
    request_args = request.args
    document_id = request_args.get('document_id')
    document_info = get_document_info(document_id)

    if not document_info:
        response_data = {
            'error': 'document_id doesnt exist'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    document_status_id = document_info.get('document_status_id')
    document_status = get_document_status(document_status_id)

    if not document_status:
        response_data = {
            'error': 'document_status not found'
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    document_status_value = document_status.get('status')

    if document_status_value != 'digitized':
        response_data = {
            'message': 'document is not yet digitized',
            'status': document_status_value,
            'document_info': {

            }
        }

        return jsonify(response_data), HTTP_200_OK

    response_data = {
        'message': 'Success',
        'status': document_status_value,
        'document_info': document_info
    }

    return jsonify(response_data), HTTP_200_OK
