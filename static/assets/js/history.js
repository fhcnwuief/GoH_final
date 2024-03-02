function updateCardContainer(data) {
    var cardContainer = document.getElementById('card-container');
    cardContainer.innerHTML = '';

    for (var i = 0; i < data.length; i++) {
        var card = document.createElement('div');
        card.className = 'con2';
       

        // Construct the full static path for the image
        var imagePath = staticUrl + data[i].verified_img;

        card.innerHTML = `
            <a><img src="${imagePath}" alt="Image"></a>
            <div>${data[i].verified_name}</div>
            <div>${data[i].verified_time}</div>
        `;

        cardContainer.appendChild(card);
    }
}

function fetchData() {
    // Use AJAX to fetch data from the API endpoint
    fetch('/history_list')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Data received:', data);

            // Check if data is an array
            if (Array.isArray(data)) {
                // Log the values of verified_img for each item in the data array
                for (var i = 0; i < data.length; i++) {
                    console.log(`Verified Image ${i}: ${data[i].verified_img}`);
                }

                updateCardContainer(data);
            } else {
                console.error('Invalid data format. Expected an array:', data);
            }
        })
        .catch(error => console.error('Error:', error));
}

// Fetch data initially and set up periodic updates
fetchData();
setInterval(fetchData, 30000);  // Update every minute, adjust as needed
