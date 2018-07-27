# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de S3 (con boto3)
usando MOTO para Tests Unitarios
"""
import boto3
from config import config
# from moto import mock_s3

"""
s3 con boto3

Para usar esta clase es necesario que se agregue 
el decorador @mock_s3 de moto en el test donde se use
"""
class s3Commons():
    """
    Constructor de la clase
    Crea el recurso
    """
    def __init__(self):
        self.s3 = None
        self.create_resource()

    def create_resource(self):
        """
        Crea un recurso S3 con MOTO
        Implementa patrón singleton, para crear sólo un recurso
        :return: None
        """
        try:
            # Crea el recurso si no existe previamente (singleton)
            if self.s3 is None:
                # Configura una sesión predeterminada, pasando los parámetros necesarios al constructor de la sesión.
                boto3.setup_default_session(region_name=config.region)
                self.s3 = boto3.resource('s3', region_name=config.region)
        except Exception as ex:
            print "[s3Commons][create_resource]" + ex.message

    def create_bucket(self, bucket_name):
        """
        Crea un bucket de s3
        :param bucket_name: nombre del bucket a crear
        :return: None
        """
        try:
            # crea el bucket si no existe previamente (esta llamada ya es singleton)
            self.s3.create_bucket(Bucket=bucket_name)
        except Exception as ex:
            print "[s3Commons][create_resource]" + ex.message

    def get_resource(self):
        """
        Retorna el recurso s3 creado
        :return: objeto bucket
        """
        return self.s3

    def get_client(self):
        """
        Retorna el cliente del recurso s3 creado
        :return: objeto client
        """
        return self.s3.meta.client

    def put(self, bucket_name, origen, destino):
        """
        Sube un fichero a s3
        :param bucket_name: Nombre del bucket donde se va a subir el fichero
        :param origen: ruta y fichero local del archivo a subir
        :param destino: ruta y fichero del bucket donde se dejará el archivo
        :return: None
        """
        try:
            file = open(origen, "r")
            self.s3.Object(bucket_name, destino).put(Body=file)
        except Exception as ex:
            print ex.message

    def get(self, bucket_name, origen, destino):
        """
        Descarga un fichero de s3
        :param bucket_name: Nombre del bucket de donde se descargará el fichero
        :param origen: ruta y fichero del bucket donde se encuentra el fichero
        :param destino: ruta y fichero del bucket donde se descargará el fichero
        :return: None
        """
        try:
            # Obtenemos el cliente de el recurso creado
            s3_client = self.s3.meta.client
            s3_client.download_file(bucket_name, origen, destino)
        except Exception as ex:
            print ex.message

    def list(self):
        """
        Retorna la lista de buckets de s3
        :return: retorna el listado de buckets de s3
        """
        listado = self.s3.meta.client.list_buckets()
        return listado