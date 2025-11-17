  window.onload = function(){
        console.log("loaded")
        let uName  ="";
        let io_client = io(); //js library
        let clientSocket = io_client.connect('http://localhost:5000');
        console.log(clientSocket)
      }

      