from Ingredientes import Ingredientes

class HotDog():
    ''' Donde van a estar los HotDogs, y donde cada uno tendra indicado su receta 
    '''

    def __init__(self, nombre : str):
        
        self.Ingredientes : dict[str, Ingredientes] = {}
        self.nombre = nombre

    def Agregar():
        ''' Este metodo permitira crear y registrar una nueva receta de Hot Dog
        '''
        pass

    def Eliminar():
        ''' Este metodo permitira eliminar recetas de Hot Dog
        '''
        pass

    def Validar_Inventario():
        ''' Este metodo permitira la validacion del inventario (si se tienen los ingredientes para hacer
        el Hot Dog)
        '''
        pass

    def Ver_Detalles():
        ''' Este metodo permitira revisar detalladamente cada Hot Dog y de que estan hechos
        '''