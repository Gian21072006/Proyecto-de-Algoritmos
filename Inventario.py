from Ingredientes import Ingredientes

class Inventario():
    ''' Se encargara de gestionar y manegar losingredientes que esten disponibles para que el 
    cliente tenga un acceso mas rapido a esta informacion
    '''

    def __init__(self):
        
        self.Ingredientes : dict[str, Ingredientes] = {}

    def Buscar_Ingredientes():
        ''' Este metodo permitira al cliente buscar los ingredientes parea su HotDog
        '''
        pass

    def Ver_Ingredientes():
        ''' Este metodo permitira al cliente ver la lista de ingredientes disponibles
        '''
        pass

    def Ingredientes_por_Categoria():
        ''' Este metodo permitira al cliente ver la lista de ingredientes disponibles calificados por su categoria 
        (ejemplo: pan = tipos de panes)
        '''
        pass

    def Actualizar_Existencia():
        ''' Este metodo permitira que la lista de ingredientes se actualice al agotarse la existencia de algun ingrediente 
        '''
        pass