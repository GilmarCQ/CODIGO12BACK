import {Router} from 'express';
import {confirmarCuenta, crearUsuario, login, perfil} from '../controllers/usuarios.controllers.js';
import {verificarToken} from '../utils/validador.js';

export const usuarioRouter = Router();

usuarioRouter.route('/registro').post(crearUsuario);
usuarioRouter.route('/login').post(login);
usuarioRouter.route('/confirmar-cuenta').post(confirmarCuenta);
usuarioRouter.get('/perfil', verificarToken, perfil);
