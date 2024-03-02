// 인증된 사람 알림 js파일
$(document).ready(function () {
    function showNotification(message) {
        console.log('Received message:', message);  // Add this line for debugging
        // $('#notification-modal-body').text(message);
        // $('#notification-modal').modal('show');
            // Check if the modal exists
        if ($('#notification-modal').length === 0) {
        console.error('Notification modal not found');
        return;
        }

        // Set the message in the modal body
        $('#notification-modal-body').text(message);

        // Trigger the modal
        $('#notification-modal').modal('show'); 
        
        // Hide the modal after 10 seconds
        setTimeout(function () {
        $('#notification-modal').modal('hide');
        }, 3000);

    }

    function fetchData() {
        $.ajax({
            url: '/get_latest_data/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
            if (data && data.current_data) {
                showNotification(data.message);

                // Update the UI or perform other actions with the data
                $('#data-container').html('Current Data: ' + data.current_data);
            }
        },
        error: function (xhr, status, error) {
            console.error('Error fetching data:', error);
        },
        complete: function () {
            // Schedule the next request after 30 seconds
            setTimeout(fetchData, 10000);
        }
    });
}

    // Initial call to start the process
    fetchData();
});

