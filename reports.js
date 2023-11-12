(async () => {
    const res = await fetch('https://icanhazdadjoke.com/', {
      headers: { Accept: 'application/json' },
    });
    const json = await res.json();
    Object.entries(json).forEach(([key, value]) => {

        const para = document.createElement("p");
        const node = document.createTextNode(`${key}: ${value}`);
        para.appendChild(node);

        const element = document.getElementById("div1");
        const child = document.getElementById("p1");
        element.insertBefore(para,child);

    });
  })();
