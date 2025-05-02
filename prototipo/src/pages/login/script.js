// Scripts específicos da página de login 

// DOM Elements
const loginForm = document.getElementById('loginForm');
const forgotPasswordForm = document.getElementById('forgotPasswordForm');
const anonymousLoginForm = document.getElementById('anonymousLoginForm');
const successModal = document.getElementById('successModal');
const successTitle = document.getElementById('successTitle');
const successMessage = document.getElementById('successMessage');
const successOkBtn = document.getElementById('successOkBtn');
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

// Hamburger menu toggle
menuBtn.addEventListener('click', function() {
    menuBtn.classList.toggle('open');
    mobileMenu.classList.toggle('active');
});

// Close mobile menu when clicking outside
document.addEventListener('click', function(e) {
    if (!menuBtn.contains(e.target) && !mobileMenu.contains(e.target) && mobileMenu.classList.contains('active')) {
        menuBtn.classList.remove('open');
        mobileMenu.classList.remove('active');
    }
});

// Navigation functions
function showForm(formToShow) {
    // Esconder todos os formulários primeiro
    [loginForm, forgotPasswordForm, anonymousLoginForm].forEach(form => {
        form.classList.add('hidden');
        form.classList.remove('slide-in');
    });
    
    // Mostrar o formulário solicitado
    formToShow.classList.remove('hidden');
    formToShow.classList.add('slide-in');
}

// Event Listeners for navigation
document.getElementById('forgotPasswordLink').addEventListener('click', function(e) {
    e.preventDefault();
    showForm(forgotPasswordForm);
});

document.getElementById('anonymousLoginLink').addEventListener('click', function(e) {
    e.preventDefault();
    showForm(anonymousLoginForm);
});

document.getElementById('backToLoginFromForgot').addEventListener('click', function(e) {
    e.preventDefault();
    showForm(loginForm);
});

document.getElementById('backToLoginFromAnonymous').addEventListener('click', function(e) {
    e.preventDefault();
    showForm(loginForm);
});

// Form submissions
loginForm.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    showSuccessModal('Login realizado!', 'Você foi autenticado com sucesso.');
    // Redirecionar após 1.5 segundos
    setTimeout(() => {
        window.location.href = '../fluxogramas/index.html';
    }, 1500);
});

forgotPasswordForm.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('recoveryEmail').value;
    showSuccessModal('Email enviado!', `Um link de recuperação foi enviado para ${email}.`);
    // Após 2 segundos, retornar para o login
    setTimeout(() => {
        showForm(loginForm);
    }, 2000);
});

// Google login
document.getElementById('googleLoginBtn').addEventListener('click', function() {
    showSuccessModal('Google Login', 'Você foi autenticado com Google com sucesso.');
    // Redirecionar após 1.5 segundos
    setTimeout(() => {
        window.location.href = '../fluxogramas/index.html';
    }, 1500);
});

// Anonymous login
document.getElementById('confirmAnonymousBtn').addEventListener('click', function() {
    showSuccessModal('Login anônimo', 'Você entrou como usuário anônimo.');
    // Redirecionar após 1.5 segundos
    setTimeout(() => {
        window.location.href = '../fluxogramas/index.html';
    }, 1500);
});

// Success modal handling
function showSuccessModal(title, message) {
    successTitle.textContent = title;
    successMessage.textContent = message;
    successModal.classList.remove('hidden');
}

successOkBtn.addEventListener('click', function() {
    successModal.classList.add('hidden');
});

// Create more dynamic smoke effects
function createDynamicSmokeEffects() {
    const colors = ['#6B19C9', '#E63783', '#F0C419'];
    const animationClasses = ['smoke-1', 'smoke-2', 'smoke-3'];
    const animatedBg = document.querySelector('.animated-bg');
    
    for (let i = 0; i < 5; i++) {
        const smoke = document.createElement('div');
        smoke.classList.add('smoke-effect');
        
        // Random properties
        const size = Math.floor(Math.random() * 300) + 150;
        const top = Math.floor(Math.random() * 100);
        const left = Math.floor(Math.random() * 100);
        const color = colors[Math.floor(Math.random() * colors.length)];
        const animClass = animationClasses[Math.floor(Math.random() * animationClasses.length)];
        
        // Apply styles
        smoke.style.width = `${size}px`;
        smoke.style.height = `${size}px`;
        smoke.style.top = `${top}%`;
        smoke.style.left = `${left}%`;
        smoke.style.backgroundColor = color;
        smoke.classList.add(animClass);
        
        animatedBg.appendChild(smoke);
    }
}

// Add more dynamic smoke effects
createDynamicSmokeEffects(); 