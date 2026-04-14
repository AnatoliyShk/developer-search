document.addEventListener('click', function (e) {
  if (e.target.classList.contains('alert__close')) {
    e.target.closest('.alert').style.display = 'none'
  }
})
