# -*- coding: utf-8 -*-
"""

"""
import io
import datetime
import zipfile


"""
Establece el nombre del fichero de cabecera con la fecha actual
"""
def get_nombre_fichero_cabecera_actual():
    now = datetime.datetime.now()
    fecha_actual = now.strftime("%Y%m%d")
    fcabecera = 'ES_D_CABECERA_' + fecha_actual + '.cab.gz'
    return fcabecera

"""
Comprime el código en un zip para ser agregado a la lambda
"""
def _process_lambda(func_str):
    zip_output = io.BytesIO()
    zip_file = zipfile.ZipFile(zip_output, 'w', zipfile.ZIP_DEFLATED)
    zip_file.writestr('lambda_function.py', func_str)
    zip_file.close()
    zip_output.seek(0)
    return zip_output.read()


def get_test_zip_file1():
    pfunc = """
def lambda_handler(event, context):
    return event
"""
    return _process_lambda(pfunc)
