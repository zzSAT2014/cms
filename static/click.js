var clicked = 0;
alert('fuck you')
function custom_onclick(){
   clicked += 1;
  document.getElementById('clicked').value = clicked;
}
document.onclick = custom_onclick;