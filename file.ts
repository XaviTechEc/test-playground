const word_1: string = "Hello";
const num_1: number = 1;

console.log();
console.log();
console.log();
console.log();
console.log("Hello world");

[1, 2, 3, 4].forEach((item) => {
  if (item % 2 === 0) {
    return;
  }
});

console.log(word_1, num_1);
console.log("");

// "hello" "hello" "hello" "hello"

/**
 * e | E -> end
 * b | B-> begin w -> word;
 * a | A -> append
 * i | I-> insert
 * $ -> end of line
 * 0 -> start of the line
 * f -> find first
 * ; -> find occurrences -> next
 * , -> find occurrences <- previous
 * 4ft -> find 4th match in the current line
 * = (x2) -> indent current line
 * y -> yank
 * yy -> yank line
 * gg -> doc start
 * shift + g -> doc end
 * shift + m -> doc middle
 * ctrl + r -
 * dw -> delete word
 * p -> paste
 * u -> undo
 * ctrl + r -> redo
 * % -> current bracket end | start
 * diw -> delete in word
 * daw -> delete around word
 * yip -> yank in paragraph
 * ci( -> change inside brackets
 *
 **/
