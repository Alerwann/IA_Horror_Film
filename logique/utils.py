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

    # === Calculs de stats ===


def calculate_proportion_in_percent(valeur_precis, valeur_totale):
    """Calcule la proportion en pourcentage"""
    valeur_precis = verif_var_int(valeur_precis)
    valeur_totale = verif_var_int(valeur_totale)

    if valeur_totale == 0:
        return 0  

    pourcent=  (valeur_precis / valeur_totale) * 100

    return round(pourcent,2)
