const place = document.querySelector("#place");
const noun = document.querySelector("#noun");
const verb = document.querySelector("#verb");
const adjective = document.querySelector("#adjective");
const plural_noun = document.querySelector("#plural_noun");

$(".form").on("submit", (evt) => {
  if (
    place.value.length < 3 ||
    noun.value.length < 3 ||
    verb.value.length < 3 ||
    adjective.value.length < 3 ||
    plural_noun.value.length < 3
  ) {
    evt.preventDefault();
    alert("Fields can't be less than 3 characters");
  }
});
