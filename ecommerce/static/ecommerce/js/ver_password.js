function togglePassword() {
    var passwordInput = document.getElementById('passwordInput');
    var eyeIcon = document.getElementById('eyeIcon');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyeIcon.src = '../assets/ojo.png';
    } else {
        passwordInput.type = 'password';
        eyeIcon.src = '../assets/visible.png';
    }
}
