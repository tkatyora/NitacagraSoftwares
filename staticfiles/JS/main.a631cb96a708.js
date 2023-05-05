// This Javascript code for pages in the main application currently the Home ,About , NewProjects
// code for NewProjects

 let showMoreBtn = document.getElementById('show-1'),
     showMore1 = document.getElementById('showmore1'),
     showLessBtn1 = document.getElementById('less1');

 console.log(showMoreBtn)
 console.log(showMore1)
 console.log(showLessBtn1)
 showMoreBtn.addEventListener('click',()=>{
  showMore1.style.display = 'block'
  showMoreBtn.style.display = 'none'
    showLessBtn1.style.display = 'block'
 })
 showLessBtn1.addEventListener('click',()=>{
   alert('clicked')
  showMore1.style.display = 'none'
  showMoreBtn.style.display = 'block'
  showLessBtn1.style.display = 'none'
 })