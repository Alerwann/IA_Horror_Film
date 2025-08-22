
def verif_var_int(var):
    """ Vérifie si un str peut être converti en int ou si c'est bien un int"""
    try:
        var_return = int(var)
    except (ValueError, TypeError):
        raise ValueError("La variable doit être un nombre valide")
    return var_return

def verif_order_int(varmin,varmax):
    """ pour deux nombre donnée vérifie leur ordre
        interverti si la valeur minimum est supérieur à la maximum"""
    if varmin > varmax:
        varmin,varmax = varmax,varmin

    return varmin,varmax

def str_strip_lower(var):
    try:
        var_return = var.strip().lower()
    except AttributeError:
        raise ValueError("La variable doit être du type str")
    return var_return