
$('#id_Varient_Type').click(function(){
    var varient_type=$('#id_Varient_Type').val()
    console.log(varient_type)
    if (varient_type) {
        $("#VarientElement").show(500)
        $.ajax({
            type:'POST',
            url:'{%url "varient_select" %}',
            data:{
                'id':varient_type,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: (data) => {
                
                    console.log(data.Type)
                    let html_data = '<option value=0>None</option>';
                    data.values.forEach(function (data) {
                        html_data += `<option value="${data.id}">${data.varient_values}</option>`
                    });
                    $(".VarientSelect").html(html_data);
                    $('.varient_Values1').html('<p>' + data.Type + '</p>')
                }
        })
    }
})