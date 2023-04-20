class Tooth {
    id;
    element;
    state = []; // length 7
    
    constructor(id, state) {
      this.id = id;
      this.element = document.getElementById(id);
      this.element.onclick = (e) => this.setState(e.target);
      this.state = state || [];
      this.init();
    }
  
    setState(target) {
      target.classList.toggle('painted');
      this.state[target.getAttribute('data')] = true;
    }
  
    init() {
      if(this.state && this.state.length) {
        this.state.forEach((toothPart, index) => {
          if(toothPart) {
            Array.from(this.element.children).forEach(part => {
              if(part.getAttribute('data') == index) this.setState(part);
            }) 
          }
        })
      }
    }  
  }
  
  const tooth1 = new Tooth(1);
  const tooth2 = new Tooth(2);
  const tooth3 = new Tooth(3);
  const tooth4 = new Tooth(4);
  const tooth5 = new Tooth(5);
  const tooth6 = new Tooth(6);
  const tooth7 = new Tooth(7);
  const tooth8 = new Tooth(8);
  const tooth9 = new Tooth(9);
  const tooth10 = new Tooth(10);
  const tooth11 = new Tooth(11);
  const tooth12 = new Tooth(12);
  const tooth13 = new Tooth(13);
  const tooth14 = new Tooth(14);
  const tooth15 = new Tooth(15);
  const tooth16 = new Tooth(16);
  const tooth17 = new Tooth(17);
  const tooth18 = new Tooth(18);
  const tooth19 = new Tooth(19);
  const tooth20 = new Tooth(20);
  const tooth21 = new Tooth(21);
  const tooth22 = new Tooth(22);
  const tooth23 = new Tooth(23);
  const tooth24 = new Tooth(24);
  const tooth25 = new Tooth(25);
  const tooth26 = new Tooth(26);


/**
    <div class="tooth-wrapper" id="${tooth.id}">
      <div class="tooth ${tooth.state ? 'painted' : ''}">
        <div class="tooth-part center-circle">${tooth.state}</div>
        <div class="tooth-part part-1"></div>
        <div class="tooth-part part-2"></div>
        <div class="tooth-part part-3"></div>
        <div class="tooth-part part-4"></div>
        <div class="tooth-part part-5"></div>
        <div class="tooth-part part-6"></div>
      </div>
    </div>
*/
/*const tooth = document.getElementById('26');

tooth.addEventListener('click', (event) => {
  const clickedPart = event.target;
 
  if (clickedPart.classList.contains('tooth-part')) {
    const color = prompt('Ingrese un color en formato hexadecimal, por ejemplo #ff0000:');
 
    if (color) {
      clickedPart.style.backgroundColor = color;
    }
  }
});*/
