<<<<<<< HEAD
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("Button");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
=======

var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var button = document.createElement("img");
  button.setAttribute("src", "delete.jpg");
  button.className = "close";
  myNodelist[i].appendChild(button);
>>>>>>> 3c740a1b2c6f3ba6067a6fe7d6a3123e82c502b5
}
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}
<<<<<<< HEAD
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);
=======

var list=document.querySelector('ul')
        list.addEventListener('click',function(ev){
            if(ev.target.tagName==='LI'){
                ev.target.classList.toggle('checked');
            }
        },false);
         
function newElement(){
    var li = document.createElement("li");
    var inputValue = document.getElementById("Task").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if(inputValue===''){
        alert("You wrote nothing)))");
    }else{
        document.getElementById("list").appendChild(li);
    }
    document.getElementById("Task").value="";
    var button = document.createElement("img");
    button.set Attribute("src","delete.jpg");
    button.className="close";
    li.appendChild(button);
    for (i=0; i<close.length; i++){
        close[i].onclick = function(){
            var div = this.parentElement;
            div.style.display="none";
        }
    }
}
>>>>>>> 3c740a1b2c6f3ba6067a6fe7d6a3123e82c502b5
