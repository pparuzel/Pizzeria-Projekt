/**
 * Created by Persi on 12/12/2017.
 */

function open_popup_div(div) {
    div.style.display = "inline-block";
}

function close_popup_div(div) {
    div.style.display = "none";
}

function add_amount(id) {
    var ele = parseInt(document.getElementById("pizza"+id).value)
    document.getElementById("pizza"+id).value = ele + 1;
}

function sub_amount(id) {
    var ele = parseInt(document.getElementById("pizza"+id).value)
    document.getElementById("pizza"+id).value = ele - 1;
}