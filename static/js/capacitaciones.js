document.addEventListener("DOMContentLoaded", function () {

    const btnNuevo = document.getElementById("btnNuevoCap");

    if (btnNuevo) {
        btnNuevo.addEventListener("click", function () {
            openCapModal();
        });
    }
});


function openCapModal() {

    document.getElementById("capId").value = "";
    document.getElementById("capDescripcion").value = "";
    document.getElementById("capNivel").value = "Grado";
    document.getElementById("capFechaDesde").value = "";
    document.getElementById("capFechaHasta").value = "";
    document.getElementById("capInstitucion").value = "";

    document.getElementById("capModalTitle").innerText = "Nueva Capacitación";

    document.getElementById("capModal").style.display = "flex";
}


function editCapModal(id, descripcion, nivel, desde, hasta, institucion) {

    document.getElementById("capId").value = id;
    document.getElementById("capDescripcion").value = descripcion;
    document.getElementById("capNivel").value = nivel;
    document.getElementById("capFechaDesde").value = desde;
    document.getElementById("capFechaHasta").value = hasta;
    document.getElementById("capInstitucion").value = institucion;

    document.getElementById("capModalTitle").innerText = "Editar Capacitación";

    document.getElementById("capModal").style.display = "flex";
}


function closeCapModal() {
    document.getElementById("capModal").style.display = "none";
}
