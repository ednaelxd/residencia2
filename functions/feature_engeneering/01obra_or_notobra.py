def define_obra(data):
    
    result = data.Objeto.str.contains("OBRAS|OBRA|obras|obra|ENGENHARIA|engenharia|CONSTRU-CAO|constru-cao", na=False)
    
    return (result.replace({True:'Obra',False:'Compras/Servicos'}))
