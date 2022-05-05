import jsonwebtoken from 'jsonwebtoken';
import {Prisma} from '../prisma.js';
import prisma from '@prisma/client';

//esta funcion actuara como un middleware
export async function verificarToken(req, res, next) {
    if (!req.headers.authorization) {
        res.status(401).json({
            message: 'Se requiere una token para esta peticion.'
        })
    }
    try {
        const token = req.headers.authorization.split(' ')[1];
        //validar que la contraseña sea correcta, que el token no haya vencido
        const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET);

        //con el paylolad se ubicara a el usuario
        const usuarioEncontrado = await Prisma.usuario.findUnique({
            where: {id: payload.id},
            rejectOnNotFound: true
        })

        req.user = usuarioEncontrado;

        //  hace que se pase a la siguiente accion
        next();

    } catch (e) {
        return res.status(400).json({
            message: "Token invalida",
            content: e.message,
        });
    }
}

export const validarAdmin = async (req, res, next) => {
    if (req.user.rol !== prisma.USUARIO_ROL.ADMINISTRADOR) {
        res.status(401).json({
            message: 'El usuario no tiene los privilegios para realizar esta operacion'
        });
    } else {
        next();
    }
}
export const validarCliente = async (req, res, next) => {
    if (req.user.rol !== prisma.USUARIO_ROL.CLIENTE) {
        res.status(401).json({
            message: 'El usuario no tiene los privilegios para realizar esta operacion'
        });
    } else {
        next();
    }
}