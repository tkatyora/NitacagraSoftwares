

const  greeting = document.getElementById('greeting');
let tryItNow = document.getElementsByClassName('try-it-now');

console.log(tryItNow)
 for ( x= 0; x <tryItNow.length;x++)

 {
   
    tryItNow[x].addEventListener('click',function(){
        alert('Thanks for choosing our Project Enjoy Using It')
        window.location =" B:\\tnc-company-projects\\company-website\\bootsrap-website\\trialProjects\\onlineCalculator\\calculator.html"
    }
    
    ); 
 }

