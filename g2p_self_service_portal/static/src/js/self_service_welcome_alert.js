const alertBox = document.getElementById('alertbox');
const closeBtn = alertBox.querySelector('.closebtn');


if (!localStorage.getItem('visited')) {
  // Show the welcome message
  alertBox.style.display="block"
  localStorage.setItem('visited', true);
}

closeBtn.addEventListener('click', function() {
  alertBox.style.display="none"
  localStorage.removeItem('visited');
});
