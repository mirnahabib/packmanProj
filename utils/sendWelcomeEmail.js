const sendEmail = require('./sendEmail');

const sendWelcomeEmail = async ({ name, email}) => {
    const message =`<h4>Hello, ${name}<h4><br>
        <p>Thank you for joining us! \n
        You'll be receiving email updates of price changes on your wishlist items.</p>\n
        <p>Stay tuned for more updates from PACKMAN.</p>`;

    return sendEmail({
        to: email,
        subject: 'THANK YOU FOR JOINING PACKMAN!',
        html: `${message}`,
        });
}
module.exports = sendWelcomeEmail;

