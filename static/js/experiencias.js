
function openExpModal() {
    document.getElementById("expModal").style.display = "flex";
}

function closeExpModal() {
    document.getElementById("expModal").style.display = "none";
}

function openEditExpModal(button) {

    const id = button.dataset.id;
    const empresa = button.dataset.empresa;
    const puesto = button.dataset.puesto;
    const desde = button.dataset.desde;
    const hasta = button.dataset.hasta;
    const salario = button.dataset.salario;

    // Cambiar título
    document.querySelector(".modal-header h3").innerText = "Editar Experiencia";

    // Crear input hidden si no existe
    let hiddenId = document.getElementById("expId");
    if (!hiddenId) {
        hiddenId = document.createElement("input");
        hiddenId.type = "hidden";
        hiddenId.name = "id";
        hiddenId.id = "expId";
        document.querySelector("#expModal form").appendChild(hiddenId);
    }

    hiddenId.value = id;

    document.querySelector("input[name='empresa']").value = empresa;
    document.querySelector("input[name='puesto']").value = puesto;
    document.querySelector("input[name='fecha_desde']").value = desde;
    document.querySelector("input[name='fecha_hasta']").value = hasta;
    document.querySelector("input[name='salario']").value = salario;

    document.getElementById("expModal").style.display = "flex";
}

