// Scripts específicos da página de cadastro 

// Elementos do DOM
const createAccountForm = document.getElementById('createAccountForm');
const successModal = document.getElementById('successModal');
const successTitle = document.getElementById('successTitle');
const successMessage = document.getElementById('successMessage');
const successOkBtn = document.getElementById('successOkBtn');
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

// Toggle do menu hamburguer
menuBtn.addEventListener('click', function() {
    menuBtn.classList.toggle('open');
    mobileMenu.classList.toggle('active');
});

// Fechar menu mobile ao clicar fora
document.addEventListener('click', function(e) {
    if (!menuBtn.contains(e.target) && !mobileMenu.contains(e.target) && mobileMenu.classList.contains('active')) {
        menuBtn.classList.remove('open');
        mobileMenu.classList.remove('active');
    }
});

// Toggle de visibilidade da senha
document.getElementById('toggleNewPassword').addEventListener('click', function() {
    const passwordInput = document.getElementById('newPassword');
    togglePasswordVisibility(passwordInput, this);
});

document.getElementById('toggleConfirmPassword').addEventListener('click', function() {
    const passwordInput = document.getElementById('confirmPassword');
    togglePasswordVisibility(passwordInput, this);
});

function togglePasswordVisibility(input, button) {
    if (input.type === 'password') {
        input.type = 'text';
        button.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
            </svg>
        `;
    } else {
        input.type = 'password';
        button.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
        `;
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    const googleSignUpBtn = document.getElementById('googleSignUpBtn');
    const form = document.querySelector('form');
    const successModal = document.getElementById('successModal');
    const successOkBtn = document.getElementById('successOkBtn');
    const toggleNewPasswordBtn = document.getElementById('toggleNewPassword');
    const toggleConfirmPasswordBtn = document.getElementById('toggleConfirmPassword');
    const newPasswordInput = document.getElementById('newPassword');
    const confirmPasswordInput = document.getElementById('confirmPassword');

    // Cadastro com Google
    if (googleSignUpBtn) {
        googleSignUpBtn.addEventListener('click', async () => {
            try {
                // Aqui você implementará a lógica de autenticação com o Google
                // Usando Firebase ou outra solução de autenticação
                showSuccessModal('Cadastro com Google realizado com sucesso!');
                setTimeout(() => {
                    window.location.href = '../login/index.html';
                }, 2000);
            } catch (error) {
                console.error('Erro no cadastro com Google:', error);
                alert('Erro ao realizar cadastro com Google. Tente novamente.');
            }
        });
    }

    // Toggle de visibilidade da senha
    if (toggleNewPasswordBtn && newPasswordInput) {
        toggleNewPasswordBtn.addEventListener('click', () => {
            const type = newPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            newPasswordInput.setAttribute('type', type);
        });
    }

    if (toggleConfirmPasswordBtn && confirmPasswordInput) {
        toggleConfirmPasswordBtn.addEventListener('click', () => {
            const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            confirmPasswordInput.setAttribute('type', type);
        });
    }

// Envio do formulário
    if (form) {
        form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
            const name = document.getElementById('newName').value;
            const email = document.getElementById('newEmail').value;
    const password = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
            const termsCheck = document.getElementById('termsCheck').checked;

            if (!termsCheck) {
                alert('Você precisa aceitar os termos de serviço.');
                return;
            }
    
    if (password !== confirmPassword) {
                alert('As senhas não coincidem.');
        return;
    }
    
    if (password.length < 8) {
                alert('A senha deve ter pelo menos 8 caracteres.');
        return;
    }
    
            try {
                // Aqui você implementará a lógica de criação de conta
                showSuccessModal('Conta criada com sucesso!');
    setTimeout(() => {
        window.location.href = '../login/index.html';
    }, 2000);
            } catch (error) {
                console.error('Erro no cadastro:', error);
                alert('Erro ao criar conta. Tente novamente.');
            }
        });
    }

    // Modal de sucesso
    if (successOkBtn) {
        successOkBtn.addEventListener('click', () => {
            successModal.classList.add('hidden');
        });
    }
});

// Mostrar modal de sucesso
function showSuccessModal(message) {
    const successModal = document.getElementById('successModal');
    const successMessage = document.getElementById('successMessage');
    if (successModal && successMessage) {
    successMessage.textContent = message;
    successModal.classList.remove('hidden');
}
}

// Criar mais efeitos de fumaça dinâmicos
function createDynamicSmokeEffects() {
    const colors = ['#6B19C9', '#E63783', '#F0C419'];
    const animationClasses = ['smoke-1', 'smoke-2', 'smoke-3'];
    const animatedBg = document.querySelector('.animated-bg');
    
    for (let i = 0; i < 5; i++) {
        const smoke = document.createElement('div');
        smoke.classList.add('smoke-effect');
        
        // Propriedades aleatórias
        const size = Math.floor(Math.random() * 300) + 150;
        const top = Math.floor(Math.random() * 100);
        const left = Math.floor(Math.random() * 100);
        const color = colors[Math.floor(Math.random() * colors.length)];
        const animClass = animationClasses[Math.floor(Math.random() * animationClasses.length)];
        
        // Aplicar estilos
        smoke.style.width = `${size}px`;
        smoke.style.height = `${size}px`;
        smoke.style.top = `${top}%`;
        smoke.style.left = `${left}%`;
        smoke.style.backgroundColor = color;
        smoke.classList.add(animClass);
        
        animatedBg.appendChild(smoke);
    }
}

// Adicionar mais efeitos de fumaça dinâmicos
createDynamicSmokeEffects(); 