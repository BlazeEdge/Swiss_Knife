document.querySelector("#scan_disk").onclick = function() {  
    // Call python's function
    eel.scan_disk()(function(){                      
      console.log("Scaning disk...")
    })
}