function openModal(id = "", nombre = "", estado = "Activo") {
    document.getElementById("editModal").style.display = "flex";

    document.getElementById("edit-id").value = id;
    document.getElementById("edit-descripcion").value = nombre;
    document.getElementById("edit-estado").value = estado;
}

function closeModal() {
    document.getElementById("editModal").style.display = "none";
}
