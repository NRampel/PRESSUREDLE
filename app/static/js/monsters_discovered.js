document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/monsters_discovered')
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById('grid-container');
            if (data.length === 0) {
                grid.innerHTML = "<p style='color: #888;'>You haven't discovered any monsters yet.</p>";
                return;
            }
            data.forEach(monster => {
                const box = document.createElement('div');
                box.className = 'monster-box';
                box.innerHTML = `
                    <img src="${monster.image_url}" alt="${monster.name}" style="max-width: 100%; border-radius: 5px; margin-bottom: 10px;">
                    <h3>${monster.name}</h3>
                `;
            
                grid.appendChild(box);
            });
        })
        .catch(error => {
            console.error("Error fetching monsters:", error);
        });
});
