document.querySelector("#del_tmp").onclick = function() {  
    // Call python's function
    eel.del_tmp()(function(){                      
      console.log("runned del_tmp func...")
    })
}