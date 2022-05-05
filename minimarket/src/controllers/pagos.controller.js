import mercadopago from 'mercadopago';
import {Prisma} from '../prisma.js';

export const crearPreferencia = async (req, res) => {
    try {
        const {pedidoId} = req.body;
        const pedidoEncontrado = await Prisma.pedido.findUnique({
            where: {id: pedidoId},
            rejectOnNotFound: true,
            include: {
                cliente: true,
                detallePedidos: {include: {producto: true}}
            }
        })
        // console.log(pedidoEncontrado);
        const preferencia = await mercadopago.preferences.create({
            auto_return: "approved",
            back_urls: {
                failure: "http://localhost:3000/pago-fallido",
                pending: "http://localhost:3000/pago-pendiente",
                success: "http://localhost:3000/pago-exitoso",
            },
            metadata: {
                nombre: "Prueba",
            },
            payer: {
                name: pedidoEncontrado.cliente.nombre,
                // surname: "De Rivero",
                // address: {
                //     zip_code: "04002",
                //     street_name: "Calle Los Girasoles",
                //     street_number: 105,
                // },
                email: "test_user_46542185@testuser.com",
            },
            items: pedidoEncontrado.detallePedidos.map((detallePedido) => ({
                id: detallePedido.productoId,
                currency_id: 'PEN',
                title: detallePedido.producto.nombre,
                quantity: detallePedido.cantidad,
                unit_price: detallePedido.producto.precio
            })),
            // [
            //     {
            //         id: "1234",
            //         category_id: "456",
            //         currency_id: "PEN",
            //         description: "Zapatillas de Outdoor",
            //         picture_url: "https://imagenes.com",
            //         quantity: 1,
            //         title: "Zapatillas edicion Otoño",
            //         unit_price: 75.2,
            //     },
            // ],
            notification_url: 'https://f44e-2800-200-f410-1d44-8092-313d-1ba9-fa84.ngrok.io/mp-webhooks'
        });
        // console.log(preferencia);

        await Prisma.pedido.update({
            data: {
                process_id: preferencia.body.id,
                estado: 'CREADO'
            },
            where: {
                id: pedidoId
            }
        })

        res.json({
            message: 'Preferencia generada exitosamente',
            content: preferencia
        })
    } catch
        (e) {
        res.json({
            message: 'Error al crear la preferencia',
            error: e.message
        })
    }
}
export const MercadoPagoWebhooks = async (req, res) => {
    console.log('__body__')
    console.log(req.body)

    console.log('__params__')
    console.log(req.params)

    console.log('__headers__')
    console.log(req.headers)

    console.log('__queryparams__')
    console.log(req.query)

    if (req.query.topic === 'merchant_order') {
        const {id} = req.query;
        // https://api.mercadolibre.com/merchant_orders/{id}
        const orden_comercial = await mercadopago.merchant_orders.get(id);
        console.log('La orden es:')
        console.log(orden_comercial)

        const pedido = await Prisma.pedido.findFirst({
            where: {
                process_id: orden_comercial.body.preference_id
            }
        })
        if(!pedido) {
            //  aca se enviara un correo para que se realize una validación manual del porque no se encuentra el pago
            console.log('Pedido incorrecto')
        }
        if (orden_comercial.body.order_status === 'paid') {
            //cambiamos el estado del pedido a pagado
            await Prisma.pedido.updateMany({
                data: { estado: 'PAGADO' },
                where: { process_id: orden_comercial.body.preference_id }
            })
        }
    }

    res.status(201).json({
        message: 'Webhooks recibido correctamente'
    })
}