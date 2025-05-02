import CONFIG from '../constants/config.js';

export const navigateTo = (route) => {
    window.location.href = route;
};

export const showModal = (content) => {
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.innerHTML = `
        <div class="modal-content">
            ${content}
        </div>
    `;
    document.body.appendChild(modal);
    return modal;
};

export const hideModal = (modal) => {
    if (modal) {
        modal.remove();
    }
};

export const formatCourseCode = (code) => {
    return code.replace(/([A-Z]+)(\d+)/, '$1 $2');
};

export const getStoredUser = () => {
    const user = localStorage.getItem(CONFIG.STORAGE.USER_KEY);
    return user ? JSON.parse(user) : null;
};

export const setStoredUser = (user) => {
    localStorage.setItem(CONFIG.STORAGE.USER_KEY, JSON.stringify(user));
};

export const removeStoredUser = () => {
    localStorage.removeItem(CONFIG.STORAGE.USER_KEY);
};

export const getStoredToken = () => {
    return localStorage.getItem(CONFIG.STORAGE.TOKEN_KEY);
};

export const setStoredToken = (token) => {
    localStorage.setItem(CONFIG.STORAGE.TOKEN_KEY, token);
};

export const removeStoredToken = () => {
    localStorage.removeItem(CONFIG.STORAGE.TOKEN_KEY);
};

export const isAuthenticated = () => {
    return !!getStoredToken();
};

export const logout = () => {
    removeStoredUser();
    removeStoredToken();
    navigateTo(CONFIG.ROUTES.LOGIN);
}; 