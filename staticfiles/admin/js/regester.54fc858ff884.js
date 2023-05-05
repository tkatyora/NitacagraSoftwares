let error = document.getElementById('error'),
     form = document.forms['form-id'],
     form2 = document.forms['form-id-2'],
     confirmPassword = document.forms["form2"]['confirmPassword'],
     password = document.forms["form2"]['password'],
     shows = document.querySelectorAll('.show'),
     prevButton = document.getElementById('previous'),
     confirms = document.getElementsByClassName('confirm')
 ;
 console.log(confirms)
 form.addEventListener('submit',function(e){
    e.preventDefault();
    
    form.style.display = "none";
    form2.style.display = "block";
 })
 form2.addEventListener('submit',function(e){
    e.preventDefault();
    validation();
})
 prevButton.addEventListener('click',function(){
   console.log('clickec')
  
   form2.style.display = "none";
    form.style.display = 'block'
   console.log(form.style.display) 
   console.log(form2.style.display) 
 } )

 // code for showing the password
   shows[0].addEventListener('click', ()=> showsDisplay1())
   shows[1].addEventListener('click', ()=> showsDisplay2())
 
     


//functions
function validation(){
   if (password.value === confirmPassword.value ){
     
      window.location = 'B:\\tnc-company-projects\\company-website\\bootsrap-website\\html.pages\\administration.html'
   }
   else {
      error.style.display = 'block'
      for (conf of confirms)
      {
        conf.style.border = ' red 2px solid'
        
      }
     
   }
}


// functiom for show
function showsDisplay1() 
{
            if(confirms[0].type === 'password'){
               confirms[0].type = 'text';
               shows[0].textContent = 'Hide'
               
            }else{
               confirms[0].type = 'password';
               show[0].textContent = 'Show'
               
            }

}
    
function showsDisplay2() 
{
            if(confirms[1].type === 'password'){
               confirms[1].type = 'text';
               show[1].textContent = 'Hide'
               
            }else{
               confirms[1].type = 'password';
               show[1].textContent = 'Show'
               
            }       
}
    

