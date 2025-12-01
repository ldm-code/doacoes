document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('button[data-produto-id]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const produtoId = btn.getAttribute('data-produto-id');
            const form = document.getElementById(`form-${produtoId}`);
            form.style.display = (form.style.display === 'none') ? 'block' : 'none';
        });
    });
});
