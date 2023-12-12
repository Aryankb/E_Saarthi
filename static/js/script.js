document.addEventListener('DOMContentLoaded', function() {
  const geoButtons = document.querySelectorAll('.geo-btn');
  const mapIframe = document.getElementById('map-iframe');

  geoButtons.forEach(button => {
    button.addEventListener('click', function() {
      const selectedOption = this.getAttribute('data-option');

      fetch('/geographical-analysis', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ option: selectedOption })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Request failed');
        }
        return response.text(); // Get the response as text (HTML)
      })
      .then(data => {
        // Set the received HTML as the iframe content
        mapIframe.srcdoc = data;

        // Scroll the page down
        window.scroll({
          top: document.body.scrollHeight,
          behavior: 'smooth' // You can change this to 'auto' for immediate scrolling
        });
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle error or show a message on the page indicating the failure
      });
    });
  });
});
