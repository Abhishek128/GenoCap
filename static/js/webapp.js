$(function() {

    // Image upload form submit functionality
    $('#img-upload').on('submit', function(event){
        // Stop form from submitting normally
        event.preventDefault();

        // Get form data
        var form = event.target;
        var data = new FormData(form);

        if ($("#file-input").val() != "") {
            $("#file-submit").text("Uploading...")

            // Perform file upload
            $.ajax({
                url: "/upload",
                method: "post",
                processData: false,
                contentType: false,
                data: data,
                processData: false,
                dataType: "json",
                success: function(data) {
                    add_thumbnails(data);
                },
                error: function(jqXHR, status, error) {
                    if (jqXHR.status == 400) {
                        alert("Must submit a valid file (png, jpeg, or jpg)");
                    } else if (jqXHR.status == 404) {
                        alert("Cannot connect to model API server");
                    }
                },
                complete: function() {
                    $("#file-submit").text("Submit");
                    $("#file-input").val("");
                }
            })
        }
    });

    // Stop propagation so images aren't 'selected' when the more info icon is clicked
    $('.more-info-icon').on('click', function(e) {
        e.stopPropagation();
    });
});
