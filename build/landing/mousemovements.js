document.addEventListener('DOMContentLoaded', () => {
    const cursor = document.getElementById('cursor');
    cursor.classList.add('cursor');

    document.addEventListener('mousemove', (e) => {
        if (window.innerWidth > 1024) {
            cursor.style.left = `${e.pageX}px`;
            cursor.style.top = `${e.pageY}px`
            cursor.style.opacity = '1'; // Show the cursor
        }
    });

    document.addEventListener('mouseleave', () => {
        cursor.style.opacity = '0'; // Hide the cursor when leaving the window
    });

    document.addEventListener('mouseenter', () => {
        cursor.style.opacity = '1'; // Show the cursor when entering the window
    });
});
