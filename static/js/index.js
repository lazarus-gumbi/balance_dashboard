
$('#check_balance').on('click', function (e) {
    e.preventDefault()
    $.ajax({
        type: "POST",
        url: "/get_balances",
        data: {},
        beforeSend: function () {
            $(".top").LoadingOverlay("show",);

        },
        success: function (response) {
            if (response.status === 'success') {
                $('.float_bal').text(response.balances.float)
                $('.check_bal').text(response.balances.check)
                $(".top").LoadingOverlay("hide", true);
            }else{
                $(".top").LoadingOverlay("hide", true);
                alert('error please try again')
            }
        },
        error: function (error) {
            alert('error please try again')
        }

    });
});