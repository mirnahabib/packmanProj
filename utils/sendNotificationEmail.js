const sendEmail = require('./sendEmail');

const sendNotificationEmail = async ({ name, email, link }) => {
    const message =`<h4>Hello, ${name}<h4><br>
        <p>This automated email was sent to inform you that <b>one of your wishlist item price has changed!</b>\n
        You can visit our <a href="https://packman-api.vercel.app/">website</a> to checkout the price changes, or you can check your item <a href="${link}">here</a>!</p>
        <p>Stay tuned for more updates from PACKMAN.</p>`;

    return sendEmail({
        to: email,
        subject: 'Price update from PACKMAN!',
        html: `${message}`,
        });
}
module.exports = sendNotificationEmail;

