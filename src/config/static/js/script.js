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
//APARTADO DE EL CONTAINER DE COOKIES
const cookieContainer = document.querySelector(".cookie-container");
const cookieButton = document.querySelector(".cookie-btn");
const customizeButton = document.querySelector(".customize-btn");
const moreInfoButton = document.querySelector(".more-info-btn");
const cookieTitle = document.querySelector(".cookie-title");
const cookieText = document.querySelector(".cookie-text");
const customizeTitle = document.querySelector(".customize-title");
const customizeText = document.querySelector(".customize-text");
const acceptButton = document.querySelector(".accept-btn");
const acceptAllButton = document.querySelector(".accept-all-btn");
const cancelButton = document.querySelector(".cancel-btn");
const cookieCheckboxes = document.querySelectorAll(".cookie-checkbox");

cookieButton.addEventListener("click", () => {
  cookieContainer.classList.add("active");
});

cancelButton.addEventListener("click", () => {
  cookieContainer.classList.remove("active");
});

customizeButton.addEventListener("click", () => {
  cookieTitle.classList.add("inactive");
  cookieText.classList.add("inactive");
  customizeTitle.classList.add("active");
  customizeText.classList.add("active");
  acceptButton.classList.add("customize");
});

acceptButton.addEventListener("click", () => {
  if (acceptButton.classList.contains("customize")) {
    let cookies = "";
    for (let i = 0; i < cookieCheckboxes.length; i++) {
      if (cookieCheckboxes[i].checked) {
        cookies += cookieCheckboxes[i].name + ",";
      }
    }
    setCookie("acceptedCookies", cookies.slice(0, -1), 30);
    cookieContainer.classList.remove("active");
  } else {
    setCookie("acceptedCookies", "all", 30);
    cookieContainer.classList.remove("active");
  }
});

acceptAllButton.addEventListener("click", () => {
  setCookie("acceptedCookies", "all", 30);
  cookieContainer.classList.remove("active");
});

moreInfoButton.addEventListener("click", () => {
  // Replace this with your own code for displaying more information about cookies
  alert("More information about cookies");
});

function setCookie(name, value, expirationDays) {
  const date = new Date();
  date.setTime(date.getTime() + expirationDays * 24 * 60 * 60 * 1000);
  const expires = "expires=" + date.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
  const cookieName = name + "=";
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i];
    while (cookie.charAt(0) == " ") {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf(cookieName) == 0) {
      return cookie.substring(cookieName.length, cookie.length);
    }
  }
  return "";
}
window.onload = () => {
  const acceptedCookies = getCookie("acceptedCookies");
  if (acceptedCookies === "all") {
    cookieContainer.style.display = "none";
  } else if (acceptedCookies !== "") {
    const acceptedCookieList = acceptedCookies.split(",");
    for (let i = 0; i < cookieCheckboxes.length; i++) {
      if (acceptedCookieList.includes(cookieCheckboxes[i].name)) {
        cookieCheckboxes[i].checked = true;
      }
    }
  }
};

