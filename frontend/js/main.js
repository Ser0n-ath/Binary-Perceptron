var colorPicker = new iro.ColorPicker("#picker", {
    // Set the size of the color picker
    width: 220,
    // Set the initial color to pure red
    color: "#f00",
  });


colorPicker.on('color:change', function(color) {
    console.log(color.rgb);

    //Send request to server to update current. 
});


console.log(hex);