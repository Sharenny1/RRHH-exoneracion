document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("btnNuevoCandidato");

    if (btn) {
        btn.addEventListener("click", function () {
            openCandidatoModal();
        });
    }

});

function openCandidatoModal() {

    const idField = document.getElementById("candidatoId");
    if (idField) idField.value = "";

    const title = document.getElementById("candidatoModalTitle");
    if (title) title.innerText = "Nuevo Candidato";

    const modal = document.getElementById("candidatoModal");
    if (modal) modal.style.display = "flex";
}

function editCandidatoModal(id, cedula, nombre, puesto, depto, salario, comp, cap, exp, rec, estado) {

    const idField = document.getElementById("candidatoId");
    if (idField) idField.value = id;

    const cedulaField = document.getElementById("candidatoCedula");
    if (cedulaField) cedulaField.value = cedula;

    const nombreField = document.getElementById("candidatoNombre");
    if (nombreField) nombreField.value = nombre;

    const puestoField = document.getElementById("candidatoPuesto");
    if (puestoField) puestoField.value = puesto;

    const deptoField = document.getElementById("candidatoDepto");
    if (deptoField) deptoField.value = depto;

    const salarioField = document.getElementById("candidatoSalario");
    if (salarioField) salarioField.value = salario;

    const compField = document.getElementById("candidatoComp");
    if (compField) compField.value = comp;

    const capField = document.getElementById("candidatoCap");
    if (capField) capField.value = cap;

    const expField = document.getElementById("candidatoExp");
    if (expField) expField.value = exp;

    const recField = document.getElementById("candidatoRec");
    if (recField) recField.value = rec;

   
    const estadoField = document.getElementById("candidatoEstado");
    if (estadoField) {
        estadoField.value = estado;
    }

    const title = document.getElementById("candidatoModalTitle");
    if (title) title.innerText = "Editar Candidato";

    const modal = document.getElementById("candidatoModal");
    if (modal) modal.style.display = "flex";
}

function closeCandidatoModal() {

    const modal = document.getElementById("candidatoModal");
    if (modal) modal.style.display = "none";
}
