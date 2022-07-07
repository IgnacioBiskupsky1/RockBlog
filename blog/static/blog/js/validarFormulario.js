var nombre = document.getElementById('nombre');
var correo = document.getElementById('correo');
var contrasena = document.getElementById('contrasena');
var confirmarContrasena = document.getElementById('confirmarContrasena');
var asunto = document.getElementById('asunto');
var mensaje = document.getElementById('mensaje');


var error = document.getElementById('error');



//function validarRegistro() {
//  console.log('Enviando formulario...')
//
//   var mensajeError = [];
//
// if (nombre.value === null || nombre.value === '') {
//      mensajeError.push('Ingresa tu nombre');
//   }
//
//  if (correo.value === null || correo.value === '') {
//     mensajeError.push('Ingresa correo');
//  }
//
//  if (contrasena.value === null || contrasena.value === '') {
//       mensajeError.push('Ingresa contraseña');
//    }
//
//    if (confirmarContraseña.value === null || confirmarContraseña.value === '') {
// mensajeError.push('Confirme la contraseña');
//}
//if (confirmarContraseña.value != contrasena) {
//    mensajeError.push('La contraseña debe ser identica');
//  }
//
//if (form.confirmarContraseña.value != form.contraseña.value) {
//    mensajeError.push('Ingresa tu nombre');
//  }
//
//  error.innerHTML = mensajeError.join(',');
//    return false;
// }


var formRegistro = document.getElementById('formularioRegistro');
form.addEventListener('submit', function(evt) {
    evt.preventDefault();
    var mensajeError = [];

    if (nombre.value === null || nombre.value === '') {
        mensajeError.push("Ingrese tu nombre ");
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (correo.value === null || correo.value === '') {
        mensajeError.push('Ingrese correo');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (contrasena.value === null || contrasena.value === '') {
        mensajeError.push('Ingrese contraseña');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (confirmarContrasena.value === null || confirmarContrasena.value === '') {
        mensajeError.push('Confirme la contraseña');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }
    if (confirmarContrasena.value !== contrasena.value) {
        mensajeError.push('La contraseña debe ser idéntica');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }




});



//function validarContacto() {
//    var form = document.form;
//
//    if (form.nombre.value == 0) {
//        alert("El campo NOMBRE esta vacio.")
//        form.nombre.value = "";
//        form.nombre.focus();
//        return false;
//    }
//
//    if (form.correo.value == 0) {
//        alert("El campo CORREO esta vacio.")
//        form.correo.value = "";
//        form.correo.focus();
//       return false;
//    }
//
//    if (form.asunto.value == 0) {
//        alert("Seleccione una opción.")
//        form.asunto.value = "";
//        form.asunto.focus();
//        return false;
//    }
//
//    if (form.mensaje.value == 0) {
//        alert("El campo de COMENTARIO esta vacio.")
//        form.mensaje.value = "";
//        form.mensaje.focus();
//        return false;
//    }
//
//}


var formContacto = document.getElementById('formularioContacto');
form.addEventListener('submit', function(evt) {
    evt.preventDefault();
    var mensajeError = [];

    if (nombre.value === null || nombre.value === '') {
        mensajeError.push("Ingrese su nombre ");
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (correo.value === null || correo.value === '') {
        mensajeError.push('Ingrese correo');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (asunto.value === '0') {
        mensajeError.push('Seleccione una opción');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (mensaje.value === null || mensaje.value === '') {
        mensajeError.push('Ingrese comentario');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }



});








//function validarLogin() {
//  var form = document.form;
//
//
//    if (form.correo.value == 0) {
//        alert("El campo CORREO esta vacio.")
//        form.correo.value = "";
//        form.correo.focus();
//        return false;
//    }
//
//    if (form.contraseña.value == 0) {
//        alert("El campo CONTRASEÑA esta vacio.")
//        form.contraseña.value = "";
//        form.contraseña.focus();
//      return false;
//    }
//}






//var expr = /^[a-zA-Z0-9_\.\-]+@[1-zA-Z0-9\-]+\-[a-zA-Z0-9\-\.]+$/;

//$(document).ready(function() {
//    $("#bEnviar").click(function() {
//        var correoLogin = $("#itCorreo").val();
//        var contrasenaLogin = $("#itContrasena").val();
//
//        if (correoLogin == "" || !expr.test(correoLogin)) {
//            $("#mensaje1").fadeIn();
//            return false;
//        } else {
//            $("#mensaje1").fadeOut();
//            if (contrasenaLogin == "") {
//                $("#mensaje2").fadeIn();
//                return false;
//            }
//        }
//    })
//})


var formLogin = document.getElementById('formularioLogin');
form.addEventListener('submit', function(evt) {
    evt.preventDefault();
    var mensajeError = [];



    if (correo.value === null || correo.value === '') {
        mensajeError.push('Ingrese correo');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }

    if (contrasena.value === null || contrasena.value === '') {
        mensajeError.push('Ingrese contraseña');
        error.innerHTML = mensajeError.join(', ');
        return false;
    }



});