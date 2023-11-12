fetch("https://09bqaa1thb.execute-api.us-east-1.amazonaws.com/dev")
  .then(response => {
    // Check if the request was successful (status code 2xx)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parse the JSON in the response
    return response.json();
  })
  .then(data => {
    // Process the data obtained from the API
    //let arr = eval(JSON.parse(data));


        const para = document.createElement("p");
        for (var item of data){
          for (const [key, value] of Object.entries(item)) {
            const node = document.createTextNode(`${key}: ${value}`);
            node.style = 'form-label'
            const lineBreak = document.createElement('br')
            para.appendChild(node);
            para.appendChild(lineBreak);
          }
          }

        const element = document.getElementById("div1");
        const child = document.getElementById("p1");
        element.insertBefore(para,child);
        

  })
  .catch(error => {
    // Handle errors during the fetch
    console.error('Fetch error:', error);
  });