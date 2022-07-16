$(document).ready(function() {
  var last_valid_selection = null;
  $('#id_procedures').change(function(event) {
    if ($(this).val().length > 3) {
      $(this).val(last_valid_selection);
    } else {
      last_valid_selection = $(this).val();
    }
  });

  $("#id_dentist").change(function () {
    console.log('dentist_changed')
    var dentist = $(this).val();
    console.log(dentist)
    $.ajax({
        type: 'POST',
        url: '/booking/get-schedule/',
        data: {
            'dentist': dentist,
        },
        success: function (response) {
            var  new_options = response;
            console.log(response)
//            alert(new_options[0].id);  // works
            $('#id_schedule').empty();
            $.each(new_options, function(key, value) {

                $('#id_schedule')
                    .append($('<option>', { value : value.id })
                    .text(value.value));
            });
        }
    });
  });
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});
