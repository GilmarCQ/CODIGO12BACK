import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    auth: {
        user: process.env.EMAIL_ACCOUNT,
        pass: process.env.EMAIL_PASSWORD
    }
});

export const enviarCorreoValidacion = async ({destinatario, hash}) => {
    const html = `
    <p>
        Hola para comenzar a disfrutar de todas las ofertas en nuestro Minimarket, por favor haz click en el siguiente enlace   
            <a href="${process.env.FRONTEND_URL}?hash=${hash}">
                Valida mi cuenta. 
            </a>
    </p>`;
    try {
        await transporter.sendMail({
            from: 'gacampanaq@gmail.com',
            to: destinatario,
            subject: 'Validación creacion de correo Minimarket',
            html
        });
        console.log('Correo enviado correctamente.');
    } catch (e) {
        console.log(e);
        return e;
    }
}