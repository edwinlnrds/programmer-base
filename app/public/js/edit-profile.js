var usernameField = document.querySelector('#username')
usernameField.addEventListener('keyup', function (event) {
  event.preventDefault()
  document.querySelector('#avatar-preview').src = `https://avatars.dicebear.com/api/initials/${usernameField.value || 'NN'}.svg`
})