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

    success: function(data){
      if (data.hotdog) {
        $('#is-hotdog').modal('toggle');
      } else {
        $('#is-not-hotdog').modal('toggle');
      }
    },

    error: function(data){
        console.log("Error");
        console.log(data);
    }
  });
});

window.select_image = function() {
  $("#image-file").click()
}
