import logging

# Configurar logging para registrar operaciones en `log.txt`
logging.basicConfig(
	filename='log.txt',
	level=logging.INFO,
	format='%(asctime)s %(levelname)s: %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def suma(a, b):
	try:
		a_f = float(a)
		b_f = float(b)
		result = a_f + b_f
		logger.info('suma: a=%s b=%s result=%s', a, b, result)
		return result
	except Exception as e:
		logger.exception('suma falló para a=%s b=%s', a, b)
		raise ValueError('Entradas no numéricas') from e


def resta(a, b):
	try:
		a_f = float(a)
		b_f = float(b)
		result = a_f - b_f
		logger.info('resta: a=%s b=%s result=%s', a, b, result)
		return result
	except Exception as e:
		logger.exception('resta falló para a=%s b=%s', a, b)
		raise ValueError('Entradas no numéricas') from e


def multiplicacion(a, b):
	try:
		a_f = float(a)
		b_f = float(b)
		result = a_f * b_f
		logger.info('multiplicacion: a=%s b=%s result=%s', a, b, result)
		return result
	except Exception as e:
		logger.exception('multiplicacion falló para a=%s b=%s', a, b)
		raise ValueError('Entradas no numéricas') from e


def division(a, b):
	try:
		a_f = float(a)
		b_f = float(b)
	except Exception as e:
		logger.exception('division falló al convertir entradas a números: a=%s b=%s', a, b)
		raise ValueError('Entradas no numéricas') from e
	if b_f == 0.0:
		logger.error('division por cero intentada: a=%s b=%s', a, b)
		raise ValueError('Division por cero no permitida')
	result = a_f / b_f
	logger.info('division: a=%s b=%s result=%s', a, b, result)
	return result


