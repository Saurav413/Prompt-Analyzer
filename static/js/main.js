(function () {
    const form = document.getElementById('analyze-form');
    const textarea = document.getElementById('user_prompt');
    const charCount = document.getElementById('char-count');
    const submitBtn = document.getElementById('submit-btn');
    const resultsPanel = document.querySelector('.results-panel');

    function updateCharCount() {
        const len = textarea.value.length;
        charCount.textContent = len === 1 ? '1 character' : len + ' characters';
    }

    if (textarea && charCount) {
        updateCharCount();
        textarea.addEventListener('input', updateCharCount);
    }

    document.querySelectorAll('.chip').forEach(function (chip) {
        chip.addEventListener('click', function () {
            textarea.value = chip.dataset.example || '';
            updateCharCount();
            textarea.focus();
        });
    });

    if (form && submitBtn) {
        form.addEventListener('submit', function () {
            submitBtn.disabled = true;
            submitBtn.classList.add('is-loading');
            submitBtn.querySelector('.btn-label').textContent = 'Analyzing…';
        });
    }

    if (resultsPanel && resultsPanel.querySelector('.score-card') && resultsPanel.querySelector('.result-box')) {
        resultsPanel.classList.add('has-both');
    }
})();
