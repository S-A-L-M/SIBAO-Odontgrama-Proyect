/*class Tooth {
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
  
  const tooth1 = new Tooth(1);*/



// Obtener todas las partes del diente
const toothParts = document.querySelectorAll('.tooth-part');

// Agregar un manejador de eventos "click" a cada parte del diente
toothParts.forEach((part) => {
  part.addEventListener('click', () => {
    // Obtener el valor del color seleccionado
    const selectedColor = document.querySelector('.selected-color');
    const colorValue = selectedColor.getAttribute('value');

    // Aplicar el color seleccionado a la parte del diente
    part.style.backgroundColor = selectedColor.style.backgroundColor;
    part.setAttribute('data', colorValue);
  });
});

// Obtener todas las celdas de colores
const colorCells = document.querySelectorAll('.color');

// Agregar un manejador de eventos "click" a cada celda de color
colorCells.forEach((cell) => {
  cell.addEventListener('click', () => {
    // Remover la clase "selected-color" de todas las celdas de color
    colorCells.forEach((c) => {
      c.classList.remove('selected-color');
    });

    // Agregar la clase "selected-color" a la celda de color seleccionada
    cell.classList.add('selected-color');
  });
});

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

// Obtener todos los elementos con la clase "tooth"
const teeth = document.querySelectorAll('.tooth');

// Iterar sobre cada diente y agregar un evento de clic
teeth.forEach(tooth => {
  tooth.addEventListener('click', () => {
    // Obtener el número de diente
    const number = tooth.getAttribute("value");
    // Mostrar un mensaje con el número de diente seleccionado
    //alert(`Has seleccionado el diente ${number}`);
    // Cambiar el color del fondo del diente seleccionado
    //tooth.style.backgroundColor = 'yellow';
  });
});
