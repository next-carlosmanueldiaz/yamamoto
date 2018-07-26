# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de DynamoDB
usando MOTO para Tests Unitarios
"""
import boto3
from boto3.dynamodb.conditions import Key as Key_boto3_dynamodb
from src.test.unit_test.config import config, const
from moto import mock_dynamodb2

"""
DynamoDB
"""
class dynCommons():
    """
    Constructor de la clase
    Crea el recurso
    """
    def __init__(self):
        self.dyn = None
        self.table_name = None
        self.table = None
        self.create_resource()

    """
    Crea el recurso con boto3 mockeado con moto
    """
    @mock_dynamodb2
    def create_resource(self):
        try:
            if self.dyn is None:
                self.dyn = boto3.resource('dynamodb', config.region)
        except Exception as ex:
            print "[dynCommons][create_resource]" + ex.message

    """
    Crea una tabla de dynamoDB pasándole nombre de tabla, esquema y atributos
    """
    def create_table(self, tablename, schema, attributes):
        try:
            self.dyn.create_table(
                TableName=tablename,
                KeySchema=schema,
                AttributeDefinitions=attributes,
                ProvisionedThroughput = {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            # Inicializamos la tabla para usarla
            self.table_name = tablename
            self.table_init()
        except Exception as ex:
            print "[dynCommons][create_table]" + ex.message

    """
    Prepara la tabla para ser usada
    """
    def table_init(self):
        try:
            self.table = self.dyn.Table(self.table_name)
        except Exception as ex:
            print "[dynCommons][table_init]" + ex.message

    """
    Inserta un registro en la tabla
    """
    def put_item(self, reg):
        try:
            self.table_init()
            self.table.put_item(Item=reg)
        except Exception as ex:
            print "[dynCommons][put_item]" + ex.message

    """
    Establece el valor de un campo
    """
    def set_value(self, key, val):
        try:
            self.table = self.table_init(self.table_name)
            self.table[key] = val
        except Exception as ex:
            print "[dynCommons][set_value]" + ex.message

    """
    Realiza una consulta
    """
    def table_query(self, field_name, value):
        results = self.table.query(
            KeyConditionExpression=Key_boto3_dynamodb(field_name).eq(value)
        )
        return results