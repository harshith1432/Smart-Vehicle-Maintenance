// Main JS interactions for Smart Vehicle Maintenance System

document.addEventListener('DOMContentLoaded', () => {
    // Flash message dismissal
    const alerts = document.querySelectorAll('.glass-card[style*="border-left"]');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            alert.style.transition = 'all 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // Active Sidebar Link highlighting
    const currentPath = window.location.pathname;
    const sidebarLinks = document.querySelectorAll('.sidebar a');
    sidebarLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.remove('btn-outline');
            link.style.background = 'var(--primary)';
            link.style.color = 'white';
        }
    });
});
