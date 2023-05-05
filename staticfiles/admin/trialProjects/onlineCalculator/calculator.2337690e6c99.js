let display = document.getElementById('display'),
numbers = document.getElementsByClassName('btn'),
minus =document.getElementById('minus'),
equal = document.getElementById('equal')
specialOperators = document.getElementsByClassName('operator-btn');


const zero = 0,
       one = 1,
       two = 2,
       three = 3,
       four = 4,
       five = 5,
       six = 6,
        seven = 7,
        eight = 8,
        nine = 9,
        plus = '+';

   
    
    
    numbers[6].addEventListener('click', function(){
        display.textContent = one + two
    }
    )
    numbers[7].addEventListener('click', function(){
        display.textContent = two 
    }
    )
    numbers[8].addEventListener('click', function(){
        display.textContent = three + one
    }
    )
    numbers[3].addEventListener('click', function(){
        display.textContent = four
    }
    )
    numbers[4].addEventListener('click', function(){
        display.textContent = five
    }
    )
    numbers[5].addEventListener('click', function(){
        display.textContent = six
    }
    )
    numbers[0].addEventListener('click', function(){
        display.textContent = seven
    }
    )
    numbers[1].addEventListener('click', function(){
        display.textContent = eight
    }
    )

    numbers[2].addEventListener('click', function()
    {
        display.textContent = nine
    }
    )
    numbers[9].addEventListener('click', function()
    {
        display.innerHTML = zero
    }
    )