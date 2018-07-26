# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de S3 (con boto3)
usando MOTO para Tests Unitarios
"""
import boto3
from src.test.unit_test.config import config
from moto import mock_s3

"""
s3 con boto3
"""
class s3Commons():
    """
    Constructor de la clase
    Crea el recurso
    """
    def __init__(self):
        self.s3 = None
        self.create_resource()

    """
    Crea un recurso S3 con MOTO
    Implementa patrón singleton, para crear sólo un recurso
    """
    @mock_s3
    def create_resource(self):
        try:
            # Crea el recurso si no existe previamente (singleton)
            if self.s3 is None:
                # Configura una sesión predeterminada, pasando los parámetros necesarios al constructor de la sesión.
                boto3.setup_default_session(region_name=config.region)
                self.s3 = boto3.resource('s3', region_name=config.region)
        except Exception as ex:
            print "[s3Commons][create_resource]" + ex.message

    """
    Crea un bucket de s3
    """
    def create_bucket(self, bucket_name):
        try:
            # crea el bucket si no existe previamente (esta llamada ya es singleton)
            self.s3.create_bucket(Bucket=bucket_name)
        except Exception as ex:
            print "[s3Commons][create_resource]" + ex.message

    """
    Retorna el recurso s3 creado
    """
    def get_resource(self):
        return self.s3

    """
    Retorna el cliente del recurso s3 creado
    """
    def get_client(self):
        return self.s3.meta.client

    """
    Sube un fichero a s3
    """
    def put(self, bucket_name, origen, destino):
        try:
            file = open(origen, "r")
            self.s3.Object(bucket_name, destino).put(Body=file)
        except Exception as ex:
            print ex.message

    """
    Descarga un fichero de s3
    """
    def get(self, bucket_name, origen, destino):
        try:
            # Obtenemos el cliente de el recurso creado
            s3_client = self.s3.meta.client
            s3_client.download_file(bucket_name, origen, destino)
        except Exception as ex:
            print ex.message

    """
    Muestra los archivos de un folder de s3
    """
    def list(self):
        listado = self.s3.meta.client.list_buckets()
        print(listado)