import express, {json} from 'express';
import {productosRouter} from './routes/productos.routes.js';
import {usuarioRouter} from './routes/usuario.routes.js';
import cors from 'cors';
import {pedidosRouter} from './routes/pedidos.routes.js';
import {detallePedidoRouter} from './routes/detallePedido.routes.js';
import mercadopago from 'mercadopago';
import {pagosRouter} from './routes/pagos.routes.js';

const app = express();

//son las credenciales que van a servir para realizar la pasarela de pago
//  el integrator_id, id del desarrollador que esta aplicando la pasarela
//  access-token, token creada al generar una nueva integracion y sera la encargada de cuando se
//  pague algo de ese dinero sera redirigido a la empresa
mercadopago.configure({
    access_token: process.env.MP_ACCESS_TOKEN,
    integrator_id: process.env.MP_INTEGRATOR_ID
});

app.use(json())

//  nullish coalescing
//  si el primer valor no es nulo o undefined tomara este valor, caso contrario tomara el segundo valor
const PORT = process.env.PORT ?? 3000;

app.get('/', (req, res) => {
    res.json({
        message: 'Bienvenido al API de Minimarket.'
    })
})
//  bloque de rutas
app.use(productosRouter)
app.use(usuarioRouter)
app.use(pedidosRouter)
app.use(detallePedidoRouter)
app.use(pagosRouter)

app.use(cors())

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
})