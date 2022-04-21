from .models import Plato, Stock
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .serializers import (PlatoSerializer,
                          StockSerializer,
                          PedidoSerializer,
                          AgregarDetallePedidoSerializer,
                          StockCreateSerializer)
from rest_framework.permissions import (
    AllowAny,  # sirve para para que el controlador sea unico, no necesite token
    IsAuthenticated,  # Los controladores solicitan un token de acceso
    IsAuthenticatedOrReadOnly,  # para el metodo GET no solicitara token, para las demas si
    IsAdminUser,  # Verifica que en el token de acceso sea de un super_user,
    SAFE_METHODS
)
from rest_framework.request import Request
from rest_framework.response import Response
from cloudinary import CloudinaryImage
from .permissions import SoloAdminPuedeEscribir, SoloMozoPuedeEscribir
from fact_electr.models import Pedido, DetallePedido
from rest_framework import status
from django.utils import timezone
from django.db import transaction, IntegrityError


class PlatoApiView(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
    # lista los permisos necesarios para poder realizar la peticion
    permission_classes = [
        IsAuthenticatedOrReadOnly, SoloAdminPuedeEscribir
    ]

    def get(self, request: Request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        for plato in data.data:
            link = CloudinaryImage(plato.get('foto')).image(secure=True)
            print(link)
        # link = CloudinaryImage(data.data[2].get('foto')).image(secure=True)
        # print(link)
        # print(data.data[2].get('foto'))
        return Response(data=data.data)


class StockApiView(ListCreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [
        IsAuthenticated, SoloAdminPuedeEscribir
    ]

    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return StockCreateSerializer
        return StockSerializer


class PedidoApiView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, SoloMozoPuedeEscribir]

    def post(self, request: Request):
        print(request.user)
        request.data['usuarioId'] = request.user.id
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data=data.data, status=status.HTTP_201_CREATED)


class AgregarDetallePedidoApiView(CreateAPIView):
    serializer_class = AgregarDetallePedidoSerializer
    queryset = Pedido.objects.all()

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        stock = Stock.objects.filter(fecha=timezone.now(),
                                     platoId=data.validated_data.get('platoId'),
                                     cantidad__gte=data.validated_data.get('cantidad')).first()
        print(stock)
        # validacion de stock
        if stock is None:
            return Response(data={
                'message': 'No hay stock para este producto el día de hoy.'
            })
        # validacion del pedido
        pedido: Pedido | None = Pedido.objects.filter(
            id=data.validated_data.get('pedidoId')).first()
        if pedido is None:
            return Response(data={'message': 'No hay ese pedido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                # guardar el detalle pedido
                # cuando se agrega un nuevo registro con relaciones (FK), no solo se debe coloar el id, para ello
                # se debe colocar la instanciua completa del modelo
                nuevoDetalle = DetallePedido(cantidad=data.validated_data.get('cantidad'),
                                             stockId=stock,
                                             pedidoId=pedido)
                stock.cantidad = stock.cantidad - nuevoDetalle.cantidad
                stock.save()
                # modificacion de la cabecera
                pedido.total = pedido.total + (nuevoDetalle.cantidad * stock.precio_diario)
                pedido.save()
        #         si no hay ningun error y se llega al final del try, automaticamente se hara el COMMIT
        except IntegrityError:
            # se genera un rollback automaticamente
            return Response(data={'message': 'Todo quedo como estaba, no se hizo nothing.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data={
            'message': 'Detalle agregado correctamente'
        })
