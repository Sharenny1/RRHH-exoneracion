document.addEventListener("DOMContentLoaded", function() {

    const btnNuevo = document.getElementById("btnNuevoIdioma");

    if (btnNuevo) {
        btnNuevo.addEventListener("click", function() {
            openIdiomaModal();
        });
    }

});


/* ===== ABRIR NUEVO ===== */
function openIdiomaModal() {

    document.getElementById("idiomaId").value = "";
    document.getElementById("idiomaNombre").value = "";
    document.getElementById("idiomaEstado").value = "Activo";

    document.getElementById("idiomaModalTitle").innerText = "Nuevo Idioma";

    document.getElementById("idiomaModal").style.display = "flex";
}


/* ===== EDITAR ===== */
function editIdiomaModal(id, nombre, estado) {

    document.getElementById("idiomaId").value = id;
    document.getElementById("idiomaNombre").value = nombre;
    document.getElementById("idiomaEstado").value = estado;

    document.getElementById("idiomaModalTitle").innerText = "Editar Idioma";

    document.getElementById("idiomaModal").style.display = "flex";
}


/* ===== CERRAR ===== */
function closeIdiomaModal() {
    document.getElementById("idiomaModal").style.display = "none";
}
