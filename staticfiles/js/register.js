const element = document.getElementById("input");
element.addEventListener("input", validate);

function validate(e) {
  let value = e.target.value
  const regEx = /^[A-Za-z0-9]*$/
  if (!regEx.test(value) && value.length < 8) {
    document.getElementById("errorMsg").innerHTML = "8 character minimum, only contains a combination of letters and numbers";
  } else if (!regEx.test(value)) {
    document.getElementById("errorMsg").innerHTML = "only contains a combination of letters and numbers";
  } else if (regEx.test(value)) {
    if (value.length < 8) {
      document.getElementById("errorMsg").innerHTML = "8 characters minimum";
      return
    }
    document.getElementById("errorMsg").innerHTML = "";
  }

}