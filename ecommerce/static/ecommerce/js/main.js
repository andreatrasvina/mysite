const hamburguesa = document.querySelector('.hamburguesa');
const enlaces = document.querySelector('.clases-menu');
const iconos = document.querySelector('.iconos-menu');
const cuentas = document.querySelector('.cuenta-menu');
const inicio_sesion = document.querySelector('.container-form');

const bienvenidaTexto = document.querySelector('.texto-container');
const videoJuegos = document.querySelector('.juegos-container');

const barras = document.querySelectorAll('.hamburguesa span')


hamburguesa.addEventListener('click', ()  =>{
    enlaces.classList.toggle('activado');
    iconos.classList.toggle('activado');
    cuentas.classList.toggle('activado');
    //inicio_sesion.classList.toggle('activado');

    barras.forEach(child => {child.classList.toggle('animado')})

    bienvenidaTexto.classList.toggle('oculto');
    videoJuegos.classList.toggle('oculto');
})


