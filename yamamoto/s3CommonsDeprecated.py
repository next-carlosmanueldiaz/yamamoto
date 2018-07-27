# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de s3 con boto
usando MOTO para Tests Unitarios
"""
import boto
from boto.s3.key import Key as Key_Boto_s3
# from moto import mock_s3_deprecated

"""
DynamoDB

Para usar esta clase es necesario que se agregue 
el decorador @mock_s3_deprecated de moto en el test donde se use
"""
class s3CommonsDeprecated():
    def __init__(self):
        """
        Constructor de la clase
        Crea el recurso
        """
        self.s3 = None
        self.create_conn()

    def create_conn(self):
        """
        Crea un recurso S3 con MOTO usando boto
        Implementa patrón singleton, para crear sólo un recurso
        :return: None
        """
        try:
            # conexion a s3 con el método predeterminado en boto.
            if self.s3 is None:
                self.s3 = boto.connect_s3()
        except Exception as ex:
            print "[s3CommonsDeprecated][create_resource]" + ex.message

    def create_bucket(self, s3d_bucket_name):
        """
        Crea un bucket de s3
        :param s3d_bucket_name: nombre del bucket a crear
        :return: None
        """
        try:
            # crea un  bucket dentro del s3 conecta
            self.s3.create_bucket(s3d_bucket_name)
        except Exception as ex:
            print "[s3CommonsDeprecated][create_bucket]" + ex.message

    def get_bucket(self, s3d_bucket_name):
        """
        Retorna el cliente del recurso s3 creado
        :param s3d_bucket_name:
        :return:
        """
        try:
            return self.s3.get_bucket(s3d_bucket_name)
        except Exception as ex:
            print "[s3CommonsDeprecated][get_bucket] " + ex.message

    def put(self, s3d_bucket_name, origen, destino):
        """
        Sube un fichero a s3
        :param s3d_bucket_name: Nombre del fichero a subir
        :param origen: ruta y fichero local del archivo a subir
        :param destino: ruta y fichero del bucket donde se dejará el archivo
        :return: None
        """
        try:
            bucketobj = self.s3.get_bucket(s3d_bucket_name)
            k = Key_Boto_s3(bucketobj)
            k.key = destino
            k.set_contents_from_filename(origen)
        except Exception as ex:
            print "[s3CommonsDeprecated][PUT] " + ex.message
