

function p() {
    let abc = 'abc';
    return renderText();

    function renderText(){
        console.log(abc);
    }
}
p()