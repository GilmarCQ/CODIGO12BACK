import {Prisma} from '../prisma.js'

export const crearProducto = async (req, res) => {
    try {
        const nuevoProducto = await Prisma.producto.create({data: req.body})
        console.log(nuevoProducto)
        res.json({
            message: 'Producto agregado correctamente.',
            content: nuevoProducto
        })
    } catch (e) {
        res.json({
            message: 'Error al crear el producto.'
        })
    }
}
export const listarProductos = async (req, res) => {
    try {
        const productos = await Prisma.producto.findMany({});
        res.json({
            message: 'Consulta exitosa',
            content: productos
        })
    } catch (e) {
        res.json({
            message: 'Error al listar los productos.'
        })
    }
}
export const actualizarProducto = async (req, res) => {
    const {id} = req.params;
    try {
        const productoEncontrado = await Prisma.producto.findUnique({
            where: {id: +id},
            rejectOnNotFound: true
        });
        const productoActualizado = await Prisma.producto.update({
            data: req.body,
            where: {id: productoEncontrado.id}
        });
        res.json({
            message: 'Producto actualizado correctamente.',
            content: productoActualizado
        })
    } catch (e) {
        console.log(e);
        res.json({
            message: 'Error al actualizar el producto.'
        })
    }

}
export const eliminarProducto = async (req, res) => {
    const {id} = req.params;
    try {
        const productoEncontrado = await Prisma.producto.findUnique({
            where: {id: +id},
            select: {id: true},
            rejectOnNotFound: true
        })
        await Prisma.producto.delete({where: {id: productoEncontrado.id}});
        res.json({
            message: 'Producto eliminado correctamente.'
        })
    } catch (e) {
        res.json({
            message: 'Ha ocurrido un error al eliminar el producto.'
        })
    }
}