//  Usando ECMAScript   ->  type: module
import express from 'express';
import cors from 'cors';

//  Usando CommonJs     ->  type: CommonJs
// const express = require('express')
const servidor = express();

//  middleware que define el formato en que se puede recibir y entender a un formato JSON
servidor.use(express.json())
servidor.use(express.raw())
servidor.use(express.urlencoded({extended: true}))
//  al agregar una regla de cors, el puerto de la ip no importa, se permite todo el dominio
//  Por defecto el metodo GET, siempre se podra realizar
servidor.use(cors({
    origin: ['http://127.0.0.1'],
    methods: ['POST', 'PUT', 'DELETE'],  //  (*), permite todos los metodos
    allowedHeaders: ['Content-Type', 'Authorization'],  //  (*), permite cualquier header
}))

const productos = [
    {
        nombre: 'platano',
        precio: 1.80,
        disponible: true
    }
]

servidor.get('/', (req, res) => {
    const data = productos
    res.status(200).json({
        data
    })
})


servidor.post('/crear-producto', (req, res) => {
    console.log(req.body)
    const data = req.body;
    productos.push(data)
    return res.status(201).json({
        message: 'Producto agregado correctamente'
    })
})

servidor
    .route('/producto/:id')
    .get((req, res) => {
        console.log(req.params);
        const {id} = req.params;
        if (productos.length >= id) {
            res.status(200).json(200, {
                data: productos[id - 1]
            })
        } else {
            res.status(401).json({
                message: 'No se encontro el producto'
            })
        }
    })
    .put((req, res) => {
    console.log(req.params);
    const {id} = req.params;
    const producto = req.body;
    if (productos.length >= id) {
        productos[id-1] = producto
        res.status(200).json(200, {
            message: 'Producto editado correctamente'
        })
    } else {
        res.status(400).json({
            message: 'No se encontro el producto'
        })
    }
})
    .delete((req, res) => {
        const {id} = req.params;
        if (productos.length >= id) {
            productos.splice(id - 1 , 1)
            res.status(200).json(200, {
                message: 'Producto eliminado correctamente'
            })
        } else {
            res.status(400).json({
                message: 'No se encontro el producto'
            })
        }
    })

servidor.listen(3000, () => {
    console.log('Servidor corriendo exitosamente en el puerto 3000');
});
