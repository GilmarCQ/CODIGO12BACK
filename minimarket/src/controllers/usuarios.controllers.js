import {Prisma} from '../prisma.js';
import {confirmarCuentaDTO, loginRequestDTO, usuarioRequestDTO} from '../dtos/usuarios.dtos.js';
import {hashSync, compareSync} from 'bcrypt';
import jsonwebtoken from 'jsonwebtoken';
import {enviarCorreoValidacion} from '../utils/sendMail.js';
import cryptojs from 'crypto-js';

export const crearUsuario = async (req, res) => {
    try {
        const data = usuarioRequestDTO(req.body);
        const password = hashSync(data.password, 10);
        const nuevoUsuario = await Prisma.usuario.create({
            data: {...data, password},
            select: {
                id: true,
                nombre: true,
                email: true,
                rol: true,
                validado: true
            }
        });

        const hash = cryptojs.AES.encrypt(
            JSON.stringify({
                nombre: nuevoUsuario.nombre,
                email: nuevoUsuario.email
            }),
            process.env.LLAVE_ENCRIPTACION
        ).toString();

        await enviarCorreoValidacion({
            destinatario: nuevoUsuario.email,
            hash
        });
        res.status(201).json({
            message: 'Usuario creado correctamente.',
            content: nuevoUsuario
        })
    } catch (e) {
        if (e instanceof Error) {
            res.status(400).json({
                message: 'Error al crear el usuario',
                content: e.message
            })
        }
    }
}
export const login = async (req, res) => {
    try {
        const data = loginRequestDTO(req.body);
        const usuarioEncontrado = await Prisma.usuario.findUnique({
            where: {email: data.email},
            rejectOnNotFound: true
        });
        //Validacion del password
        if (compareSync(data.password, usuarioEncontrado.password)) {
            const token = jsonwebtoken.sign(
                {
                    id: usuarioEncontrado.id,
                    mensaje: 'API de minimarket'
                },
                process.env.JWT_SECRET,
                {expiresIn: '1h'}
            );
            res.json({
                message: 'Bienvenido',
                token
            })
        } else {
            throw Error('Credenciales incorrectas.');
        }
    } catch (e) {
        res.status(400).json({
            message: 'Error al iniciar sesion.',
            content: e.message
        })
    }
}
export const confirmarCuenta = async (req, res) => {
    try {
        const data = confirmarCuentaDTO(req.body)
        const informacion = JSON.parse(cryptojs.AES.decrypt(
            data.hash,
            process.env.LLAVE_ENCRIPTACION
        ).toString(cryptojs.enc.Utf8));
        const usuarioEncontrado = await Prisma.usuario.findFirst({
            where: {
                email: informacion.email,
                validado: false
            },
            select: {
                id: true
            }
        })
        if (!usuarioEncontrado) {
            throw new Error('El usuario ya fue validado.');
        }
        await Prisma.usuario.update({
            where: {id: usuarioEncontrado.id},
            data: {validado: true}
        })
        res.json({
            message: 'Cuenta Validada correctamente'
        })
    } catch (e) {
        if (e instanceof Error) {
            res.status(400).json({
                message: 'Error al validar la cuenta.',
                content: e.message
            })
        }
    }
}

export const perfil = (req, res) => {
    console.log(req.user);
    res.json({
        message: 'Bienvenido',
        content: req.user
    });
}