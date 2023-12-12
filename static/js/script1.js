 document.getElementById('complaintForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const form = event.target;
            const formData = new FormData(form);

            fetch('/complain', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                // Display response from Flask on the screen
                console.log(data); // You can handle this response as required
                const responseContainer = document.getElementById('responseContainer');
                responseContainer.innerHTML = `${JSON.stringify(data)}`;

            })
            .catch(error => console.error('Error:', error));
        });