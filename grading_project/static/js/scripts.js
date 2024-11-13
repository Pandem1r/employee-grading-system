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
    event.preventDefault();
    let worksSection = document.getElementById('works-' + username);
    let isHidden = worksSection.style.display === 'none';

    // Показать или скрыть строку
    worksSection.style.display = isHidden ? 'table-row' : 'none';

    // Если секция стала видимой, применить autoResizeTextarea к текстовым полям
    if (isHidden) {
        worksSection.querySelectorAll('textarea').forEach(autoResizeTextarea);
    }
}


// Автоматически подгоняем текстовое поле при загрузке страницы
window.onload = function() {
    document.querySelectorAll('textarea').forEach(function (textarea) {
        autoResizeTextarea(textarea);
    });
};