// Mobile menu functionality
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('open');
    mobileMenu.classList.toggle('active');
});

// Course modal functionality
const courseModal = document.getElementById('course-modal');
const closeCourseModal = document.getElementById('close-course-modal');
const courseBoxes = document.querySelectorAll('.course-box');

courseBoxes.forEach(box => {
    box.addEventListener('click', () => {
        courseModal.classList.remove('hidden');
    });
});

closeCourseModal.addEventListener('click', () => {
    courseModal.classList.add('hidden');
});

// Add course modal functionality
const addCourseModal = document.getElementById('add-course-modal');
const closeAddModal = document.getElementById('close-add-modal');
const addCourseBtn = document.getElementById('add-course-btn');
const cancelAdd = document.getElementById('cancel-add');
const confirmAdd = document.getElementById('confirm-add');
const courseTable = document.querySelector('#add-course-modal table tbody');
const selectedCourses = new Set();

// Function to update selected courses count
function updateSelectedCoursesCount() {
    const countElement = document.querySelector('#add-course-modal .bg-black.bg-opacity-50 h3');
    const creditsElement = document.querySelector('#add-course-modal .bg-black.bg-opacity-50 .text-white span:first-child');
    const hoursElement = document.querySelector('#add-course-modal .bg-black.bg-opacity-50 .text-white span:last-child');
    
    countElement.textContent = `Matérias Selecionadas: ${selectedCourses.size}`;
    creditsElement.textContent = `Total de Créditos: ${selectedCourses.size * 4}`;
    hoursElement.textContent = `Carga Horária: ${selectedCourses.size * 4} horas/semana`;
}

// Function to update course box appearance
function updateCourseBoxAppearance(courseId, isSelected) {
    const courseBox = document.querySelector(`.course-box[data-course-id="${courseId}"]`);
    if (!courseBox) return;

    // Remove all possible states
    courseBox.classList.remove('course-future', 'course-selected', 'course-current', 'course-completed');

    if (isSelected) {
        courseBox.classList.add('course-selected');
    } else {
        courseBox.classList.add('course-future');
    }
}

// Function to toggle course selection
function toggleCourseSelection(courseId, button) {
    if (selectedCourses.has(courseId)) {
        selectedCourses.delete(courseId);
        button.textContent = 'Adicionar';
        button.className = 'bg-gradient-to-r from-green-600 to-green-500 text-white py-1 px-3 rounded hover:from-green-700 hover:to-green-600 transition-all duration-300';
        button.closest('tr').classList.remove('bg-purple-900', 'bg-opacity-20');
    } else {
        selectedCourses.add(courseId);
        button.textContent = 'Remover';
        button.className = 'bg-red-600 text-white py-1 px-3 rounded hover:bg-red-700 transition-all duration-300';
        button.closest('tr').classList.add('bg-purple-900', 'bg-opacity-20');
    }
    updateSelectedCoursesCount();
}

// Add event listeners to course buttons
courseTable.addEventListener('click', (e) => {
    const button = e.target.closest('button');
    if (!button) return;
    
    const row = button.closest('tr');
    const courseId = row.querySelector('td:first-child').textContent;
    toggleCourseSelection(courseId, button);
});

// Open add course modal
addCourseBtn.addEventListener('click', () => {
    addCourseModal.classList.remove('hidden');
});

// Close add course modal
closeAddModal.addEventListener('click', () => {
    addCourseModal.classList.add('hidden');
    selectedCourses.clear();
    updateSelectedCoursesCount();
});

// Cancel adding courses
cancelAdd.addEventListener('click', () => {
    addCourseModal.classList.add('hidden');
    selectedCourses.clear();
    updateSelectedCoursesCount();
});

// Confirm adding courses
confirmAdd.addEventListener('click', () => {
    // Apply changes to all selected courses
    selectedCourses.forEach(courseId => {
        updateCourseBoxAppearance(courseId, true);
    });
    
    // Reset courses that were previously selected but are now deselected
    document.querySelectorAll('.course-box').forEach(box => {
        const courseId = box.dataset.courseId;
        if (!selectedCourses.has(courseId) && box.classList.contains('course-selected')) {
            updateCourseBoxAppearance(courseId, false);
        }
    });
    
    alert('Alterações salvas com sucesso!');
    addCourseModal.classList.add('hidden');
    selectedCourses.clear();
    updateSelectedCoursesCount();
});

// Zoom functionality
const zoomIn = document.getElementById('zoom-in');
const zoomOut = document.getElementById('zoom-out');
const zoomLevel = document.getElementById('zoom-level');
const fluxogram = document.getElementById('fluxogram');

let currentZoom = 100;

zoomIn.addEventListener('click', () => {
    if (currentZoom < 200) {
        currentZoom += 10;
        fluxogram.style.transform = `scale(${currentZoom / 100})`;
        zoomLevel.textContent = `${currentZoom}%`;
    }
});

zoomOut.addEventListener('click', () => {
    if (currentZoom > 50) {
        currentZoom -= 10;
        fluxogram.style.transform = `scale(${currentZoom / 100})`;
        zoomLevel.textContent = `${currentZoom}%`;
    }
});

// Save functionality
const saveBtn = document.getElementById('save-btn');

saveBtn.addEventListener('click', () => {
    // Implement save functionality here
    alert('Fluxograma salvo com sucesso!');
}); 