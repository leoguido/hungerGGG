const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value

$('#bt_send_tributes_number').click(function(){

    n = $('#input_tributes_number').val();

    if( (n > 0) && (n != '') && (n < 12) ){
        $.ajax({
            url :'/send/tributes/number/',
            type:'POST',
            data: {'csrfmiddlewaretoken':csrf , 'tributes':n},
            success: function(html){
                $('#tribute_forms').append(html);
                $('#bt_send_tributes_number').prop('disabled', true);
                $('#submit_tributes').prop('disabled', false);
            }
        });
    }
});
