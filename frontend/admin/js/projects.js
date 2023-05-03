let btn = document.getElementsByClassName('button');


 for ( x= 0; x <btn.length;x++)

 {
    console.log('hie')
    btn[x].addEventListener('click',() => alert('You About to download the source code of this project'));
    
 }