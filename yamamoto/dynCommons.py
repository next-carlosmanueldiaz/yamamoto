# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de DynamoDB
usando MOTO para Tests Unitarios
"""
import boto3
from boto3.dynamodb.conditions import Key as Key_boto3_dynamodb
from config import config
# from moto import mock_dynamodb2

"""
DynamoDB

Para usar esta clase es necesario que se agregue 
el decorador @mock_dynamodb2 de moto en el test donde se use
"""
class dynCommons():

    def __init__(self):
        """
        Constructor de la clase
        Crea el recurso
        """
        self.debug = False
        self.dyn = None
        self.table_name = None
        self.table = None
        self.create_resource()

    def create_resource(self):
        """
        Crea el recurso con boto3 mockeado con moto
        :return: None
        """
        try:
            if self.dyn is None:
                self.dyn = boto3.resource('dynamodb', config.region)
                if self.debug: print('[dynCommons][INFO][create_resource] Recurso DynamoDB creado correctamente')
        except Exception as ex:
            print "[dynCommons][ERROR][create_resource]" + ex.message

    def create_table(self, tablename, schema, attributes):
        """
        Crea una tabla de dynamoDB pasándole nombre de tabla, esquema y atributos
        :param tablename:
        :param schema:
        :param attributes:
        :return: None
        """
        try:
            self.table_name = tablename
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
            if self.debug: print('[dynCommons][INFO][create_table] Tabla DynamoDB creada correctamente.')
            self.table_init()
        except Exception as ex:
            print "[dynCommons][ERROR][create_table]" + ex.message

    def table_init(self):
        """
        Prepara la tabla para ser usada
        :return: None
        """
        try:
            self.table = self.dyn.Table(self.table_name)
        except Exception as ex:
            print "[dynCommons][ERROR][table_init]" + ex.message

    def put_item(self, reg):
        """
        Inserta un registro en la tabla
        :param reg: Json con el registro a insertar
        :return: None
        """
        try:
            self.table_init()
            self.table.put_item(Item=reg)
            if self.debug: print('[dynCommons][INFO][create_table] Registro insertado correctamente.')
        except Exception as ex:
            print "[dynCommons][ERROR][put_item]" + ex.message

    def set_value(self, key, val):
        """
        Establece el valor de un campo
        :param key: clave a modificar
        :param val: nuevo valor a insertar
        :return: None
        """
        try:
            self.table = self.table_init(self.table_name)
            self.table[key] = val
        except Exception as ex:
            print "[dynCommons][ERROR][set_value]" + ex.message

    def table_query(self, field_name, value):
        """
        Realiza una consulta
        :param field_name: campo a consultar
        :param value: valor del campo a consultar
        :return: resultado de la consulta ejecutada
        """
        try:
            results = self.table.query(
                KeyConditionExpression=Key_boto3_dynamodb(field_name).eq(value)
            )
            return results
        except Exception as ex:
            print "[dynCommons][ERROR][table_query]" + ex.message