const date = document.getElementById('date'),
      month = document.getElementById('month'),
      year = document.querySelector('#year'),
      day = document.querySelector("#day");

console.log(date)
console.log(month)
console.log(year)
console.log(day)

// day.innerHTML = new Date().getDay();
date.innerHTML = new Date().getDate();
month.innerHTML = new Date().getUTCMonth();

year.innerHTML = new Date().getFullYear();