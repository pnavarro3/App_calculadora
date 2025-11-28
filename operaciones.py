def suma(a, b):
    try:
        return float(a) + float(b)
    except Exception as e:
        raise ValueError("Entradas no numéricas") from e


def resta(a, b):
    try:
        return float(a) - float(b)
    except Exception as e:
        raise ValueError("Entradas no numéricas") from e


def multiplicacion(a, b):
    try:
        return float(a) * float(b)
    except Exception as e:
        raise ValueError("Entradas no numéricas") from e


def division(a, b):
    try:
        a_f = float(a)
        b_f = float(b)
    except Exception as e:
        raise ValueError("Entradas no numéricas") from e
    if b_f == 0.0:
        raise ValueError("Division por cero no permitida")
    return a_f / b_f
def suma(a, b):
	try:
		return float(a) + float(b)
	except Exception as e:
		raise ValueError("Entradas no numéricas") from e


def resta(a, b):
	try:
		return float(a) - float(b)
	except Exception as e:
		raise ValueError("Entradas no numéricas") from e


def multiplicacion(a, b):
	try:
		return float(a) * float(b)
	except Exception as e:
		raise ValueError("Entradas no numéricas") from e


def division(a, b):
	try:
		a_f = float(a)
		b_f = float(b)
	except Exception as e:
		raise ValueError("Entradas no numéricas") from e
	if b_f == 0.0:
		raise ValueError("Division por cero no permitida")
	return a_f / b_f

