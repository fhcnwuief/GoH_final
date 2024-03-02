let isRecording = false;

async function toggleRecording() {
    if (!isRecording) {
        startRecording();
    } else {
        stopRecording();
    }
}

async function startRecording() {
    // Check if recording is already in progress
    if (isRecording) {
        return;
    }
    

    try {
        const csrftoken = getCookie('csrftoken');

        const response = await fetch('/video/start-recording/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
        });

        if (response.ok) {
            const data = await response.json();
            alert(`Recording started successfully!`);
        } else {
            const data = await response.json();
            alert(`Error starting recording: ${data.error}`);
        }
    } catch (error) {
        console.error('Error starting recording:', error);
    }
}

async function stopRecording() {
    // You can implement stopping the recording if needed
    // For now, you can leave it empty or implement it based on your requirements
    isRecording = false;
}

// Add a function to get the CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if the cookie name matches the requested name
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}