document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('.stat-form');

    forms.forEach((form) => {
        form.addEventListener('submit', (event) => {
            event.preventDefault();
            const data = Object.fromEntries(new FormData(form).entries());
            const entry = {
                source: form.dataset.source,
                metric: data.metric.trim(),
                value: Number(data.value),
                notes: data.notes.trim(),
            };

            const existing = JSON.parse(localStorage.getItem('newfrontier-stats') || '[]');
            existing.push(entry);
            localStorage.setItem('newfrontier-stats', JSON.stringify(existing));

            const blob = new Blob([JSON.stringify(existing, null, 2)], { type: 'application/json' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'statistics_data.json';
            link.click();
            URL.revokeObjectURL(link.href);

            form.reset();
            const status = form.querySelector('.form-status');
            if (status) {
                status.textContent = 'Saved locally and downloaded as statistics_data.json.';
            }
        });
    });
});
