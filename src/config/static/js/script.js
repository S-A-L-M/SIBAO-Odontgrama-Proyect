'use strict';



/**
 * addEvent on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
}



/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const navbarToggler = document.querySelector("[data-nav-toggler]");

const toggleNav = function () {
  navbar.classList.toggle("active");
  navbarToggler.classList.toggle("active");
}

addEventOnElem(navbarToggler, "click", toggleNav);

const closeNav = function () {
  navbar.classList.remove("active");
  navbarToggler.classList.remove("active");
}

addEventOnElem(navbarLinks, "click", closeNav);



/**
 * header active
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

window.addEventListener("scroll", function () {
  if (window.scrollY >= 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
});
// carga la API de Google
gapi.load('client', init);

function init() {
  // inicializa la API de Google con tu CLIENT_ID
  gapi.client.init({
    'apiKey': 'AIzaSyAr6-Qevgfy3lAGZ-8SDVjbHAPCmWKk5MQ',
    'clientId': '887732355759-6qt78dnapfnm1j27b4e34cu6hkcd6fat.apps.googleusercontent.com',
    'discoveryDocs': ['https://www.googleapis.com/discovery/v1/apis/gmail/v1/rest'],
    'scope': 'https://www.googleapis.com/auth/gmail.send'
  }).then(function () {
    // cuando la API de Google está lista, llama a la función sendEmail()
    sendEmail();
  }, function(error) {
    // si hay un error al inicializar la API de Google, muestra un mensaje de error en la consola
    console.error(error);
  });
}

function sendEmail() {
  // obtiene el correo electrónico del usuario del campo de entrada
  var userEmail = document.getElementById('email-input').value;

  // crea el mensaje de correo electrónico
  var message = "To: " + userEmail + "\r\n" +
    "Subject: Confirmación de correo electrónico\r\n\r\n" +
    "¡Gracias por registrarte! Te contactaremos pronto.";

  // codifica el mensaje en Base64 para que pueda ser enviado a través de la API de Gmail
  var encodedMessage = btoa(message);

  // llama a la API de Gmail para enviar el correo electrónico
  var request = gapi.client.gmail.users.messages.send({
    'userId': 'me',
    'resource': {
      'raw': encodedMessage
    }
  });
  request.execute(function(response) {
    // muestra un mensaje de éxito en la consola
    console.log(response);
  });
}