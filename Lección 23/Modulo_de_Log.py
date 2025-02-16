import logging as log

log.basicConfig(
    level = log.WARNING,
    format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] --> %(message)s',
    datefmt = '%I:%M:%S %p',
    handlers = [
        #log.FileHandler('bitacora.txt'),
        log.StreamHandler()
    ]
)

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')