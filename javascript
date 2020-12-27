<script>
    $(document).ready(function() {
$("#addNewDevice").click(function() {
    var newInput = $("<input required type='text' value=''></input>")
        .attr("id", "newInput")
        .attr("name", "newInput")
    $("#flist").append(newInput);
});
</script>


<script>
        $(document).ready(function() {
          
          $("#addLB").click(function() {
              var newInput = $("<label>DeviceName<input type='text' value='' name='devices-1-deviceName' id='devices-1-deviceName'></input></label><label>Device IP<input type='text' id='devices-1-deviceIP' name='devices-1-deviceIP' value=''></input></label><br/>")
                  .attr("id", "device")
                  .attr("name", "device")
              $("#devices").append(newInput);

          });
          
        });
    </script>