// This file contains the JavaScript code for the website, handling interactivity and dynamic content.

document.addEventListener('DOMContentLoaded', () => {
    console.log('Coffee Shop Website Loaded');

    // Example of interactivity: Toggle menu on mobile
    const menuToggle = document.getElementById('menu-toggle');
    const nav = document.getElementById('nav');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }

    // Additional JavaScript functionality can be added here
});