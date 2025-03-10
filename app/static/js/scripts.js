document.addEventListener('DOMContentLoaded', function () {
    console.log('Application prête !');

    const formAjouter = document.querySelector('form');
    if (formAjouter) {
        formAjouter.addEventListener('submit', function (e) {
            e.preventDefault();  

            const formData = new FormData(formAjouter);

            fetch(formAjouter.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);  
                    window.location.href = data.redirect_url;  
                } else {
                    alert('Erreur : ' + data.message);  
                }
            })
            .catch(error => {
                console.error('Erreur AJAX :', error);
                alert('Une erreur s\'est produite lors de l\'envoi des données.');
            });
        });
    }
});