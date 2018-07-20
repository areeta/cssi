const apiKey = "D9ra05ehCCnqpaPMsWU6GrFLdOxWGhtf";

console.log("Hello");

// This is the base URL for the Giphy API.
let url = "http://api.giphy.com/v1/gifs/search";

// `` (back tick) lets you combine strings
let query = `${url}?api_key=${apiKey}&q=kittens&limit=1`;
console.log(query);

// This function fetches a gif that matches the given searchTerm.
function fetchGif(searchTerm) {
  console.log(searchTerm);
  //this will go get information from another page
  window.fetch(query).then(data => {
    //json is javascript object notation
    return data.json();
  }).then(json => {
    let results = json.data;
    let result = results[0];
    let imageUrl = result.images.downsized.url;
    createImage(imageUrl);
  });
};

function createImage(url) {
  let image = document.createElement("img");
  image.src = url;
  document.body.appendChild(image);
}

fetchGif("kittens");
