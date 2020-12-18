submissonButton = document.getElementById("formSubmission");
submissonButton.addEventListener("click", () => {
    sendRequest();
});

function sendRequest() {
    $.ajax({
    url: './../memberRequest',
    data: {
      'name': document.getElementById("name").value,
      'email': document.getElementById("email").value,
      'message': document.getElementById("message").value
    },
    dataType: 'json',
    success: function (data) {
        if (data.toString() == 'true') {
            docunent.getElementById("form").style.display = "none";
        } else {
            document.getElementById("notifyError").style.display = "block";
        }
      }
    });
}
