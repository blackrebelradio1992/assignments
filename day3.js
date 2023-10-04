// console.log("hey vic")

function makeAName(firstName, lastName) {
    let fullName = firstName + " " + lastName
    return fullName;
}

// console.log(makeAName("John", "Wick"));

// data types
    // strings

    greeting = "This is a string and this is how i work"

    let person = " mark"

    // console.log( greeting + person)
    // console.log(`${person}`)

    //numbers

    // console.log(Math.floor(3242/3));

    // booleans
    // console.log ('' == false)
    // console.log()

    // function xoTest(){
    //     let x = 8
    //     let o = 9

    //     return x === o ? true : false;
    // }

    // console.log(xoTest())

    // conparison operators

    // let myArray = ["Name", `${35}`, 35, false];
    // // console.log(myArray.slice(0,3));

    // let myArray2 = ["Name", `${35}`, 35, false,[4, 3, 1, "hoopla"]];

    // console.log(myArray2[4][3]);
    // myArray2[4].push(3)
    // console.log(myArray2)


    
    // loops

    // while, for Of, for in, for i,

    // let num = 100

    // while (num >0){
    //     console.log(num)
    //     num -= 1
    // }
    // console.log("end of while loop")

    // for (let i = 10; i > 0; i--){
    //     console.log(i)
    // }
    // console.log("end of for loop")

    let myObj = {
        "I": 1,
        "II": 2
    }

    // for (key, value of Object.entries(myObj)){
    //     console.log(key)
    //     console.log(value)
    // }
    // for (numeral)
    // let myString = "asdfghjkl;poiuygbnjkfghyg"

    // let letters = {}
    // for (ltr of myString){
    //     console.log(letters[ltr])
    //     if (letters[ltr]){
    //         letters[ltr] =+ 1
    //     }
    //     else{
    //         letters[ltr] = 1
    //     }
    // }
    // console.log(letters)

    const makeFullName = (firstName, lastName) => {
         `${firstName} ${lastName}`
        };

console.log(makeFullName("Benjamin", "Cohen")); // "Benjamin Cohen"