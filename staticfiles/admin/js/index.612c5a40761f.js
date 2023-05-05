let button = document.getElementsByClassName('button');
const time = document.querySelector('#time'),
      logIn = document.getElementById('logIn');

 for ( x= 0; x <button.length;x++)
 {
    button[x].addEventListener('click',() => window.location="B:\\tnc-company-projects\\company-website\\bootsrap-website\\html.pages\\service.html");
    
 }
 console.log(logIn)
//  logIn.addEventListener('click',() => window.location="B:\\tnc-company-projects\\company-website\\bootsrap-website\\html.pages\\administration.html");
   
 // function for setting yearin the footer
 time.innerHTML = new Date().getFullYear();
   