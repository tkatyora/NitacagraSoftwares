let buyButtons = document.getElementsByClassName('buy'),
    dropdwonbtn = document.getElementById('service'),
    dropdwonBlog = document.getElementById('blog'),
    dropdwonMenu = document.getElementById('dropdown-menu'),
    dropdwonMenu2 = document.getElementById('dropdown-menu2'),
    navLinkBtn = document.getElementsByClassName('services'),
    viewButtons = document.getElementsByClassName('view');



console.log(dropdwonbtn)
console.log(dropdwonMenu)
console.log(navLinkBtn)

dropdwonbtn.addEventListener('mouseover',function(e){
dropdwonMenu.style.display = 'block';
dropdwonMenu2.style.display = 'none';
 
})
 dropdwonBlog.addEventListener('mouseover',function(e){
dropdwonMenu2.style.display = 'block';
dropdwonMenu.style.display = 'none';
// dropdwonBlog.addEventListener('mouseout',function(e){
// dropdwonMenu2.style.display = 'none'
  
//  })


})


 for ( y= 0; y < navLinkBtn.length;x++)
 {
  navLinkBtn[y].addEventListener('mouseover',function(){
  dropdwonMenu.style.display = 'none' 
})
    }


// dropdwonbtn.addEventListener('mouseout',function(e){
// dropdwonMenu.style.display = 'none'
  
//  })
// dropdwonMenu.addEventListener('mouseout',function(){
//  dropdwonMenu.style.display = 'none' 
// })

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


    
 
