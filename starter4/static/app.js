$(document).ready(function () {
    $(document).on('click', '#update', function () {
        $.get('/output', function (data) {
            // Update the <code> with the server output
            $('#output').text(data.output);
        })
    })
});