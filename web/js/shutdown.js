document.querySelector("#shutdown").onclick = function() {  
    // Call python's function
    eel.shutdown()(function(){                      
      console.log("runned shutdown func...")
    })
}