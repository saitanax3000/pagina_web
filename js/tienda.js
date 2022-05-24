let productos =[];
let total = 0;

function añadir(producto, precio){
    console.log(producto, precio);
    productos.push(producto);
    total= total + precio;
    document.getElementById("pagar").innerHTML = `Pagar $${total}`
}

function pay(){
    window.alert(productos.join(", \n"));
}

