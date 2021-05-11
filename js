function check_date(elem,unwanted_date){
    date=elem.parentElement.parentElement.children[0].textContent;
    if(~unwanted_date.indexOf(date)){return false;}
    return true;
}
function check_count(elem){
    txt = elem.innerHTML;
    if(~txt.indexOf("0")){return false;}
    return true;
}
let elements=document.getElementById("required_element").nextElementSibling;
arr=elements.getElementsByClassName("b-doctor-schedule__item-tickets");
available_days=[];
for(let i=0;i<arr.length;i++){
    if(check_count(arr[i]) && check_date(arr[i],arguments[0])){available_days.push(arr[i])}
}
if(available_days.length){return available_days[0].parentElement.parentElement;}
