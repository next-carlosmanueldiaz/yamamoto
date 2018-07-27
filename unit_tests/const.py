# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
# DYNAMODB:

# nombre de la tabla en DynamoDB
table_config_name = "nombreTabla"

# Esquema de la tabla en DynamoDB
table_config_schema = [
    {
        'AttributeName': 'keyName',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': "sortKey",
        'KeyType': "RANGE"
    }
]

# Atributos de la tabla en dynamoDB
table_config_attributes = [
    {
        'AttributeName': 'keyName',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'sortKey',
        'AttributeType': 'S'
    }
]

# Registro de ejemplo
config_miscelanea_reg = {
    'keyName': 'MISCELANEA',
    'sortKey': '2018-04-26T00:00:00.000Z',
    'activated': True,
    'frequency': 'DAILY',
    'load_type': 'COPY',
    'num_files': 1,
    'separator': ",",
}