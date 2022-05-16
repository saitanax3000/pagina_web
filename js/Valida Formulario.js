$(document).ready(function() {
    
    $("#error").hide();
    //validamos el formulario al enviar los datos
    $("#formulario").submit(function(){
        var mensaje =""; //almacena el texto de las validaciones

        if($("#nombre").val().trim().length==0){
            // validamos el nombre que no quede en blanco
            mensaje = "El nombre no debe estar en blanco";

        }
        if($("#email").val().trim().length==0){
            mensaje = "El correo no debe estar en blanco";
        }


        if($("#ciudad").val().trim().length==0){
            mensaje = "La Ciudad de Residencia no debe estar en blanco";
        }

        if($("#comment").val().trim().length==0 ){
            mensaje="Debe comentar para la ONG"
        }

        if($("#comment").val().trim().length==0 && ($("#ciudad").val().trim().length==0) 
            && ($("#nombre").val().trim().length==0) && ($("#email").val().trim().length==0) && ($("#rut").val().trim().length==0)) {
            mensaje = "Debe Completar el formulario";
        }
        

        // Evitamos que se envien los datos del formulario
        if(mensaje !="")
        {
            $("#error").html(mensaje); //permite mostrar el mensaje de error en el div
            $("#error").show(); //permite mostrar el div
            event.preventDefault(); //evitamos el envio de los datos
        }

                
    });
})