import {Router} from 'express';
import {validarCliente, verificarToken} from '../utils/validador.js';
import {crearPedido} from '../controllers/pedidos.controllers.js';

export const pedidosRouter = Router();

pedidosRouter
    .route('/pedidos')
    .all(verificarToken, validarCliente)
    .post(crearPedido);