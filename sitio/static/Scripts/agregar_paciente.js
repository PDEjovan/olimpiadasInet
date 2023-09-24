document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".form_agregar_paciente");
    const dniInput = document.getElementById("dni");
    const dniError = document.getElementById("dni-error");

    // Agregar un evento de escucha para el evento "input" en el campo del DNI
    dniInput.addEventListener("input", function() {
        // Obtener el valor actual del campo del DNI
        const dniValue = dniInput.value.trim();
        
        // Utilizar una expresión regular para eliminar todos los caracteres que no sean números
        const numericValue = dniValue.replace(/[^0-9]/g, "");

        // Asignar el valor numérico al campo del DNI
        dniInput.value = numericValue;

        // Validar la longitud del DNI
        if (numericValue.length < 8) {
            dniError.textContent = "El DNI debe tener al menos 8 caracteres.";
            dniError.style.color = "#EE5162";
            dniError.style.display = "block";
        } else {
            dniError.textContent = "";
            dniError.style.display = "none";
        }
    });

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

    const chkAlergia = document.getElementById("chk_input_alergias");
    const chkEnfermedad = document.getElementById("chk_input_enfermedad");
    const chkTratamiento = document.getElementById("chk_input_tratamiento");
    const chkEnfCir = document.getElementById("chk_input_enf_o_cir");

    const alergiaInput = document.getElementById("alergiaInput");
    const enfermedadInput = document.getElementById("enfermedadInput");
    const tratamientoInput = document.getElementById("tratamientoInput");
    const enfCirInput = document.getElementById("enfCirInput");

    chkAlergia.addEventListener("change", function() {
        alergiaInput.disabled = !chkAlergia.checked;
        if (!chkAlergia.checked) {
            alergiaInput.value = ""; // Borra el texto si se desactiva la checkbox
        }
    });

    chkEnfermedad.addEventListener("change", function() {
        enfermedadInput.disabled = !chkEnfermedad.checked;
        if (!chkEnfermedad.checked) {
            enfermedadInput.value = ""; // Borra el texto si se desactiva la checkbox
        }
    });

    chkTratamiento.addEventListener("change", function() {
        tratamientoInput.disabled = !chkTratamiento.checked;
        if (!chkTratamiento.checked) {
            tratamientoInput.value = ""; // Borra el texto si se desactiva la checkbox
        }
    });

    chkEnfCir.addEventListener("change", function() {
        enfCirInput.disabled = !chkEnfCir.checked;
        if (!chkEnfCir.checked) {
            enfCirInput.value = ""; // Borra el texto si se desactiva la checkbox
        }
    });

    const direccionInput = document.getElementById("direccionInput"); // Agregar ID al campo de dirección
    const direccionError = document.getElementById("direccion-error"); // Agregar un elemento para mostrar el error

    direccionInput.addEventListener("input", function() {
        const direccionValue = direccionInput.value.trim();
        
        if (!/^[a-zA-Z0-9\s]+$/.test(direccionValue)) {
            direccionError.textContent = "La dirección debe contener solo letras, números y espacios.";
            direccionError.style.color = "#EE5162";
            direccionError.style.display = "block";
        } else {
            direccionError.textContent = "";
            direccionError.style.display = "none";
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
        const dniValue = dniInput.value.trim(); // Elimina espacios en blanco al principio y al final
        const nombreValue = nombreInput.value.trim(); 
        const apellidoValue = apellidoInput.value.trim();
        const direccionValue = direccionInput.value.trim();

        if (dniValue.length < 8) {
            event.preventDefault(); // Evita que el formulario se envíe
            dniError.textContent = "* El DNI debe tener al menos 8 caracteres.";
            dniError.style.color = "#EE5162"; // Cambia el color del texto a rojo
            dniError.style.display = "block"; // Muestra el mensaje de error
            dniInput.scrollIntoView();
        } else {
            dniError.textContent = ""; // Borra el mensaje de error
            dniError.style.display = "none"; // Oculta el mensaje de error
        }


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

        
        if (!/^[a-zA-Z0-9\s]+$/.test(direccionValue)) {
            event.preventDefault(); // Evita que el formulario se envíe
            direccionError.textContent = "La dirección debe contener solo letras, números y espacios.";
            direccionError.style.color = "#EE5162";
            direccionError.style.display = "block";
            apellidoInput.scrollIntoView();
        }

    });
});