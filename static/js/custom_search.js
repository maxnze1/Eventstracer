$(function () {
    $('#search').keyup(function () {
        $.ajax({
            method: 'POST',
            url: '/events/search/',
            data: {
                'search_text': $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSucess,
            dataType: 'html'
        })
    })
})

function searchSucess(data) {
    $('#search_display').html(data)
}