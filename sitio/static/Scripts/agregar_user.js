
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".form_agregar_medico_enfermero");

    const password = document.getElementById("password");
    const confirm_password = document.getElementById("confirm_password");
    const error_password = document.getElementById("contraseña-error");
    const error_conf_password = document.getElementById("contraseña-conf-error");

    const nombreInput = document.getElementById("nombreInput"); // Agregar ID al campo de nombre
    const nombreError = document.getElementById("nombre-error"); // Agregar un elemento para mostrar el error
    

    nombreInput.addEventListener("input", function() {
        const nombreValue = nombreInput.value.trim();

        if (nombreValue.length < 3) {
            nombreError.textContent = "El nombre debe tener al menos 3 caracteres.";
            nombreError.style.color = "#EE5162";
            nombreError.style.display = "block";
        } else if (!/^[a-zA-Z]+$/.test(nombreValue)) {
            nombreError.textContent = "El nombre solo debe contener letras.";
            nombreError.style.color = "#EE5162";
            nombreError.style.display = "block";
        } else {
            nombreError.textContent = "";
            nombreError.style.display = "none";
        }
    });

    const apellidoInput = document.getElementById("apellidoInput"); // Agregar ID al campo de apellido
    const apellidoError = document.getElementById("apellido-error"); // Agregar un elemento para mostrar el error

    apellidoInput.addEventListener("input", function() {
        const apellidoValue = apellidoInput.value.trim();
        
        if (apellidoValue.length < 3) {
            apellidoError.textContent = "El nombre debe tener al menos 3 caracteres.";
            apellidoError.style.color = "#EE5162";
            apellidoError.style.display = "block";
        } else if (!/^[a-zA-Z]+$/.test(apellidoValue)) {
            apellidoError.textContent = "El nombre solo debe contener letras.";
            apellidoError.style.color = "#EE5162";
            apellidoError.style.display = "block";
        } else {
            apellidoError.textContent = "";
            apellidoError.style.display = "none";
        }
    });

    const telefonoInput = document.getElementById("telefonoInput");

    telefonoInput.addEventListener("input", function() {
        const inputValue = telefonoInput.value;
        const telnumericValue = inputValue.replace(/\D/g, ""); // Elimina todos los caracteres no numéricos

        // Asigna el valor numérico nuevamente al campo de entrada
        telefonoInput.value = telnumericValue;
    });

    form.addEventListener("submit", function(event) {
        const nombreValue = nombreInput.value.trim(); 
        const apellidoValue = apellidoInput.value.trim();
        const passwordValue = password.value.trim();
        const confirm_password_Value = confirm_password.value.trim();

        if (nombreValue.length < 3) {
            event.preventDefault(); // Evita que el formulario se envíe
            nombreError.textContent = "El nombre debe tener al menos 3 caracteres.";
            nombreError.style.color = "#EE5162";
            nombreError.style.display = "block";
            nombreInput.scrollIntoView();
        } else if (!/^[a-zA-Z]+$/.test(nombreValue)) {
            event.preventDefault(); // Evita que el formulario se envíe
            nombreError.textContent = "El nombre solo debe contener letras.";
            nombreError.style.color = "#EE5162";
            nombreError.style.display = "block";
            nombreInput.scrollIntoView();
        } else {
            nombreError.textContent = "";
            nombreError.style.display = "none";
        }
        

        if (apellidoValue.length < 3) {
            event.preventDefault(); // Evita que el formulario se envíe
            apellidoError.textContent = "El apellido debe tener al menos 3 caracteres.";
            apellidoError.style.color = "#EE5162";
            apellidoError.style.display = "block";
            apellidoInput.scrollIntoView();
        } else if (!/^[a-zA-Z]+$/.test(apellidoValue)) {
            event.preventDefault(); // Evita que el formulario se envíe
            apellidoError.textContent = "El apellido solo debe contener letras.";
            apellidoError.style.color = "#EE5162";
            apellidoError.style.display = "block";
            apellidoInput.scrollIntoView();
        } else {
            apellidoError.textContent = "";
            apellidoError.style.display = "none";
        }

        if (passwordValue.length < 8) {
            event.preventDefault(); // Evita que el formulario se envíe
            error_password.textContent = "La contraseña debe tener al menos 8 caracteres.";
            error_password.style.color = "#EE5162";
            error_password.style.display = "block";
            passwordValue.scrollIntoView();
        } else {
            error_password.textContent = "";
            error_password.style.display = "none";
        }

        if (passwordValue !== confirm_password_Value) {
            event.preventDefault(); // Evita que el formulario se envíe
            error_conf_password.textContent = "Las contraseñas no coinciden";
            error_conf_password.style.color = "#EE5162";
            error_conf_password.style.display = "block";
            confirm_password_Value.scrollIntoView();
        } else {
            error_conf_password.textContent = "";
            error_conf_password.style.display = "none";
        }
    });
});