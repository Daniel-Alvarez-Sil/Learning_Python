# Módulo para manejar los mensajes de la bítacora

import logging as log

log.basicConfig(
    level = log.INFO,
    format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] --> %(message)s',
    datefmt = '%I:%M:%S %p',
    handlers = [
        #log.FileHandler('Bítacora_de_Operaciones.txt')
        log.StreamHandler()
    ]
)

if __name__ != '__main__':
    log.info(f'{__name__} ha sido importado con éxito')
