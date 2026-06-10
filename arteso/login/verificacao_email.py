def validar_email(email):

    if "@" not in email:
        return False

    partes = email.split("@")
    if len(partes) != 2:
        return False

    usuario, dominio = partes

    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    if email.endswith("."):
        return False

    if dominio.startswith("."):
        return False

    if ".." in email:
        return False

    return True