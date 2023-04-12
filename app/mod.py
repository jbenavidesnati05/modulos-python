
def getPoblacion ():
    keys = ['col','bol']
    values = [300,400]
    return keys,values

def poblacionPais(data, country):
    result = list(filter(lambda item: item['country']== country , data))
    return result

