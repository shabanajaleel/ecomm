$(document).ready(function(){
    $('#addrow').click(function(){
        var htm=$('#varientId').html()
        console.log(htm)
        var minus='<div class="col-lg-2">\
                    <div class="form-group" style="text-align: center;margin-top:30px;" id="but">\
                    <button type="button" class="btn btn-primary remove" >remove</button>\
                    </div>' 
        var newhtm="<div class='row varient '><div class='col-lg-10 row' id='varientId'>"+ htm +'</div>' + minus +'</div>'
        $('.varient:first').after(newhtm)

    })
 
   
})

$(document).on('click', '.remove', function () {
    $(this).parent().parent().parent().remove();
})

$(document).on('click', '#addnewrow', function () {
    console.log('hai')
        var htm='<div class="form-group col-3">\
        <label for="exampleInputUsername1">SKU Code</label>\
        <input type="text" name="code" maxlength="255" class="form-control form-control-sm" required="" id="id_Varient_name">\
        </div>\
        <div class="form-group col-3">\
        <label for="exampleInputUsername1" class="varient_Values1">dgwe</label>\
        <select name="varient_values" class="form-control form-control-sm VarientSelect"\
            required="" id="id_Varient_Values">\
        </select>\
        </div>\
        <div class="form-group col-2">\
        <label for="exampleInputUsername1">Selling Prize</label>\
        <input type="text" name="selling_price" maxlength="255" class="form-control form-control-sm" required="" id="id_Selling_Prize">\
        </div>\
        <div class="form-group col-2">\
        <label for="exampleInputUsername1">Display Price</label>\
        <input type="text" name="display_price" maxlength="255" class="form-control form-control-sm" required="" id="id_Display_Prize">\
        </div>\
        <div class="form-group col-2">\
        <label for="exampleInputUsername1">Product Stock</label>\
        <input type="number" name="product_stock" class="form-control form-control-sm" required>\
        </div>'
        console.log(htm)
        var minus='<div class="col-lg-2">\
                    <div class="form-group" style="text-align: center;margin-top:30px;" id="but">\
                    <button type="button" class="btn btn-primary remove" >remove</button>\
                    </div>' 
        var newhtm="<div class='row varient '><div class='col-lg-10 row' id='varientId'>"+ htm +'</div>' + minus +'</div>'
        $('.varient:first').after(newhtm)

    })
 
   
