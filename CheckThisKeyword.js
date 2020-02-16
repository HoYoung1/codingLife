#!/usr/bin/env node
intervalCrendential = null;

class Device {
    constructor(){
        console.log("constructor");
        this.first();
        this.flag = true
    }
   

    first() {
        this.second(true);
        setTimeout(function(){
            this.second(false);
        }.bind(this),3000);
        var intervalCrendential;
        this.second(false);
    }
    

    async second(flag) {

        
        if(flag){
            intervalCrendential = setInterval(this.update_kkk.bind(this), 1000); // every 30 minutes
            console.log(intervalCrendential+'ggggggggggg')
        }else{
            console.log('clearinterval');
            console.log(intervalCrendential);
            clearInterval(intervalCrendential);
        }
    }

    async update_kkk() {
        // console.log('what is this', this); // 
        this.getSomething(function() {
            console.log('whats this', this);
            console.log(2);
        }.bind(this));
        
    }
    async getSomething(callback){
        // console.log('here is this', this); // 
        console.log("get SomeThing");
        callback();
    }
}

async function main() {
        const iotDevice = new Device();
}

module.exports = main;

if (require.main === module) {
    main();
}
