document.addEventListener('DOMContentLoaded', function () {
    const imageContainers = document.querySelectorAll('.recent_photo img');
    const saveButton = document.querySelector('.user-register');

    if (saveButton && imageContainers.length > 0) {
        saveButton.addEventListener('click', function () {
            // Assuming the first image container is the one you want to save
            const imageToSave = imageContainers[0];

            // Check if an image is present
            if (imageToSave && imageToSave.src) {
                // Convert base64 image to a Blob
                fetch(imageToSave.src)
                    .then(res => {
                        if (!res.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return res.blob();
                    })
                    .then(blob => {
                        // Create a link element
                        const link = document.createElement('a');
                        const objectURL = URL.createObjectURL(blob);

                        link.href = objectURL;

                        // Set the download attribute to specify the filename
                        link.download = 'image.jpg';

                        // Simulate a click on the link to trigger the download
                        link.click();

                        // Revoke the object URL to free up resources
                        URL.revokeObjectURL(objectURL);
                    })
                    .catch(error => console.error('Error fetching image:', error));
            } else {
                console.log('No image to save');
            }
        });
    } else {
        console.error('Save button or image container not found.');
    }
});

