document.addEventListener('input', function (event) {
    if (event.target.tagName.toLowerCase() === 'textarea') {
        autoResizeTextarea(event.target);
    }
});

function autoResizeTextarea(textarea) {
    // Сброс высоты, чтобы правильно рассчитать новую высоту
    textarea.style.height = 'auto';
    // Установка высоты равной контенту
    textarea.style.height = textarea.scrollHeight + 'px';
}

function toggleUserWorks(event, username) {
    event.preventDefault();  // Предотвращает перемещение вверх
    let worksSection = document.getElementById('works-' + username);
    worksSection.style.display = worksSection.style.display === 'none' ? 'table-row' : 'none';
}

// Автоматически подгоняем текстовое поле при загрузке страницы
window.onload = function() {
    document.querySelectorAll('textarea').forEach(function (textarea) {
        autoResizeTextarea(textarea);
    });
};