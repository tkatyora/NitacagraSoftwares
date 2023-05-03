let error = document.getElementsByClassName('error'),
  form = document.forms['form-id'],
  error1 = document.getElementById('error1'),
  error2 = document.getElementById('error2'),
  error3 = document.getElementById('error3'),
  username = document.forms["form"]['username'],
  password = document.forms["form"]['password'],
  show = document.querySelector('#show'),
  time = document.querySelector('#time'),
  input = document.getElementsByClassName('input')
  ;


console.log(error1)
console.log(error2)
console.log(error3)
for (error of error) {
  error.style.display = 'none';
}
form.addEventListener('submit', function (e) {
  e.preventDefault();
   console.log('hie')
  validation();

})

// validation function
function validation() {
  if (password.value == 2000 && username.value == 'admin') {
    window.location = "B:\\TNC-COMPANY-PROJECTS\\company-website\\BOOTSRAP-WEBSITE\\html.pages\\admin-dashboard.html";
  }
  else if (password.value == 2000 && username.value != 'admin') {
    usernameWrong();

  }
  else if (password.value != 2000 && username.value == 'admin') {
    error2.style.display = 'block';
    passwordWrong();
  }
  else {

    error1.style.display = 'block';
    bothWrong();
  }
}
show.addEventListener('click', function () {
  if (input[1].type === 'password') {
    input[1].type = 'text';
    show.textContent = 'Hide'

  } else {
    input[1].type = 'password';
    show.textContent = 'Show'

  }

}

)



// functions

function usernameWrong() {
  error3.style.display = 'block';
  input[0].style.border = '2px red solid';
  input[0].style.backgroundColor = 'red'
}
function passwordWrong() {
  error2.style.display = 'block';
  input[1].style.border = '2px red solid';

}
function bothWrong() {
  error3.style.display = 'block';
  input[0].style.border = '2px red solid';
  input[1].style.border = '2px red solid';

}

