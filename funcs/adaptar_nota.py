def adaptar_nota(nota):
    if nota >= 9.0:
        return "obra-prima"
    elif 9.0 > nota  >= 8.0:
        return "excelente"
    elif 8.0 > nota >= 7.0:
        return "bom"
    elif 7.0 > nota: 
        return "mediano"