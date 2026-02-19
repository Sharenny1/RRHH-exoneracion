document.addEventListener("DOMContentLoaded", function () {

    const ctx = document.getElementById('graficoResumen');

    if (ctx) {
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Candidatos', 'Empleados'],
                datasets: [{
                    label: 'Cantidad',
                    data: [2, 3],
                    backgroundColor: ['#007bff', '#28a745']
                }]
            }
        });
    }

});
