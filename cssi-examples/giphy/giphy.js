const apiKey = "D9ra05ehCCnqpaPMsWU6GrFLdOxWGhtf";

console.log("Hello");

let url = "http://api.giphy.com/v1/gifs/search";
// `` (back tick) lets you combine strings
let query = `${url}?api_key=${apiKey}&q=kittens&limit=1`;
console.log(query);

function fetchGif(searchTerm) {
  console.log(searchTerm);
  //this will go get information from another page
  window.fetch(query).then(data => {
    //json is javascript object notation
    return data.json();
  }).then(json => {
    let results = json.data;
    let result = results[0];
    createImage(result.url);
    console.log(result);
  });
};

function createImage(url) {
  let image = document.createElement("img");
  image.src = url;
  document.body.appendChild(image);
}

fetchGif("kittens");
