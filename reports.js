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
    //var container = document.getElementById('p1');
    const container = document.createElement("updateMessages");
    container.classList.add('list-group-item');

    for (var item of data) {
        // Create a container for each paragraph
        var paraContainer = document.createElement('div');
        paraContainer.classList.add('list-group-item'); // Add a class for styling if needed
    
        // Create a paragraph element for each item in the data
        var paragraph = document.createElement('div');
        paragraph.textContent = item['LatestGreetingTime'] + " reported an event at " + item['address'];
    
        // Append the paragraph to the container
        paraContainer.appendChild(paragraph);
    
        // Append the container to the main container
        container.appendChild(paraContainer);
    }
    
    // Assuming you have an existing element with an id "main-container" to append the containers to
    document.getElementById("updateMessages").appendChild(container);
    
  })
  .catch(error => {
    // Handle errors during the fetch
    console.error('Fetch error:', error);
  });