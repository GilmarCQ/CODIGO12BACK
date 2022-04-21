from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class SoloAdminPuedeEscribir(BasePermission):
    message = 'Este usuario no tiene permisos'
    code = 200

    def has_permission(self, request: Request, view):
        # view  >   es la vista desde la cual se ejecuta la peticion
        # Middlewares > intermediario entre una peticion y la logica final
        # request brindara la informacion de la peticion
        # los custom permission siempre deben devolver True o False, para indicar si cumple con los permisos
        # determinados
        # request.user  >   info del usuario autenticado
        # print(request)
        # print(request.user)
        # print(request.user.nombre)
        # print(request.user.rol)
        # print(request.auth)

        # if str(type(view)) == "<class 'menu.views.StockApiView'>":
        #     validando si la vista es StockApiView, asi aplicar una validacion propia para dicha vista

        # Version con operador ternario
        # return True if request.method in SAFE_METHODS else request.user.rol == 'ADMINISTRADOR'

        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.rol == 'ADMINISTRADOR'

class SoloMozoPuedeEscribir(BasePermission):
    message = 'Este usuario no tiene permisos'
    code = 200
    def has_permission(self, request: Request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.rol == 'MOZO'
