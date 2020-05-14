
$(document).ajaxStart(function() { 

    $('#dt-select_wrapper').hide();
    $('#div_carga').show();

});
$(document).ajaxStop(function() { 

    $('#div_carga').hide();
    $('#dt-select_wrapper').show();

});

var table

function cargarDatos(){

    $.ajax({
      url: '/cargarVentas',
      type: 'POST',
      success: function(response) { 

        var dataSet = JSON.parse(response)['datos']

        table = $('#dt-select').DataTable({
          data: dataSet,
            columns: [
              {title: "id", visible: false},
              {title: "Producto"},
              {title: "Cliente"},
              {title: "Cantidad"},
              {title: "Precio"},
              {title: "Total"},
              {title: "Controles"}
            ],
            dom: 'Bfrtip',
            select: false
        });

      },
      error: function(error) {

        console.log(error);

      }
    });

  } 

cargarDatos()

var preciosProductos = []
var idProducto
var idCliente

$('#botonCrearVenta').click(function() {

  $.ajax({
      url: '/selectInventario',
      type: 'POST',
      async: false,
      success: function(response) {

        preciosProductos = []

        $("#sProductos").empty();

        var data = JSON.parse(response)['datos']

        if (data.length > 1){

          idProducto = data[0][0]

          $("#sProductos").append('<option value='+data[0][0]+' selected>'+data[0][1]+'</option>');
          let precioS = data[0][2]
          preciosProductos.push(parseFloat(precioS.substring(0, precioS.length-1)))
          $('#precioCP').val(parseFloat(precioS.substring(0, precioS.length-1)));
  
          for (var i = 1; i < data.length; i++) {
            $("#sProductos").append('<option value='+data[i][0]+'>'+data[i][1]+'</option>');
            let precio = data[i][2]
            preciosProductos.push(parseFloat(precio.substring(0, precio.length-1)))
          }

        }
        else {

          idProducto = data[0][0]

          $("#sProductos").append('<option value='+data[0][0]+' selected>'+data[0][1]+'</option>');
          let precioS = data[0][2]
          preciosProductos.push(parseFloat(precioS.substring(0, precioS.length-1)))
          $('#precioCP').val(parseFloat(precioS.substring(0, precioS.length-1)));

        }

      },
      error: function(error) {
          console.log(error);
      }
  });

  $.ajax({
      url: '/selectCliente',
      type: 'POST',
      async: false,
      success: function(response) {

        $("#sCliente").empty();

        var data = JSON.parse(response)['datos']

        if (data.length > 1) {

          idCliente = data[0][0]

          $("#sCliente").append('<option value='+data[0][0]+' selected>'+data[0][1]+'</option>');
  
          for (var i = 1; i < data.length; i++) {
            $("#sCliente").append('<option value='+data[i][0]+'>'+data[i][1]+'</option>');
          }

        }
        else {

          idCliente = data[0][0]

          $("#sCliente").append('<option value='+data[0][0]+' selected>'+data[0][1]+'</option>');

        }

      },
      error: function(error) {
          console.log(error);
      }
  });

  $('#modalCrearVenta').modal('show');

  return false

});

$('#sProductos').on('change', function() {

  idProducto = this.value

  $('#precioCP').val(preciosProductos[this.selectedIndex]);

  let cantidad = parseInt($('#cantidadCP').val())
  let precio = parseFloat($('#precioCP').val())

  $('#totalCP').val(cantidad*precio)

});

$("#cantidadCP").on("change paste keyup", function() {

  let cantidad = parseInt($(this).val())
  let precio = parseFloat($('#precioCP').val())

  $('#totalCP').val(cantidad*precio)
  
});

$('#sCliente').on('change', function() {

  idCliente = this.value

});


function validarC(){

  let valido = true

  if ($('#cantidadCP').val() == "" || $('#precioCP').val() == "" || $('#totalCP').val() == "" || parseInt($('#cantidadCP').val()) < 0 || parseFloat($('#precioCP').val()) < 0 || parseFloat($('#totalCP').val()) < 0){

    valido = false
  }

  return valido

}

$('#crearVenta').click(function() {

  let data = { sProductos : idProducto, sCliente : idCliente, cantidadCP : $('#cantidadCP').val(), precioCP : $('#precioCP').val(), totalCP : $('#totalCP').val() }

  if (validarC()){

      $('#modalCrearVenta').modal('hide');

        $.ajax({
            url: '/crearVenta',
            data: data,
            type: 'POST',
            async:false,
            success: function(response) {

              table.destroy();
              cargarDatos()

            },
            error: function(error) {

                console.log(error);

            }
        });

        return false

      }
      else {

        return false

      }

    });

function borrar(data){

    $.ajax({
            url: '/borrarVenta',
            data: { idVenta : data },
            type: 'POST',
            async:false,
            success: function(response) {

              table.destroy();
              cargarDatos()

            },
            error: function(error) {

                console.log(error);

            }
        });

    return false

}


function vender(data){

    $.ajax({
            url: '/realizarVenta',
            data: { idVenta : data },
            type: 'POST',
            async:false,
            success: function(response) {

              table.destroy();
              cargarDatos()

            },
            error: function(error) {

                console.log(error);

            }
        });

    return false

}