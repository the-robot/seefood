$("#image-file").change(function(e){
  var image = e.target.files[0];

  var formData = new FormData();
  formData.append("picture", image);

  $.ajax({
    type: "POST",
    url: "/seefood",
    data: formData,
    cache:false,
    contentType: false,
    processData: false,

    success: function(data) {
      if (data.hotdog) {
        $("#is-hotdog").modal("show");
      } else {
        $("#is-not-hotdog").modal("show");
      }
    },

    error: function(data) {
        console.log("Error");
        console.log(data);
    },

    complete: function() {
      // clear fileinput
      $("#image-file").val('');
    }
  });
});

$("#about-button").click(function() {
  $("#about-modal").modal("show")
});

window.select_image = function() {
  $("#image-file").click()
}
