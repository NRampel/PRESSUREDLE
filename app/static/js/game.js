 (function() {
            const monsterToHighlight = "{{ highlight_guess }}";

            if (monsterToHighlight) {
                const rowId = "row-" + monsterToHighlight.replace(/ /g, '-');
                const rowElement = document.getElementById(rowId);

                if (rowElement) {
                    rowElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    rowElement.classList.add('highlight');

                    setTimeout(() => {
                        rowElement.classList.remove('highlight');
                    }, 2000); 
                }
            }
        })();

        (function() {
            const stopwatch = document.getElementById('stopwatch');

            const resetTimer = () => sessionStorage.removeItem('pressuredle_start_time');
            const difficultyForm = document.getElementById('difficulty-form');
            if (difficultyForm) difficultyForm.addEventListener('submit', resetTimer);
            const playAgainForm = document.getElementById('play-again-form');
            if (playAgainForm) playAgainForm.addEventListener('submit', resetTimer);

            let startTime = sessionStorage.getItem('pressuredle_start_time');
            if (!startTime && document.querySelector('input[name="monster_guess"]')) {
                startTime = Date.now();
                sessionStorage.setItem('pressuredle_start_time', startTime);
            }

            if (startTime) {
                const getElapsed = () => Math.floor((Date.now() - startTime) / 1000);

                if (stopwatch) {
                    const updateTimer = () => {
                        const elapsed = getElapsed();
                        const m = Math.floor(elapsed / 60).toString().padStart(2, '0');
                        const s = (elapsed % 60).toString().padStart(2, '0');
                        stopwatch.textContent = `${m}:${s}`;
                    };
                    updateTimer();
                    if (document.querySelector('input[name="monster_guess"]')) {
                        setInterval(updateTimer, 1000);
                    }
                }

                const finalTime = document.getElementById('final-time');
                if (finalTime) {
                    finalTime.textContent = getElapsed() + " seconds";
                }
            }
        })();
        document.addEventListener("DOMContentLoaded", function() {
            const backgrounds = window.GAME_BACKGROUNDS; 
            let chosenImage = sessionStorage.getItem('active_background');
            if (!chosenImage && backgrounds && backgrounds.length > 0) {
                const randomIndex = Math.floor(Math.random() * backgrounds.length);
                chosenImage = backgrounds[randomIndex];
                sessionStorage.setItem('active_background', chosenImage);
            }
            if (chosenImage) {
                const bgPath = "/static/images/backgrounds/" + chosenImage;
                document.body.style.backgroundImage = `url('${bgPath}')`;
            }
        });