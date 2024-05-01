preguntas_basicas = {
    'pregunta_1': {'enunciado':['Enunciado básico 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado básico 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado básico 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['Enunciado intermedio 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado intermedio 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado intermedio 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['Enunciado avanzado 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}


if __name__ == '__main__':
    #print(preguntas_basicas['pregunta_1'])
    #{
    #    'enunciado': ['Enunciado básico 1'],#valor tipo lista (va entre corchetes)
    #    'alternativas': [['alt_1',0], ['alt_2',1], ['alt_3',0], ['alt_4',0] ]
    #}
    
    #print(preguntas_basicas['pregunta_1'])
    #print(preguntas_basicas['pregunta_1'] ['enunciado'])
    #print(preguntas_basicas['pregunta_1'] ['enunciado'][0])
    #print(preguntas_basicas['pregunta_1'] ['alternativas'][1][0])
    
    #print(pool_preguntas['basicas'])
    #print(pool_preguntas['basicas']['pregunta_2'])#{'enunciado': ['Enunciado básico 1'],'alternativas': [['alt_1',0], ['alt_2',1], ['alt_3',0], ['alt_4',0]]}
    
    print(pool_preguntas['basicas']['pregunta_2']['enunciado'][0])#enunciado básico 2
    
    print(pool_preguntas['intermedias']['pregunta_1']['alternativas'][0][0])
    
    print(pool_preguntas['avanzadas']['pregunta_3']['alternativas'] [3] [1])
    
    incorrectas = {}
    correctas = {}
    
    for clave, valor in pool_preguntas.items():
        
        if valor == 0:
            print("La alternativa no es correcta") 
            
        
        else:
            print("la alternativa es correcta")  
    
    #(Cómo se puede imprimir o mostrar la alternativa correcta de cada tipo de pregunta, de acuerdo si su valor es 0 o 1... :( ?)    