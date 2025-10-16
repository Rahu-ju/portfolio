// a small script to send ajax request using vanilla js to send mail to me.

        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('contactForm');
            const submitBtn = document.getElementById('submitBtn');
            const btnText = document.getElementById('btnText');
            const btnSpinner = document.getElementById('btnSpinner');
            const alertContainer = document.getElementById('alert-container');

            // Get CSRF token
            function getCsrfToken() {
              const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
              return csrfInput ? csrfInput.value : null;
            }
            const csrftoken = getCsrfToken();

            // Show alert message
            function showAlert(message, type) {
                alertContainer.innerHTML = `
                    <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                        ${message}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                `;
            }

            // Handle form submission
            form.addEventListener('submit', async function(e) {
                e.preventDefault();

                // Get form data
                const formData = {
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    message: document.getElementById('message').value
                };

                // Show loading state
                submitBtn.disabled = true;
                btnText.classList.add('d-none');
                btnSpinner.classList.remove('d-none');

                try {
                    // Send AJAX request
                    const response = await fetch('contact/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken
                        },
                        body: JSON.stringify(formData)
                    });

                    const data = await response.json();

                    if (response.ok && data.status === 'success') {
                        showAlert(data.message, 'success');
                        form.reset();
                    } else {
                        showAlert(data.message, 'danger');
                    }
                } catch (error) {
                    showAlert('An error occurred. Please try again.', 'danger');
                    // console.log('Error:', error);
                } finally {
                    // Hide loading state
                    submitBtn.disabled = false;
                    btnText.classList.remove('d-none');
                    btnSpinner.classList.add('d-none');
                }
            });
        });
