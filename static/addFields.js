$(document).ready(function() {
          
    $("#addLB").click(function() {
        
        var newInput = $("<label>DeviceName<input type='text' value='' name='devices-1-deviceName' id='devices-1-deviceName'></input></label><label>Device IP<input type='text' id='devices-1-deviceIP' name='devices-1-deviceIP' value=''></input></label><br/>")
            .attr("id", "device")
            .attr("name", "device")
        $("#devices").append(newInput);

    });

    $("#addPool").click(function() {
        
        var newInput = $("<label>DeviceName<input type='text' value='' name='devices-1-deviceName' id='devices-1-deviceName'></input></label><label>Device IP<input type='text' id='devices-1-deviceIP' name='devices-1-deviceIP' value=''></input></label><br/>")
            .attr("id", "device")
            .attr("name", "device")
        $("#devices").append(newInput);
    });
    
    $("#addVirtual").click(function() {
        
        var newInput = $("<label>DeviceName<input type='text' value='' name='devices-1-deviceName' id='devices-1-deviceName'></input></label><label>Device IP<input type='text' id='devices-1-deviceIP' name='devices-1-deviceIP' value=''></input></label><br/>")
            .attr("id", "device")
            .attr("name", "device")
        $("#devices").append(newInput);
    });

  });