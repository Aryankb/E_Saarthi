document.getElementById('complaintForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const mobileNumber = document.getElementById('mobile').value;

    fetch('/fetch_complaints', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ mobileNumber: mobileNumber })
    })
    .then(response => response.json())
    .then(data => {
        // Display response from Flask on the screen
        console.log(data); // You can handle this response as required

        const responseContainer = document.getElementById('responseContainer');
        responseContainer.innerHTML = '';

        if (data.complaints && data.complaints.length > 0) {
            data.complaints.forEach(complaint => {
                const complaintDiv = document.createElement('div');
                complaintDiv.classList.add('complaint');
                complaintDiv.innerHTML = `
                    <h3>Complaint ID: ${complaint.id}</h3>
                    <p>Details: ${complaint.details}</p>
                    <p>Status: ${complaint.status}</p>
                    <p>Priority: ${complaint.priority}</p>
                `;
                responseContainer.appendChild(complaintDiv);
            });
        } else {
            responseContainer.innerText = 'No complaints found for this mobile number.';
        }
    })
    .catch(error => console.error('Error:', error));
});
