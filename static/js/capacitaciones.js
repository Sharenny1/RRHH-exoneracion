document.addEventListener("DOMContentLoaded", function() {

    const btnNuevo = document.getElementById("btnNuevoCap");

    if (btnNuevo) {
        btnNuevo.addEventListener("click", function() {
            openCapModal();
        });
    }

});


function openCapModal() {

    document.getElementById("capId").value = "";
    document.getElementById("capNombre").value = "";
    document.getElementById("capEstado").value = "Activo";

    document.getElementById("capModalTitle").innerText = "Nueva Capacitación";

    document.getElementById("capModal").style.display = "flex";
}


function editCapModal(id, nombre, estado) {

    document.getElementById("capId").value = id;
    document.getElementById("capNombre").value = nombre;
    document.getElementById("capEstado").value = estado;

    document.getElementById("capModalTitle").innerText = "Editar Capacitación";

    document.getElementById("capModal").style.display = "flex";
}


function closeCapModal() {
    document.getElementById("capModal").style.display = "none";
}
