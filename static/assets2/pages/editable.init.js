/**
 * Theme: Unikit - Responsive Bootstrap 5 Admin Dashboard
 * Author: Mannatthemes
 * Editable Js
 */
//define data array
var tabledata = [
    {id:1, name:"پریسا محمدی", progress:12, gender:"مرد", rating:1, col:"red", dob:"1400/2/18", car:1},
    {id:2, name:"پریسا محمدی", progress:1, gender:"زن", rating:2, col:"blue", dob:"1400/8/11", car:true},
    {id:3, name:"پریسا محمدی", progress:42, gender:"زن", rating:0, col:"green", dob:"1400/5/15", car:"true"},
    {id:4, name:"پریسا محمدی", progress:100, gender:"مرد", rating:1, col:"orange", dob:"1400/10/19"},
    {id:5, name:"پریسا محمدی", progress:16, gender:"زن", rating:5, col:"yellow", dob:"1400/11/21"},
    {id:6, name:"پریسا محمدی", progress:38, gender:"مرد", rating:4, col:"red", dob:"1400/12/29", car:1},
    {id:1, name:"پریسا محمدی", progress:12, gender:"مرد", rating:1, col:"red", dob:"1400/2/18", car:1},
    {id:2, name:"پریسا محمدی", progress:1, gender:"زن", rating:2, col:"blue", dob:"1400/8/11", car:true},
    {id:3, name:"پریسا محمدی", progress:42, gender:"زن", rating:0, col:"green", dob:"1400/5/15", car:"true"},
    {id:4, name:"پریسا محمدی", progress:100, gender:"مرد", rating:1, col:"orange", dob:"1400/10/19"},
    {id:5, name:"پریسا محمدی", progress:16, gender:"زن", rating:5, col:"yellow", dob:"1400/11/21"},
    {id:6, name:"پریسا محمدی", progress:38, gender:"مرد", rating:4, col:"red", dob:"1400/12/29", car:1},
];

var dateEditor = function(cell, onRendered, success, cancel){
    //cell - the cell component for the editable cell
    //onRendered - function to call when the editor has been rendered
    //success - function to call to pass the successfuly updated value to Tabulator
    //cancel - function to call to abort the edit and return to a normal cell

    //create and style input
    var cellValue = moment(cell.getValue(), "DD/MM/YYYY").format("YYYY-MM-DD"),
    input = document.createElement("input");

    input.setAttribute("type", "date");

    input.style.padding = "4px";
    input.style.width = "100%";
    input.style.boxSizing = "border-box";

    input.value = cellValue;

    onRendered(function(){
        input.focus();
        input.style.height = "100%";
    });

    function onChange(){
        if(input.value != cellValue){
            success(moment(input.value, "YYYY-MM-DD").format("DD/MM/YYYY"));
        }else{
            cancel();
        }
    }

    //submit new value on blur or change
    input.addEventListener("blur", onChange);

    //submit new value on enter
    input.addEventListener("keydown", function(e){
        if(e.keyCode == 13){
            onChange();
        }

        if(e.keyCode == 27){
            cancel();
        }
    });

    return input;
};

//Build Tabulator
var table = new Tabulator("#editable", {
    height:"310px",
    layout:"fitColumns",
    reactiveData:true, //turn on data reactivity
    data:tabledata, //load data into table
    columns:[
        {title:"نام", field:"name", width:150, editor:"input"},
        {title:"مکان", field:"location", width:130, editor:"autocomplete", editorParams:{allowEmpty:true, showListOnEmpty:true, values:true}},
        {title:"پیشرفت", field:"progress", sorter:"number", hozAlign:"left", formatter:"progress", width:140, editor:true},
        {title:"جنسیت", field:"gender", editor:"select", editorParams:{values:{"male":"Male", "female":"Female", "unknown":"Unknown"}}},
        {title:"رتبه بندی", field:"rating",  formatter:"star", hozAlign:"center", width:100, editor:true},
        {title:"تاریخ تولد", field:"dob", hozAlign:"center", sorter:"date", width:140, editor:dateEditor},
        {title:"درایور", field:"car", hozAlign:"center", editor:true, formatter:"tickCross"},
    ],
});

//add row to bottom of table on button click
document.getElementById("reactivity-add").addEventListener("click", function(){
    tabledata.push({name: "من یک ردیف جدید هستم", progress:100, gender:"مرد"});
});

//remove bottom row from table on button click
document.getElementById("reactivity-delete").addEventListener("click", function(){
    tabledata.pop();
});

//update name on first row in table on button click
document.getElementById("reactivity-update").addEventListener("click", function(){
    tabledata[0].name = "به روز رسانی شده ام";
});