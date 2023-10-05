// const { describe } = require("yargs")
// const { describe } = require("yargs")
const outsideOrNah = require("./day3.js")

describe("writing a test of if it works or not", () => {
    test("testing outsideOrNah", () => {
        expect(outsideOrNah("sunny").toBe("we outside"))
    })
})

// describe("checking a function w/ on parameters", () => {
//     test("see if it works at all", () => {
//         const  outsideOr = (weather) => {
//             if ( weather == "sunny") {
//                 return "outside"
//             } else {
//                 return "inside"
//             }
//         }
//         expect(outsideOr("sunny").toBe("outside"))
//     })
// })