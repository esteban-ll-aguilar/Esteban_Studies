// Función para alternar entre modo claro y oscuro
document.addEventListener('DOMContentLoaded', function() {
    // Verificar si hay una preferencia guardada en localStorage
    const savedTheme = localStorage.getItem('theme');
    
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        document.getElementById('theme-icon').classList.remove('fa-moon');
        document.getElementById('theme-icon').classList.add('fa-sun');
    }
    
    // Manejar el toggle del tema
    const themeToggle = document.querySelector('.theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        
        // Guardar preferencia en localStorage
        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
        } else {
            localStorage.setItem('theme', 'light');
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
        }
    });
    
    // Toggle para mostrar/ocultar contraseña
    const togglePassword = document.querySelector('.toggle-password');
    const passwordInput = document.querySelector('input[type="password"]');
    
    togglePassword.addEventListener('click', function() {
        // Cambiar el tipo de input
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        
        // Cambiar el icono
        this.classList.toggle('fa-eye-slash');
        this.classList.toggle('fa-eye');
    });    // Para propósitos de demostración - mostrar las acciones en consola
    const loginForm = document.querySelector('form');
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        console.log('Intento de login con correo electrónico');
    });

    // Botón personalizado de Google (respaldo)
    const googleBtn = document.querySelector('.google-btn');
    if (googleBtn) {
        googleBtn.addEventListener('click', function() {
            console.log('Intento de login con Google (botón personalizado)');
            // Si tienes el ID de cliente de Google configurado, puedes iniciar sesión programáticamente
            if (window.google && window.google.accounts) {
                google.accounts.id.prompt();
            }
        });
    }
});

// Función para manejar la respuesta de Google Sign-In
function handleCredentialResponse(response) {
    // Aquí recibirías el token JWT de Google
    console.log('Google Sign-In completado exitosamente');
    console.log('JWT ID Token:', response.credential);
    
    // En una implementación real, enviarías este token a tu servidor para verificación
    // y luego redirigirías al usuario a la página principal
    
    // Para demostración:
    const responsePayload = parseJwt(response.credential);
    console.log("ID: " + responsePayload.sub);
    console.log('Nombre completo: ' + responsePayload.name);
    console.log('Imagen de perfil: ' + responsePayload.picture);
    console.log('Email: ' + responsePayload.email);
}

// Función para analizar el token JWT
function parseJwt(token) {
    try {
        return JSON.parse(atob(token.split('.')[1]));
    } catch (e) {
        console.error('Error al analizar el token JWT:', e);
        return null;
    }
}

// Agregar Google Fonts para el botón
document.addEventListener('DOMContentLoaded', function() {
    const robotoFont = document.createElement('link');
    robotoFont.rel = 'stylesheet';
    robotoFont.href = 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap';
    document.head.appendChild(robotoFont);
    
    // Actualizar el botón de Google cuando esté en modo oscuro
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.attributeName === 'class' && 
                document.body.classList.contains('dark-mode')) {
                // Intentar actualizar el tema del botón de Google
                try {
                    const googleButton = document.querySelector('.g_id_signin div[aria-labelledby]');
                    if (googleButton) {
                        googleButton.setAttribute('data-theme', 'filled_black');
                    }
                } catch (e) {
                    console.log('No se pudo actualizar el tema del botón de Google', e);
                }
            }
        });
    });
    
    observer.observe(document.body, { attributes: true });
});