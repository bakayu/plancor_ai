document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll('.button');
    buttons.forEach(button => {
        button.style.opacity = '0';
        setTimeout(() => {
            button.style.transition = 'opacity 1s ease-in';
            button.style.opacity = '1';
        }, 100);
    });
});
