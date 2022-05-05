import {Prisma} from '../prisma.js';
import {crearPedidoRequersDTO} from '../dtos/pedidos.dto.js';

export const crearPedido = async (req, res) => {
    try {
        const {clienteId} = crearPedidoRequersDTO({clienteId: req.user.id})
        const nuevoPedido = await Prisma.pedido.create({
            data: {
                estado: 'CREADO',
                fecha: new Date(),
                total: 0.00,
                clienteId
            },
            select: {
                id: true
            }
        });
        res.status(201).json({
            message: 'Pedido creado correctamente',
            content: nuevoPedido
        });
    } catch (e) {
        res.status(400).json({
            message: 'Error al crear el pedido',
            content: e.message
        });
    }
}