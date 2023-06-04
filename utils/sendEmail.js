const nodemailer = require('nodemailer');
const nodemailerConfig = require('./nodemailerConfig');

const sendEmail = async ({ to, subject, html }) => {
  //let testAccount = await nodemailer.createTestAccount();
  const transporter = nodemailer.createTransport(nodemailerConfig);
  return transporter.sendMail({
    from: 'projectpackman@gmail.com', // sender address
    to,
    subject,
    html,
  }, function(error){
    if(error){
      console.log(error);
    }
  });
};

module.exports = sendEmail;
