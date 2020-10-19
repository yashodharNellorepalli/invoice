schema

create table `customers`(
  `id` int auto_increment,
  `name` int default 0,
  `email` int default NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `documents`(
  `id` int auto_increment,
  `customer_id` int default 0,
  `invoice_id` text default NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

commands:
virtualenv -p python3 vEnv (creating virtualEnv)
source vEnv/bin/activate (get into the environment)
pip3 install -r requirements.pip (install packages)
install redis and up the redis server


CELERY 
celery -A app.celery.tasks worker --pool=solo --loglevel=info

Testing:
run tests/test.py

NOTE: Please add the data to env.cfg file if you want to change the config

RUN the Application: python3 run.py

CURL:

curl --location --request POST 'http://localhost:8081/customers/upload-document?customer_id=1' \
 -F 'file=@/Users/yashodharnellorepalli/Downloads/invoice_1.pdf'

curl --location --request GET 'http://localhost:8081/customers/document-status?document_id=2'

curl --location --request GET 'http://localhost:8081/customers/digitized-document?document_id=2'

curl --location --request GET 'http://localhost:8081/documents/fetch-documents?document_id=2'

curl --location --request PUT 'http://localhost:8081/documents/update-document' \
--header 'Content-Type: application/json' \
--data-raw '{
    "document_id": 1,
    "invoice_id": "invoice_edit_1"
}'

curl --location --request PUT 'http://localhost:8081/documents/add-field' \
--header 'Content-Type: application/json' \
--data-raw '{
    "document_id": 1,
    "fields": [
        {
            "name": "p1",
            "type": "text",
            "can_be_null": 1,
            "default": ""
        }
    ]
}'

curl --location --request PUT 'http://localhost:8081/documents/modify-field' \
--header 'Content-Type: application/json' \
--data-raw '{
    "document_id": 1,
    "fields": [
        {
            "name": "p1",
            "type": "text",
            "can_be_null": 1,
            "default": ""
        }
    ]
}'