let buyButtons = document.getElementsByClassName('buy'),
    
    viewButtons = document.getElementsByClassName('view');


// for the buy button clicked
 for ( x= 0; x <buyButtons.length;x++)

 {
   
    buyButtons[x].addEventListener('click',function(){
      alert('Thanks for choosing this service ');
      window.location = 'B:\\tnc-company-projects\\company-website\\bootsrap-website\\html.pages\\buy.html'
    } )
    }

// for the view button clicked
 for ( x= 0; x <viewButtons.length;x++)

 {
    
    viewButtons[x].addEventListener('click',function(){
   console.log('hie')
      window.location = 'B:\\tnc-company-projects\\company-website\\bootsrap-website\\html.pages\\detailed.html'
    } )
    }


    
 
