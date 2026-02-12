document.addEventListener('DOMContentLoaded', () => {
    sessionStorage.removeItem('pressuredle_start_time');
    const countdownElement = document.getElementById('countdown');
    if (countdownElement) {
        const targetUrl = countdownElement.dataset.redirect;
        
        let seconds = 3;

        const interval = setInterval(() => {
            seconds--;
            countdownElement.textContent = seconds;
            if (seconds <= 0) {
                clearInterval(interval);
                if (targetUrl) {
                    window.location.href = targetUrl;
                } else {
                    console.error("Redirect URL not found on countdown element.");
                }
            }
        }, 1000);
    }
});