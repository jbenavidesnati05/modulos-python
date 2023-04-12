import mod 
data = [
        {
        'country':'colombia',
        'poblacion':300
        },
        {
        'country':'peru',
        'poblacion':500
        },
    ]
def run():
    keys, values =  mod.getPoblacion()
    print(keys,values)


    country = input

    result = mod.poblacionPais(data, 'colombia')
    print(result)