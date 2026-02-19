document.addEventListener("DOMContentLoaded", function () {

    const btnNuevo = document.getElementById("btnNuevoPuesto");

    if (btnNuevo) {
        btnNuevo.addEventListener("click", function () {
            openPuestoModal();
        });
    }

});


function openPuestoModal() {

    document.getElementById("puestoId").value = "";
    document.getElementById("puestoNombre").value = "";
    document.getElementById("puestoRiesgo").value = "Alto";
    document.getElementById("puestoMin").value = "";
    document.getElementById("puestoMax").value = "";
    document.getElementById("puestoEstado").value = "Activo";

    document.getElementById("puestoModalTitle").innerText = "Nuevo Puesto";

    document.getElementById("puestoModal").style.display = "flex";
}


function editPuestoModal(id, nombre, riesgo, min, max, estado) {

    document.getElementById("puestoId").value = id;
    document.getElementById("puestoNombre").value = nombre;
    document.getElementById("puestoRiesgo").value = riesgo;
    document.getElementById("puestoMin").value = min;
    document.getElementById("puestoMax").value = max;
    document.getElementById("puestoEstado").value = estado;

    document.getElementById("puestoModalTitle").innerText = "Editar Puesto";

    document.getElementById("puestoModal").style.display = "flex";
}


function closePuestoModal() {
    document.getElementById("puestoModal").style.display = "none";
}
