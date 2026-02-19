document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("btnNuevoEmpleado");

    if (btn) {
        btn.addEventListener("click", function () {
            openEmpleadoModal();
        });
    }

});


function openEmpleadoModal() {

    document.getElementById("empleadoId").value = "";
    document.getElementById("empleadoModalTitle").innerText = "Nuevo Empleado";
    document.getElementById("empleadoModal").style.display = "flex";
}


function editEmpleadoModal(id, cedula, nombre, fecha, depto, puesto, salario, estado) {

    document.getElementById("empleadoId").value = id;
    document.getElementById("empleadoCedula").value = cedula;
    document.getElementById("empleadoNombre").value = nombre;
    document.getElementById("empleadoFecha").value = fecha;
    document.getElementById("empleadoDepto").value = depto;
    document.getElementById("empleadoPuesto").value = puesto;
    document.getElementById("empleadoSalario").value = salario;
    document.getElementById("empleadoEstado").value = estado;

    document.getElementById("empleadoModalTitle").innerText = "Editar Empleado";
    document.getElementById("empleadoModal").style.display = "flex";
}


function closeEmpleadoModal() {
    document.getElementById("empleadoModal").style.display = "none";
}
